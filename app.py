import streamlit as st
from transformers import pipeline

# Initialize the summarizer and question-answering pipelines
summarizer = pipeline("summarization")
qa_pipeline = pipeline("question-answering")

def summarize_text(text):
    return summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

def answer_question(question, context):
    return qa_pipeline(question=question, context=context)['answer']

# Streamlit UI setup
st.set_page_config(page_title="Roshan Consulting", page_icon=":robot:", layout="wide")

# Add logo
st.image("roshan_logo.png", use_column_width=True)

st.title("Roshan Consulting - Your Virtual Assistant")

st.write("### How can I assist you today?")

# Text input for customer inquiries or articles
text_input = st.text_area("Paste an article or text for summarization here", height=200)
question_input = st.text_input("Ask a question about our business")

# Context for QA (could be expanded to use dynamic data)
business_context = """
We offer a variety of services including customer support, product information, and more. 
Our hours are Monday to Friday from 9 AM to 6 PM. We are located at 123 Business Street, 
Your City. You can reach us at support@yourbusiness.com or call us at (555) 123-4567.
"""

# Buttons for user actions
if st.button('Summarize Text'):
    if text_input:
        with st.spinner('Generating summary...'):
            summary = summarize_text(text_input)
            st.write("### Summary:")
            st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

if st.button('Get Answer'):
    if question_input:
        with st.spinner('Finding answer...'):
            answer = answer_question(question_input, business_context)
            st.write("### Answer:")
            st.write(answer)
    else:
        st.write("Please ask a question.")

