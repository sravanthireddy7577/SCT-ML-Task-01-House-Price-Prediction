# House Price Prediction using Linear Regression

## 📌 Project Overview

This project implements a Linear Regression model to predict house prices based on:

- Above-ground living area (square footage)
- Number of bedrooms
- Number of full bathrooms

This project was completed as part of my Machine Learning Internship at SkillCraft Technology.

---

## 📊 Dataset

The project uses the **House Prices: Advanced Regression Techniques** dataset from Kaggle.

Dataset:
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data

The target variable is:

- `SalePrice` — House selling price

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Streamlit

---

## 🤖 Machine Learning Approach

### Features

The following features are used to predict house prices:

- `GrLivArea` — Above-ground living area in square feet
- `BedroomAbvGr` — Number of bedrooms above basement level
- `FullBath` — Number of full bathrooms above grade

### Target Variable

- `SalePrice` — House selling price

### Data Splitting

The dataset is divided into:

- **80% Training Data**
- **20% Testing Data**

A Linear Regression model is trained using the training data and evaluated using the testing data.

---

## 📈 Model Performance

The model was evaluated using Mean Absolute Error (MAE) and R² Score.

| Metric | Score |
|---|---:|
| Mean Absolute Error (MAE) | 35,788.06 |
| R² Score | 0.6341 |

### Interpretation

- The **MAE** indicates that the model's predictions differ from the actual house prices by approximately **$35,788 on average**.
- The **R² Score of 0.6341** means the model explains approximately **63.41% of the variation in house prices** using the selected features.

---

## 📉 Visualization

The project includes a scatter plot comparing:

- **Actual House Prices**
- **Predicted House Prices**

The visualization helps evaluate how closely the predicted prices follow the actual prices.

---

## 📁 Project Structure

```text
House-price-prediction/
│
├── house_price_pred.py
├── app.py
├── requirements.txt
├── README.md
└── MLHousePriceDataSet.csv
```
## 📌 About

This project was created as part of my Machine Learning Internship at SkillCraft Technology.

It demonstrates the use of Linear Regression to predict house prices based on living area, number of bedrooms, and number of full bathrooms.

## 👩‍💻 Author

**Sravanthi Reddy**

Machine Learning Intern at SkillCraft Technology

GitHub: [@sravanthireddy7577](https://github.com/sravanthireddy7577)
