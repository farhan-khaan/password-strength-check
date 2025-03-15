import streamlit as st  # Streamlit
import re  # Regular Expression

# Set Page Config
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# CSS Styling to Change Input Box Color
st.markdown("""
    <style>
    /* Change Input Box Color */
    div[data-baseweb="input"] {
        background-color: #222 !important;  /* Dark background */
        border-radius: 5px !important;
        text-color = black
    }
    input {
        color: white !important;  /* White text */
        text-align: center;
    }
    /* Style the Button */
    .stButton>button {
        background-color: #444 !important;
        color: white !important;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #666 !important;
        color: #fff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Welcome Message with Icon
st.markdown("## 🔒 Welcome to the Password Strength Checker")
st.write("We will give you helpful tips to create a **strong password** 🔑")

# Function to Check Password Strength
def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ **Password should be at least 8 characters long**")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ **Include both UPPERCASE and lowercase letters**")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ **Add at least one number (0-9)**")
    
    if re.search(r'[!@#$%^&()*]', password):
        score += 1
    else:
        feedback.append("❌ **Use at least one special character (!@#$%^&*)**")

    # Display Strength
    if score == 4:
        st.success("✅ **Your password is strong!**")
    elif score == 3:
        st.warning("⚠️ **Your password is medium strength. Consider improving it.**")
    else:
        st.error("🚨 **Your password is weak!** Please follow the suggestions below.")

    # Show Feedback in Expander
    if feedback:
        with st.expander("💡 Improvement Suggestions"):
            for tip in feedback:
                st.write(tip)

# Password Input (Now with custom background color!)
password = st.text_input("🔑 Enter your password", type="password", help="Enter your password to check its strength")

# Button to Check Password
if st.button("🔍 Check Password"):
    if password:
        check_password(password)
    else:
        st.warning("⚠️ Please enter a password first.")

# Footer
st.markdown("© 2025 **Farhan Khan** | 🔐 Secure Your Passwords!")
