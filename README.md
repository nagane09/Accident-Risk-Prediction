# 🔮 Power Consumption Prediction

This project predicts power consumption (kW) using machine learning and provides a real-time interface through a Flask web application.

---

## 🌐 Flask Web Application

- **Deployed using Flask** for real-time predictions.
- **User interface**: HTML form for inputting data.
- **Backend**: Validates input and handles errors.
- **Output**: Displays predicted power consumption instantly.

---

## 🧩 App Features

- HTML form for user input
- Backend validation & error handling
- Instant prediction of power consumption

---

## 🧪 Flask Route Logic

**GET**: Renders the input form  
**POST**:
1. Collects user inputs
2. Converts inputs to numerical format
3. Predicts power consumption using the trained model
4. Returns the predicted value


---

## 🧠 Mathematical Intuition (High-Level)

The final model (`XGBRegressor`) works by:

1. Training multiple decision trees on random subsets of data.
2. Averaging predictions to reduce variance.

\[
\hat{y} = \frac{1}{N} \sum_{i=1}^{N} f_i(x)
\]

Where:  
- \(f_i(x)\) is the prediction from the \(i\)-th tree  
- \(N\) is the number of trees  

This approach reduces overfitting compared to a single decision tree.

---

## 🚀 Future Improvements

- Hyperparameter tuning with `GridSearchCV`
- Time-series specific models (LSTM, Prophet)
- Feature importance visualization
- Docker-based deployment
- REST API integration

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Flask
- Joblib
- HTML/CSS

---

## 📊 Model Training (High-Level Overview)

- **Data preprocessing**:
  - Categorical features → OneHotEncoding
  - Numerical features → StandardScaler
- **Models tested**: Gradient Boosting, XGBoost, Random Forest, etc.
- **Evaluation metrics**: MSE, RMSE, MAE, R²
- **Final model**: `XGBRegressor` with tuned hyperparameters

```python
from xgboost import XGBRegressor

xgb_model = XGBRegressor(
    n_estimators=1000,
    learning_rate=0.03,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    tree_method="hist",
    random_state=42
)
xgb_model.fit(X_train_processed, y_train)
````

-Validation results:
-MSE: 0.00317
-MAE: 0.0437
-R²: 0.8852
-Model and preprocessor saved using joblib:
