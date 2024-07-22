import streamlit as st

from src import roc_analysis
from src import SessionState
from src import user_manual
from src import translations


def main():
    session_state = SessionState()

    with st.sidebar:
        st.title(':sparkles: ROCFlow')
        language = st.selectbox("Select Language", ["Русский", "English"])
        session_state.language = language

        add_radio = st.radio(translations[language]['nav'],
                             (translations[language]['ROC_Analyse_btn'],
                              translations[language]['User_Manual_btn']))

        st.link_button(':magic_wand: almanelis',
                       'https://github.com/almanelis/')

    if add_radio == translations[language]['ROC_Analyse_btn']:
        roc_analysis(session_state.language)
    if add_radio == translations[language]['User_Manual_btn']:
        user_manual(session_state.language)


if __name__ == "__main__":
    main()
