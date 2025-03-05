import streamlit as st

def convert_units(category, from_unit, to_unit, value):
    conversion_factors = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Inch": 39.3701, "Foot": 3.28084},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
        "Temperature": {"Celsius": 1, "Fahrenheit": 1, "Kelvin": 1},
        "Area": {"Square Meter": 1, "Square Kilometer": 1e-6, "Square Foot": 10.764, "Square Inch": 1550.003, "Acre": 0.0002471},
        "Volume": {"Cubic Meter": 1, "Liter": 1000, "Milliliter": 1000000, "Gallon": 264.172, "Cubic Foot": 35.315},
        "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400, "Week": 1/604800}
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value * (conversion_factors[category][from_unit] / conversion_factors[category][to_unit])

st.set_page_config(page_title="Unit Converter", layout="centered")
st.markdown(""" <h1 style='text-align: center; color: #4A90E2; margin-bottom: 0;'>Unit Converter</h1> """, unsafe_allow_html=True)

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature", "Area", "Volume", "Time"], key="category")
units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Inch", "Foot"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Area": ["Square Meter", "Square Kilometer", "Square Foot", "Square Inch", "Acre"],
    "Volume": ["Cubic Meter", "Liter", "Milliliter", "Gallon", "Cubic Foot"],
    "Time": ["Second", "Minute", "Hour", "Day", "Week"]
}

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", units[category], key="from_unit")
with col2:
    to_unit = st.selectbox("To", units[category], key="to_unit")

value = st.number_input("Enter Value", min_value=0.0, format="%.10f")

if st.button("Convert", use_container_width=True):
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"Converted Value: {result:.10f} {to_unit}")

st.markdown(""" <style> 
div.stButton > button { background-color: #4A90E2; color: white; font-size: 18px; border-radius: 10px; }
div[data-testid="stSelectbox"] { cursor: pointer; }
.css-10trblm > a { display: none; }
</style> """, unsafe_allow_html=True)