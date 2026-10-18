import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import io

st.set_page_config(
    page_title="Multilingual Translation Studio",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Multilingual Translation Studio")
st.write("Translate text accurately across 100+ global languages with voice playback and copy support.")

# format display labels in title case
lang_map = {name.title(): code for code, name in LANGUAGES.items()}
display_langs = sorted(list(lang_map.keys()))

# sidebar configuration
with st.sidebar:
    st.header("🛠️ Configuration & Info")
    st.info("Task 1: Language Translation Tool\n\nInternship Project by CodeAlpha")

# layout controls
col1, col2 = st.columns(2)

with col1:
    src_selection = st.selectbox("Source Language", ["Auto Detect"] + display_langs, index=0)

with col2:
    default_target_idx = display_langs.index("Telugu") if "Telugu" in display_langs else 0
    tgt_selection = st.selectbox("Target Language", display_langs, index=default_target_idx)

# input and output interface
input_col, output_col = st.columns(2)

with input_col:
    st.markdown("### 📝 Original Input")
    user_text = st.text_area(
        label="Input Text",
        height=200,
        placeholder="Type or paste text to translate...",
        label_visibility="collapsed"
    )

with output_col:
    st.markdown("### 🎯 Translated Output")
    output_container = st.empty()
    audio_container = st.empty()

# action button execution
if st.button("🚀 Translate", type="primary", use_container_width=True):
    if not user_text.strip():
        st.warning("Please enter text before translating.")
    else:
        try:
            translator = Translator()
            
            tgt_code = lang_map[tgt_selection]
            src_code = 'auto' if src_selection == "Auto Detect" else lang_map[src_selection]

            # translate input raw text
            res = translator.translate(user_text, src=src_code, dest=tgt_code)

            # display translated text inside interactive code block (provides native 1-click copy button)
            output_container.code(res.text, language=None)
            st.success("Translation completed successfully!")

            # optional text-to-speech voice playback
            try:
                tts = gTTS(text=res.text, lang=tgt_code)
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)

                with audio_container:
                    st.markdown("#### 🔊 Audio Pronunciation")
                    st.audio(fp, format="audio/mp3")
            except Exception:
                pass

        except Exception as err:
            st.error(f"Translation failed: {err}")