import re
import streamlit as st

# Page Styling
st.set_page_config(page_title="Password Strength Checker By Fahad Memon", page_icon="🔐", layout="centered")

# Custom CSS for Professional UI
st.markdown("""
    <style>
        /* Center content */
        .main {
            text-align: center;
            font-family: 'Arial', sans-serif;
            color: white;
            
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
        }
        /* Stylish input */
        .stTextInput input {
            width: 100% !important;
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            background-color: #252525;
            color: white;
        }
        /* Attractive button */
        .stButton button {
            width: 100%;
            background: linear-gradient(45deg, #4CAF50, #2e7d32);
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(76, 175, 80, 0.3);
            transition: 0.3s ease-in-out;
        }
        .stButton button:hover {
            background: linear-gradient(45deg, #2e7d32, #1b5e20);
            transform: scale(1.05);
        }
        /* Expander styling */
        .st-expander {
            background-color: #252525 !important;
            border-left: 5px solid #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# Page title and description with styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Enter your password below to check its security level. 🔍</p>", unsafe_allow_html=True)

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Password Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters long**.")

    # Upper & Lower Case Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*)**.")

    # Display password strength results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    return feedback  # Return feedback list

# Input field inside centered container
st.markdown("<div class='main'>", unsafe_allow_html=True)
password = st.text_input("Enter your password: ", type="password", help="Ensure your password is strong 🔒")
st.markdown("</div>", unsafe_allow_html=True)

# Button Working
if st.button("🔍 Check Strength"):
    if password:
        feedback = check_password_strength(password)

        # Show Feedback
        if feedback:
            with st.expander("🔍 **Improve Your Password** "):
                for item in feedback:
                    st.write(item)
    else:
        st.warning("⚠️ Please enter a password first!")  # Show warning if password is empty
