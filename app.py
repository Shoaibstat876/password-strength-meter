import streamlit as st
import re
import random
import string

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "Your password is secure! 🎉", "green"
    elif score == 3:
        return "⚠️ Moderate Password", "Consider adding more security features.", "orange"
    else:
        return "❌ Weak Password", "Improve it using the suggestions below.", "red", feedback

# Function to generate a strong password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Check the security of your password and improve it!")

password = st.text_input("Enter your password", type="password")

if password:
    strength, message, color, *feedback = check_password_strength(password)
    st.markdown(f"<h3 style='color:{color};'>{strength}</h3>", unsafe_allow_html=True)
    st.write(message)

    if feedback:
        st.write("🔹 **Suggestions:**")
        for tip in feedback[0]:
            st.write("- " + tip)

st.write("Want a secure password? Click below to generate one:")
if st.button("Generate Strong Password"):
    st.text(generate_password())
