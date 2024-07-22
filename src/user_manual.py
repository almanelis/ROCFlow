import streamlit as st

from .LEXICON import translations


def user_manual(lang):
    st.title(translations[lang]['user_manual_title'])
    st.write(translations[lang]['user_manual_text'])
