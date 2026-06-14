css = """
<style>

.stApp {
    background:
    radial-gradient(circle at top left, #0f172a, #020617);
}

/* MAIN WIDTH */

.block-container {
    padding-top: 4rem;
    padding-left: 4rem;
    padding-right: 4rem;
    max-width: 1400px;
}

.hero {
    padding: 2rem;
    border-radius: 24px;

    background:
    linear-gradient(
        135deg,
        rgba(59,130,246,0.15),
        rgba(139,92,246,0.15)
    );

    border: 1px solid rgba(255,255,255,0.08);

    margin-bottom: 2rem;
}

.hero h1 {
    font-size: 64px;
    font-weight: 800;
    margin-bottom: 0.5rem;
}

.hero p {
    font-size: 20px;
    color: #cbd5e1;
}

/* CARDS */

.card {
    background: rgba(15,23,42,0.75);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 1.5rem;

    backdrop-filter: blur(10px);

    margin-bottom: 1rem;
}

/* BUTTON */

.stButton > button {

    width: 100%;

    background:
    linear-gradient(
        135deg,
        #3b82f6,
        #8b5cf6
    );

    color: white;

    border: none;

    border-radius: 16px;

    padding: 0.85rem;

    font-size: 18px;

    font-weight: 700;

    transition: 0.3s;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
    0 10px 30px rgba(59,130,246,0.35);
}

/* INPUTS */

.stTextArea textarea,
.stTextInput input {

    background-color: rgba(15,23,42,0.8);

    border-radius: 16px;

    border: 1px solid rgba(255,255,255,0.08);

    color: white;
}

/* FILE UPLOADER */

[data-testid="stFileUploader"] {

    background: rgba(15,23,42,0.8);

    border-radius: 20px;

    border: 1px dashed rgba(255,255,255,0.15);

    padding: 1rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #111827,
        #0f172a
    );

    border-right:
    1px solid rgba(255,255,255,0.08);
}

</style>
"""

translations = {
    "English": {
        "title": "AI CV Assistant",
        "description": "Analyze CVs, optimize job applications, generate cover letters and evaluate portfolios using AI.",
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
        "description": "Аналізуйте CV, оптимізуйте подачі на роботу, генеруйте супровідні листи та оцінюйте портфоліо за допомогою ШІ.",
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
        "description": "Analizuj CV, optymalizuj aplikacje do pracy, generuj listy motivacyjne i oceniaj portfola za pomocą AI.",
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