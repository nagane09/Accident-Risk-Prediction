from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load model + preprocessor
MODEL_PATH = "models/model.joblib"
PREPROCESSOR_PATH = "models/preprocessor.joblib"

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = None

    if request.method == "POST":
        try:
            # Collect inputs from form
            data = [
                request.form["id"],
                request.form["road_type"],
                request.form["num_lanes"],
                request.form["curvature"],
                request.form["speed_limit"],
                request.form["lighting"],
                request.form["weather"],
                request.form["road_signs_present"],
                request.form["public_road"],
                request.form["time_of_day"],
                request.form["holiday"],
                request.form["school_season"],
                request.form["num_reported_accidents"],
            ]

            # Convert to NumPy array
            arr = np.array([data], dtype=object)

            # Preprocess
            processed = preprocessor.transform(arr)

            # Predict
            pred = model.predict(processed)[0]
            prediction_text = f"Predicted Accident Risk: {pred:.4f}"

        except Exception as e:
            prediction_text = f"Error: {str(e)}"

    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
