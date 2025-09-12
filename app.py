import streamlit as st
from transformers import pipeline

# Load model
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

st.title("📚 AI Tutor (English + Hindi)")
st.write("Ask a question in English or Hindi and get a simple explanation!")

# User input
user_input = st.text_area("Enter your question:")

if st.button("Get Answer"):
    if user_input:
        result = qa_pipeline(user_input, max_new_tokens=128, do_sample=False)
        st.success(result[0]['generated_text'])
    else:
        st.warning("Please enter a question!")
