from transformers import pipeline
import streamlit as st

st.set_page_config(
    page_title="Translator",
    page_icon=":robot:",
    layout="wide"
)

st.header("🇫🇷🇪🇸 Translator 🇺🇸🇨🇳")

col1, col2 = st.columns([1, 1])

with col1:
    option_llm = st.selectbox(
        "Model",
        (
            "Helsinki-NLP/opus-mt-fr-en",
            "Helsinki-NLP/opus-mt-en-fr",
            "Helsinki-NLP/opus-mt-es-en",
            "Helsinki-NLP/opus-mt-en-es",
            "Helsinki-NLP/opus-mt-it-en",
            "Helsinki-NLP/opus-mt-en-it",
            "Helsinki-NLP/opus-mt-en-de",
            "Helsinki-NLP/opus-mt-de-en",
        )
    )


def get_query():
    input_text = st.text_area(
        label="Your input text",
        placeholder="Say anything",
        key="question_text"
    )
    return input_text


query = get_query()

if query and len(query) > 1:
    output = ""
    try:
        with st.spinner(text="In progress..."):
            translator = pipeline("translation", model=option_llm)
            output = translator(query)[0]['translation_text']
    except Exception as e:
        output = f"Sorry: cannot translate! {e}"

    height = min(2 * len(output), 240)
    st.text_area(
        label="Response",
        value=output,
        height=height
    )
