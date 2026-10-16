# 🌐 CodeAlpha Task 1: Language Translation Tool

A clean, responsive, and feature-packed web application for multilingual language translation and voice synthesis built using **Python**, **Streamlit**, **deep-translator**, and **gTTS (Google Text-to-Speech)**.

---

## ✨ Features

- **Multilingual Translation:** Supports over 100 languages via `deep-translator` (GoogleTranslator).
- **Auto-Detection:** Automatically detects the source language of input text or allows manual selection.
- **Two-Column Responsive UI:** Streamlined layout with side-by-side language selectors and dual input/output text areas.
- **Integrated Text-to-Speech (TTS):** Synthesizes natural-sounding spoken audio of translated text with `gTTS` and plays it directly in-app using `st.audio`.
- **Customizable Speech Rate:** Optional slow speech toggle for language learners and pronunciation practice.
- **Word & Character Counters:** Real-time statistics for input text.
- **Export & Download:** Download translated text as `.txt` and speech audio as `.mp3`.
- **Robust Error Handling:** Graceful feedback for network connection drops, unsupported audio languages, or invalid inputs.

---

## 📁 Project Structure

```text
CodeAlpha_LanguageTranslationTool/
│
├── app.py              # Main Streamlit web application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation and guide
```

---

## 🛠️ Prerequisites

- **Python 3.8+** installed on your machine.
- An active internet connection (for online translation and TTS queries).

---

## 📦 Installation Steps

1. **Clone or Navigate to the Project Directory:**
   ```bash
   cd CodeAlpha_LanguageTranslationTool
   ```

2. **(Optional but recommended) Create a Virtual Environment:**
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   Install all required libraries using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run the Application

Launch the Streamlit app with the following command:

```bash
streamlit run app.py
```

The app will open automatically in your default web browser at `http://localhost:8501`.

---

## 📖 How to Use

1. **Choose Source Language:** Leave as `"Auto Detect"` or select your input language from the dropdown.
2. **Choose Target Language:** Select the language into which you want your text translated.
3. **Enter Text:** Type or paste your original text in the input box.
4. **Translate:** Click the **🚀 Translate** button.
5. **Listen & Export:** Listen to the speech pronunciation with the audio player, or download the text/audio files.

---

## 📄 License & Attribution

Developed for **CodeAlpha Internship - Task 1 (Language Translation Tool)**.
Technologies: [Streamlit](https://streamlit.io/) | [deep-translator](https://github.com/nidhaloff/deep-translator) | [gTTS](https://github.com/pndurette/gTTS)
