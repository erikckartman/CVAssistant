import streamlit as st
import pdfplumber, re

from model import analyze_cv, extract_text_from_url

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

st.title("CV Assistant")

cv = st.file_uploader("Insert CV", type="pdf")
job = st.text_area("Insert the URL or job description")

if st.button("Analyze"):
    if cv is not None:
        cv_text = extract_text_from_pdf(cv)
        cv_text = clean_text(cv_text)
        job_text = extract_text_from_url(job) if job.startswith("http") else job
        st.write("CV extracted successfully!")
        if job:
            result = analyze_cv(cv_text, job)
            st.write(result)