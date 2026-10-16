"""
CodeAlpha Task 1: Language Translation Tool
Built with Streamlit, deep-translator (GoogleTranslator), and gTTS
"""

import io
import streamlit as st
from deep_translator import GoogleTranslator, MyMemoryTranslator
from gtts import gTTS

# Curated fallback dictionary of supported languages
FALLBACK_LANGUAGES = {
    "afrikaans": "af", "albanian": "sq", "amharic": "am", "arabic": "ar", "armenian": "hy",
    "azerbaijani": "az", "basque": "eu", "belarusian": "be", "bengali": "bn", "bosnian": "bs",
    "bulgarian": "bg", "catalan": "ca", "cebuano": "ceb", "chichewa": "ny", "chinese (simplified)": "zh-CN",
    "chinese (traditional)": "zh-TW", "corsican": "co", "croatian": "hr", "czech": "cs", "danish": "da",
    "dutch": "nl", "english": "en", "esperanto": "eo", "estonian": "et", "filipino": "tl",
    "finnish": "fi", "french": "fr", "frisian": "fy", "galician": "gl", "georgian": "ka",
    "german": "de", "greek": "el", "gujarati": "gu", "haitian creole": "ht", "hausa": "ha",
    "hawaiian": "haw", "hebrew": "iw", "hindi": "hi", "hmong": "hmn", "hungarian": "hu",
    "icelandic": "is", "igbo": "ig", "indonesian": "id", "irish": "ga", "italian": "it",
    "japanese": "ja", "javanese": "jw", "kannada": "kn", "kazakh": "kk", "khmer": "km",
    "korean": "ko", "kurdish (kurmanji)": "ku", "kyrgyz": "ky", "lao": "lo", "latin": "la",
    "latvian": "lv", "lithuanian": "lt", "luxembourgish": "lb", "macedonian": "mk", "malagasy": "mg",
    "malay": "ms", "malayalam": "ml", "maltese": "mt", "maori": "mi", "marathi": "mr",
    "mongolian": "mn", "myanmar (burmese)": "my", "nepali": "ne", "norwegian": "no", "odia": "or",
    "pashto": "ps", "persian": "fa", "polish": "pl", "portuguese": "pt", "punjabi": "pa",
    "romanian": "ro", "russian": "ru", "samoan": "sm", "scots gaelic": "gd", "serbian": "sr",
    "sesotho": "st", "shona": "sn", "sindhi": "sd", "sinhala": "si", "slovak": "sk",
    "slovenian": "sl", "somali": "so", "spanish": "es", "sundanese": "su", "swahili": "sw",
    "swedish": "sv", "tajik": "tg", "tamil": "ta", "telugu": "te", "thai": "th",
    "turkish": "tr", "ukrainian": "uk", "urdu": "ur", "uyghur": "ug", "uzbek": "uz",
    "vietnamese": "vi", "welsh": "cy", "xhosa": "xh", "yiddish": "yi", "yoruba": "yo", "zulu": "zu"
}


@st.cache_data(show_spinner=False)
def load_languages():
    """Retrieve supported language catalog from deep-translator with offline fallback."""
    try:
        supported = GoogleTranslator().get_supported_languages(as_dict=True)
        if isinstance(supported, dict) and len(supported) > 0:
            return supported
    except Exception:
        pass
    return FALLBACK_LANGUAGES


def execute_translation(text: str, source_label: str, target_label: str) -> str:
    """
    Executes translation using deep-translator (GoogleTranslator),
    with intelligent fallback handling if Google rate-limits requests.
    """
    langs = load_languages()
    s_code = "auto" if source_label == "Auto Detect" else langs.get(source_label.lower(), "auto")
    t_code = langs.get(target_label.lower(), "es")

    # Primary translation method: deep-translator GoogleTranslator
    try:
        translator = GoogleTranslator(source=s_code, target=t_code)
        result = translator.translate(text)
        if result:
            return result
    except Exception as primary_exc:
        # Fallback to MyMemoryTranslator (also part of deep-translator) if rate-limited
        try:
            source_for_mm = "english" if source_label.lower() in ["auto detect", "auto"] else source_label.lower()
            target_for_mm = target_label.lower()
            mm_translator = MyMemoryTranslator(source=source_for_mm, target=target_for_mm)
            fallback_res = mm_translator.translate(text)
            if fallback_res and not fallback_res.startswith("'AUTO' IS AN INVALID"):
                try:
                    st.info("ℹ️ Translated via secondary translation provider due to high Google API traffic.")
                except Exception:
                    pass
                return fallback_res
        except Exception:
            pass
        # If both fail, raise the original error for transparent feedback
        raise primary_exc

    return ""


def main():
    # Configure Streamlit page
    st.set_page_config(
        page_title="Language Translation Tool | CodeAlpha",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for enhanced modern UI aesthetics
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        .hero-banner {
            background: linear-gradient(135deg, #4338ca 0%, #6366f1 50%, #a855f7 100%);
            padding: 2.2rem 2.5rem;
            border-radius: 18px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 12px 30px -8px rgba(79, 70, 229, 0.35);
            border: 1px solid rgba(255, 255, 255, 0.15);
        }
        .hero-banner h1 {
            color: white !important;
            font-size: 2.3rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.5rem !important;
            letter-spacing: -0.02em;
        }
        .hero-banner p {
            color: rgba(255, 255, 255, 0.9) !important;
            font-size: 1.05rem !important;
            margin: 0 !important;
            line-height: 1.5;
        }

        .output-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.25rem 1.5rem;
            min-height: 220px;
            font-size: 1.05rem;
            line-height: 1.7;
            color: #0f172a;
            white-space: pre-wrap;
            word-break: break-word;
            box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.02);
        }

        @media (prefers-color-scheme: dark) {
            .output-card {
                background: #1e293b;
                border-color: #334155;
                color: #f1f5f9;
            }
        }

        .section-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.3rem 0.85rem;
            font-size: 0.82rem;
            font-weight: 600;
            border-radius: 9999px;
            background-color: #ede9fe;
            color: #5b21b6;
            margin-bottom: 0.6rem;
        }
        .stat-bar {
            display: flex;
            gap: 1.2rem;
            font-size: 0.85rem;
            color: #64748b;
            margin-top: 0.4rem;
            margin-bottom: 0.8rem;
        }

        div.stButton > button:first-child {
            border-radius: 10px;
            font-weight: 600;
            transition: all 0.2s ease;
        }
    </style>
    """, unsafe_allow_html=True)

    languages_dict = load_languages()
    display_languages = sorted([name.title() for name in languages_dict.keys()])

    # Header Banner
    st.markdown("""
    <div class="hero-banner">
        <h1>🌐 Multilingual Translation & Speech Studio</h1>
        <p>Translate text seamlessly across 100+ languages with automated detection and instant text-to-speech voice synthesis.</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar with app documentation & preferences
    with st.sidebar:
        st.markdown("### 🛠️ Configuration & Info")
        st.info(
            "**Task 1: Language Translation Tool**\n\n"
            "Internship Project by **CodeAlpha**\n\n"
            "• Core Engine: `deep-translator` (GoogleTranslator)\n"
            "• Audio Engine: `gTTS` (Google Text-to-Speech)\n"
            "• Interface: `Streamlit`"
        )
        st.divider()
        tts_speed_slow = st.checkbox(
            "🐢 Slow Speech Audio",
            value=False,
            help="Slow down speech pronunciation (ideal for language study)."
        )
        st.caption("Tip: Leave source language on 'Auto Detect' for instant recognition.")

    # Top Selection Columns: Source Language & Target Language
    col_lang_source, col_lang_target = st.columns(2)

    with col_lang_source:
        source_options = ["Auto Detect"] + display_languages
        selected_source = st.selectbox(
            "Source Language",
            options=source_options,
            index=0,
            help="Select the source language or keep 'Auto Detect' to identify automatically."
        )

    with col_lang_target:
        default_target_idx = display_languages.index("Spanish") if "Spanish" in display_languages else 0
        selected_target = st.selectbox(
            "Target Language",
            options=display_languages,
            index=default_target_idx,
            help="Select the target language for the translation."
        )

    # Dual-column Work Area: Input Text & Translated Output
    col_input, col_output = st.columns(2)

    with col_input:
        st.markdown('<div class="section-pill">📝 Original Input</div>', unsafe_allow_html=True)
        input_text = st.text_area(
            label="Input Text Area",
            placeholder="Enter or paste text here to translate...",
            height=220,
            label_visibility="collapsed"
        )

        chars = len(input_text)
        words = len(input_text.split()) if input_text.strip() else 0
        st.markdown(
            f'<div class="stat-bar"><span>Characters: <b>{chars}</b></span><span>Words: <b>{words}</b></span></div>',
            unsafe_allow_html=True
        )

        btn_col1, btn_col2 = st.columns([1.2, 1])
        with btn_col1:
            translate_btn = st.button("🚀 Translate", type="primary", use_container_width=True)
        with btn_col2:
            clear_btn = st.button("🗑️ Clear", use_container_width=True)
            if clear_btn:
                st.session_state.pop("translation_output", None)
                st.session_state.pop("tts_audio_data", None)
                st.rerun()

    if "translation_output" not in st.session_state:
        st.session_state["translation_output"] = ""
    if "tts_audio_data" not in st.session_state:
        st.session_state["tts_audio_data"] = None

    if translate_btn:
        clean_text = input_text.strip() if input_text else ""
        if not clean_text:
            st.warning("⚠️ Please provide text in the input box before translating.")
        else:
            with st.spinner("Translating text..."):
                try:
                    translated_str = execute_translation(clean_text, selected_source, selected_target)
                    if translated_str:
                        st.session_state["translation_output"] = translated_str

                        # Synthesize speech using gTTS
                        target_code = languages_dict.get(selected_target.lower(), "es")
                        lang_for_gtts = target_code.split("-")[0] if ("-" in target_code and target_code not in ["zh-CN", "zh-TW"]) else target_code

                        try:
                            tts = gTTS(text=translated_str, lang=lang_for_gtts, slow=tts_speed_slow)
                            audio_buffer = io.BytesIO()
                            tts.write_to_fp(audio_buffer)
                            audio_buffer.seek(0)
                            st.session_state["tts_audio_data"] = audio_buffer.read()
                        except Exception as tts_err:
                            st.session_state["tts_audio_data"] = None
                            st.caption(f"Note: Voice synthesis is currently unavailable for code '{target_code}' ({tts_err}).")
                    else:
                        st.error("Translation returned an empty result. Please revise the input text.")
                except Exception as err:
                    st.error(f"❌ Translation failed: {err}")
                    st.info("Tip: Check your network connection or try choosing specific source/target languages.")

    with col_output:
        st.markdown('<div class="section-pill">🎯 Translated Output</div>', unsafe_allow_html=True)

        if st.session_state["translation_output"]:
            st.markdown(
                f'<div class="output-card">{st.session_state["translation_output"]}</div>',
                unsafe_allow_html=True
            )

            if st.session_state["tts_audio_data"]:
                st.markdown("##### 🔊 Audio Pronunciation")
                st.audio(st.session_state["tts_audio_data"], format="audio/mp3")

            st.divider()
            dl1, dl2 = st.columns(2)
            with dl1:
                st.download_button(
                    label="📄 Download Text (.txt)",
                    data=st.session_state["translation_output"],
                    file_name=f"translation_{selected_target.lower()}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            with dl2:
                if st.session_state["tts_audio_data"]:
                    st.download_button(
                        label="🎧 Download Audio (.mp3)",
                        data=st.session_state["tts_audio_data"],
                        file_name=f"speech_{selected_target.lower()}.mp3",
                        mime="audio/mp3",
                        use_container_width=True
                    )
        else:
            st.markdown(
                '<div class="output-card" style="color: #94a3b8; font-style: italic;">The translated text and speech player will be displayed here once you click "Translate".</div>',
                unsafe_allow_html=True
            )


if __name__ == "__main__":
    main()
