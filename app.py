import streamlit as st
import joblib


#                              Page Configuration

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

#                              Load Model

model = joblib.load("house_price_model.pkl")


#                               Sidebar

st.sidebar.title("🏠 House Price Prediction")

st.sidebar.info("""
### About Project

This Machine Learning model predicts house prices using Linear Regression.

**Features Used**
- Area
- Bedrooms
- Bathrooms
- House Age
- Parking

Developed using:
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
""")

# Main Title

st.title("🏠 House Price Prediction System")

st.write("Enter the house details below to estimate its price.")

st.divider()


# Input Section

col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "Area (sqft)",
        min_value=100,
        max_value=10000,
        value=1500,
        step=50
    )

    bedroom = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=3
    )

    bathroom = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )

with col2:
    age = st.number_input(
        "House Age (Years)",
        min_value=0,
        max_value=100,
        value=10
    )

    parking = st.number_input(
        "Parking Spaces",
        min_value=0,
        max_value=10,
        value=2
    )

st.write("")

# Prediction button

if st.button("🔍 Predict House Price", use_container_width=True):

    input_data = [[area, bedroom, bathroom, age, parking]]

    prediction = model.predict(input_data)[0]

    st.success("Prediction Generated Successfully ✅")

    st.metric(
        label="Estimated House Price",
        value=f"{prediction:,.2f}"
    )

    st.info(f"""
**Input Summary**

- Area : {area} sqft
- Bedrooms : {bedroom}
- Bathrooms : {bathroom}
- House Age : {age} Years
- Parking : {parking}
""")


# Footer

st.divider()

st.caption("Developed using Streamlit & Scikit-Learn...")
st.caption("©vxdvicky House Price Prediction System. All rights reserved.")