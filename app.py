import streamlit as st
import pdfplumber, re

from model import analyze_cv, extract_text_from_url, generate_cover_letter
from additional import css, translations

st.set_page_config(
    page_title="AI Career Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(css, unsafe_allow_html=True)

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



t = translations[ui_language]

st.markdown(f"""
<div class="hero">

<h1>{t['title']}</h1>

<p>{t['description']}</p>

</div>
""", unsafe_allow_html=True)

cv = st.file_uploader(t["upload_cv"], type="pdf")

with st.expander(t["add_portfolio"]):
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

job = st.text_area(t["insertjob"])
if st.button(t["analyze"]):
    if cv is not None:
        cv_text = extract_text_from_pdf(cv)
        cv_text = clean_text(cv_text)
        
        portfolio_text = ""
        if portfolio_type == "PDF" and portfolio_pdf is not None:
            portfolio_text = extract_text_from_pdf(portfolio_pdf)
            portfolio_text = clean_text(portfolio_text)
        elif portfolio_type == "URL" and portfolio_url:
            portfolio_text = extract_text_from_url(portfolio_url)
            portfolio_text = clean_text(portfolio_text)

        job_text = extract_text_from_url(job) if job.startswith("http") else job
        st.write(t["success"])

        if job:
            result = analyze_cv(cv_text, job, portfolio_text, analysis_language)
            st.write(result)
            cover_letter = generate_cover_letter(cv_text, job, result, letter_language)
            st.write(t["generated_cover_letter"])
            st.write(cover_letter)