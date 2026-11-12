import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool", page_icon="🌍", layout="centered")

st.title("🌍 Language Translation Tool")
st.write("Translate text between languages in a few simple steps.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
    "Bengali": "bn",
    "Marathi": "mr",
}

col1, col2 = st.columns(2)
with col1:
    source_name = st.selectbox("Translate from", list(languages.keys()), index=0)
with col2:
    target_name = st.selectbox("Translate to", list(languages.keys()), index=1)

text = st.text_area("Enter your text", placeholder="Type something to translate...", height=150)

if st.button("Translate", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text first.")
    elif source_name == target_name:
        st.info("Choose two different languages.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source_name],
                target=languages[target_name]
            ).translate(text)
            st.subheader("Translated text")
            st.text_area("Result", value=translated, height=150)
            st.caption("Translation is provided by an online translation service. Check important translations before using them.")
        except Exception as error:
            st.error("Translation could not be completed. Please check your internet connection and try again.")
