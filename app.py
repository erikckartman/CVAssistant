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

with st.sidebar:

    st.title("Settings")

    ui_language = st.selectbox(
        "Interface Language",
        ["English", "Українська", "Polski"]
    )

    analysis_language = st.selectbox(
        "Analysis Language",
        ["English", "Українська", "Polski"]
    )

    letter_language = st.selectbox(
        "Cover Letter Language",
        ["English", "Українська", "Polski"]
    )

translations = {
    "English": {
        "title": "AI CV Assistant",
        "upload_cv": "Upload CV",
        "portfoliotype": "Portfolio Type",
        "insertjob": "Insert the URL or job description",
        "insertpdf": "Insert Portfolio PDF",
        "inserturl": "Insert Portfolio URL",
        "analyze": "Analyze",
        "success": "CV extracted successfully!",
        "generated_cover_letter": "Generated Cover Letter:",
        "add_portfolio": "Add Portfolio"
    },

    "Українська": {
        "title": "AI Помічник для CV",
        "upload_cv": "Завантаж CV",
        "portfoliotype": "Тип портфоліо",
        "insertjob": "Вставте URL або опис вакансії",
        "insertpdf": "Вставте PDF портфоліо",
        "inserturl": "Вставте URL портфоліо",
        "analyze": "Проаналізувати",
        "success": "CV успішно отримано!",
        "generated_cover_letter": "Згенерований супровідний лист:",
        "add_portfolio": "Додайте портфоліо"
    },

    "Polski": {
        "title": "Asystent AI do CV",
        "upload_cv": "Wgraj CV",
        "portfoliotype": "Typ portfola",
        "insertjob": "Wstaw URL lub opis stanowiska",
        "insertpdf": "Wstaw PDF portfola",
        "inserturl": "Wstaw URL portfola",
        "analyze": "Analizuj",
        "success": "CV został pomyślnie wyodrębniony!",
        "generated_cover_letter": "Wygenerowany list motivacyjny:",
        "add_portfolio": "Dodaj portfolo"
    }
}

t = translations[ui_language]

st.title(t["title"])

cv = st.file_uploader(t["upload_cv"], type="pdf")
add_portfolio = st.checkbox(t["add_portfolio"])
job = st.text_area(t["insertjob"])
if add_portfolio:
    portfolio_type = st.radio(
        t["portfoliotype"],
        ["PDF", "URL"]
    )

    if portfolio_type == "PDF":
        portfolio_pdf = st.file_uploader(
        t["insertpdf"],
        type=["pdf"]
    )
    elif portfolio_type == "URL":
        portfolio_url = st.text_input(t["inserturl"])
if st.button(t["analyze"]):
    if cv is not None:
        cv_text = extract_text_from_pdf(cv)
        cv_text = clean_text(cv_text)
        portfoliotext = extract_text_from_pdf(portfolio_pdf) if add_portfolio and portfolio_type == "PDF" else extract_text_from_url(portfolio_url) if add_portfolio and portfolio_type == "URL" else ""
        job_text = extract_text_from_url(job) if job.startswith("http") else job
        st.write(t["success"])
        if job:
            result = analyze_cv(cv_text, job, portfoliotext, analysis_language)
            st.write(result)
            cover_letter = generate_cover_letter(cv_text, job, result, letter_language)
            st.write(t["generated_cover_letter"])
            st.write(cover_letter)