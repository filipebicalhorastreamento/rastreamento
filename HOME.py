import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="MOBILI - RASTREAMENTO",
        layout="wide",
    )

    st.markdown(
        """
        PROCEDIMENTO OPERACIONAL PADRÃO
        LINKS ÚTEIS:  
        SAFECAR - https://www.safecar.net.br/associacoes/
        """
    )


if __name__ == "__main__":
    run()
