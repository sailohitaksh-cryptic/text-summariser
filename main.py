import streamlit as st
from transformers import pipeline

def summarize_text(article):
    summarizer = pipeline('summarization')
    summary = summarizer(article, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']


st.title("Text Summarization App")

# Text input field
user_input = st.text_area("Enter the text to summarize")
st.write(f"Length of Article: {len(user_input.split(' '))-1}")

if st.button("Summarize"):
    if user_input:
        summary_text = summarize_text(user_input)

        # Display summarized text
        st.subheader("Summarized Text")
        st.text_area("Summarised Text",summary_text)

        # Display length of article and summary
        
        st.write(f"Length of Summary: {len(summary_text.split(' '))}")

        # Copy to clipboard
        st.button("Copy Summarized Text", to_copy=summary_text)
    else:
        st.warning("Please enter some text.")
