# Accident Risk Prediction

A Machine Learning project that predicts the **risk of road accidents** using historical accident data and statistical learning models.

Road accidents cause millions of injuries and deaths every year, and predicting where accidents are most likely to occur — or how severe they might be — can help governments, drivers, and planners improve **road safety and decision-making**.

---

## 🚀 Project Overview

This project uses historical accident data to build a supervised machine learning model that estimates the **risk of an accident** (or severity, depending on the dataset) based on relevant features such as traffic conditions, weather, location, time, and other factors.

👉 Users can upload a dataset or use a test dataset to run the model and get prediction


---

## 🧠 What This Project Does

This project performs:

1. **Exploratory Data Analysis (EDA)**  
   * Understands patterns in accident data  
   * Visualizes key features (location, time, severity, etc.)

2. **Data Preprocessing**
   * Cleans missing values
   * Encodes categorical variables
   * Scales numerical features

3. **Machine Learning Model Training**
   * Fits models such as Random Forest, Logistic Regression, XGBoost, etc.
   * Evaluates accuracy and performance

4. **Prediction**
   * Takes new input data
   * Generates accident risk scores or risk labels

5. **Output**
   * Saves results to `submission.csv`  
   * Can be used to visualize high-risk areas

---

## 🧪 Datasets

The repository includes:

* **submission_data.csv** – Raw dataset used for model prediction
* **submission.csv** – Resulting predictions

Place additional datasets in the `data/` folder if needed.

---

## 📦 Requirements

Install required libraries:

```bash
pip install -r requirements.txt
```

## 📈 Model Results & Performance

The **Gradient Boosting Regressor** was trained and evaluated to predict accident risk.  
The model shows strong performance on both training and validation datasets.

---

### 🔹 Training Performance (Gradient Boosting)

- **Mean Squared Error (MSE):** 0.0032  
- **Root Mean Squared Error (RMSE):** 0.0569  
- **Mean Absolute Error (MAE):** 0.0443  
- **R² Score:** 0.8833  

---

### 🔹 Validation Performance

- **Mean Squared Error (MSE):** 0.0032  
- **Root Mean Squared Error (RMSE):** 0.0570  
- **Mean Absolute Error (MAE):** 0.0444  
- **R² Score:** 0.8824  

---

### 📌 Interpretation

- The high **R² score (~0.88)** indicates that the model explains most of the variance in accident risk.
- Very similar training and validation metrics confirm **good generalization**.
- Low error values suggest accurate and stable predictions.

---

## 🛠 Technologies Used

- **Python** – Core programming language  
- **Pandas & NumPy** – Data manipulation and numerical computing  
- **scikit-learn** – Machine learning models and evaluation  
- **Jupyter Notebook** – Interactive analysis and experimentation  
- **CSV Files** – Dataset storage and prediction results  

---

## 📊 Example Use Cases

This system can be applied in real-world scenarios such as:

- **Government Agencies**  
  Identify and map accident-prone zones to improve road safety.

- **Insurance Companies**  
  Assess accident risk for policy pricing and claims analysis.

- **Traffic & Urban Planners**  
  Prioritize infrastructure improvements based on risk prediction.

- **Data Scientists & Researchers**  
  Experiment with predictive modeling and safety analytics.
