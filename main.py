import streamlit as st
from transformers import pipeline

def summarize_text(article):
    summarizer = pipeline('summarization')
    summary = summarizer(article, max_length=180, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def copy_text(text):
    st.experimental_set_query_params(copy=text)
    st.info("Text copied to clipboard")


st.title("Text Summarization App")

# Text input field
user_input = st.text_area("Enter the text to summarize")
st.write(f"Length of Article: {len(user_input.split(' '))}")

if st.button("Summarize"):
    if user_input:
        summary_text = summarize_text(user_input)

        # Display summarized text
        st.text_area("Summarized Text", value=summary_text, height=200)

        # Display length of article and summary
        st.write(f"Length of Summary: {len(summary_text.split(' '))}")

         # Copy to clipboard
        copy_text(summary_text)

        # Retrieve copied text from query parameters
        copied_text = st.experimental_get_query_params().get("copy", "")
        if copied_text:
            st.experimental_set_query_params()
            st.experimental_rerun()
    else:
        st.warning("Please enter some text.")
