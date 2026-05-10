import streamlit as st
import pdfplumber, re

from model import analyze_cv, extract_text_from_url, generate_cover_letter

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
add_portfolio = st.checkbox("Add Portfolio")
job = st.text_area("Insert the URL or job description")

if add_portfolio:
    portfolio_type = st.radio(
        "Portfolio Type",
        ["PDF", "URL"]
    )

    if portfolio_type == "PDF":
        portfolio_pdf = st.file_uploader(
        "Upload Portfolio PDF",
        type=["pdf"]
    )
    elif portfolio_type == "URL":
        portfolio_url = st.text_input("Insert Portfolio URL")

if st.button("Analyze"):
    if cv is not None:
        cv_text = extract_text_from_pdf(cv)
        cv_text = clean_text(cv_text)
        portfoliotext = extract_text_from_pdf(portfolio_pdf) if add_portfolio and portfolio_type == "PDF" else extract_text_from_url(portfolio_url) if add_portfolio and portfolio_type == "URL" else ""
        job_text = extract_text_from_url(job) if job.startswith("http") else job
        st.write("CV extracted successfully!")
        if job:
            result = analyze_cv(cv_text, job, portfoliotext)
            st.write(result)
            cover_letter = generate_cover_letter(cv_text, job, result)
            st.write("Generated Cover Letter:")
            st.write(cover_letter)