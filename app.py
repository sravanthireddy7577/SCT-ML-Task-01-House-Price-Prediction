import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# Load the dataset
df = pd.read_csv("MLHousePriceDataSet.csv")


# Select features and target
X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = df['SalePrice']


# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)


# Title
st.title("🏠 House Price Prediction")

st.write(
    "Predict the price of a house using its living area, "
    "number of bedrooms, and number of bathrooms."
)


# Section
st.subheader("Enter House Details")


# Inputs
gr_liv_area = st.number_input(
    "📐 Square Footage (GrLivArea)",
    min_value=100,
    value=1500,
    step=100
)

bedrooms = st.number_input(
    "🛏️ Number of Bedrooms",
    min_value=1,
    value=3,
    step=1
)

full_bath = st.number_input(
    "🛁 Number of Full Bathrooms",
    min_value=1,
    value=2,
    step=1
)


# Prediction
if st.button("🔮 Predict House Price"):

    input_data = pd.DataFrame(
        [[gr_liv_area, bedrooms, full_bath]],
        columns=['GrLivArea', 'BedroomAbvGr', 'FullBath']
    )

    prediction = model.predict(input_data)[0]

    st.success("Prediction completed successfully!")

    st.subheader("💰 Predicted House Price")

    st.metric(
        label="Estimated Price",
        value=f"${prediction:,.2f}"
    )

    st.subheader("🏡 House Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Square Footage**")
        st.write(f"{gr_liv_area:,} sq ft")

    with col2:
        st.write("**Bedrooms**")
        st.write(bedrooms)

    with col3:
        st.write("**Bathrooms**")
        st.write(full_bath)