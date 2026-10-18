# Language Translation Tool

An interactive web application built with Python and Streamlit for translating text across 100+ global languages with integrated Text-to-Speech voice synthesis and 1-click text copying[cite: 1, 13]. Developed as part of the CodeAlpha Artificial Intelligence Internship[cite: 1].

## Features
- **Auto & Manual Language Selection**: Supports automatic language detection as well as manual source and target language picking across 100+ languages[cite: 1, 13].
- **Accurate Real-Time Translation**: Powered by the Google Translate API via `googletrans` for natural translations[cite: 1, 13].
- **Text-to-Speech (TTS)**: Synthesizes output speech audio on demand using Google Text-to-Speech (`gTTS`)[cite: 1, 13].
- **1-Click Copy**: Output container allows users to copy translated text instantly[cite: 13].
- **Responsive Web UI**: Modern, clean side-by-side layout created with Streamlit[cite: 1, 13].

## Tech Stack
- **Language**: Python
- **Frontend UI**: Streamlit
- **Translation Engine**: `googletrans` (4.0.0-rc1)[cite: 1]
- **Audio Engine**: `gTTS` (Google Text-to-Speech)[cite: 1]

## Repository Structure
```text
CodeAlpha_LanguageTranslationTool/
│── app.py             # Main Streamlit application logic
│── requirements.txt   # Required Python packages
└── README.md          # Project documentation

Setup & Installation:

1.Clone the repository:
Bash
git clone [https://github.com/allurineraj/CodeAlpha_LanguageTranslationTool.git](https://github.com/allurineraj/CodeAlpha_LanguageTranslationTool.git)
cd CodeAlpha_LanguageTranslationTool

2.Set up a virtual environment (optional but recommended):
Bash
python -m venv venv
.\venv\Scripts\Activate.ps1

3.Install dependencies:
Bash
pip install -r requirements.txt

4.Run the application:
Bash
streamlit run app.py

5.Access the app in your browser at http://localhost:8501.
