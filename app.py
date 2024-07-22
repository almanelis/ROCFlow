import streamlit as st

from src import roc_analysis
from src import SessionState
from src import user_manual


def main():
    session_state = SessionState()

    with st.sidebar:
        st.title('ROCFlow')
        add_radio = st.radio('Навигация',
                             ('ROC Анализ', 'Руководство пользователя'))
        language = st.selectbox("Select Language", ["Русский", "English"])
        session_state.language = language
        st.link_button('almanelis', 'https://github.com/almanelis/')

    if add_radio == 'ROC Анализ':
        roc_analysis(session_state.language)
    if add_radio == 'Руководство пользователя':
        user_manual(session_state.language)


if __name__ == "__main__":
    main()
