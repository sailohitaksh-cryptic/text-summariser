![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Text-Transformer&fontSize=100&animation=fadeIn&fontAlignY=38&theme=tokyonight)

This is a web application that provides text summarization functionality using the Streamlit framework and the Transformers library.

## Overview

The Text Summarization App allows users to enter a text article and generate a summarized version of the input. The application utilizes the Hugging Face Transformers library to perform the text summarization task.

## How to Use

1. Access the web application at [https://text-summariser.streamlit.app/](https://text-summariser.streamlit.app/).
2. Enter the text you want to summarize in the provided text area.
3. The length of the input article will be displayed.
4. Click the "Summarize" button to generate the summary.
5. The summarized text will be displayed in a separate text area.
6. The length of the summary will also be shown.
7. You can copy the summarized text to the clipboard by clicking the "Copy Summarized Text" button.

## Dependencies

The following dependencies are required to run the application:

- Streamlit
- Transformers

You can install the dependencies using the following command:

    pip install streamlit transformers


# Run Locally
To run the Text Summarization App locally, follow these steps:

1. Clone the repository:

    `git clone https://github.com/sailohitaksh-cryptic/text-summariser.git`

2. Install the dependencies as mentioned above:
   `pip install -r requirements.txt`
   
3. Run the application:
   `streamlit run main.py`

4. Access the application in your web browser at http://localhost:8501.

About
This web application was developed by Sai Lohitaksh. It is based on the Streamlit framework and utilizes the Transformers library for text summarization. For more information, please contact [here](rainasai603@gmail.com).
