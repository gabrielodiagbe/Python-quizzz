import streamlit as st

st.title("Python Practice – Lesson 1")

question = "Fill in the missing code to print 'Hello, World!'"
st.write(question)

answer = st.text_input("Type your code here:")

if answer:
    if answer.strip() == "print('Hello, World!')":
        st.success("✅ Correct! Proceed to the next question.")
    else:
        st.error("❌ Wrong, try again.")
