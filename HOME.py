import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="MOBILI - RASTREAMENTO",
        layout="wide",
    )
    st.title('PROCEDIMENTO OPERACIONAL PADRÃO')
    st.markdown(
        """
        LINKS ÚTEIS:  
        SGR - https://sgr.hinova.com.br/sgr/sgrv2/#/access/signin
        SAFECAR - https://www.safecar.net.br/associacoes/  
          
        PLATAFORMAS:  
          
        GETRAK - https://sistema.getrak.com/mobili/msumario/index  
        SOFTRUCK - https://app.softruck.com/  
        LÓGICA - https://mobili.logicasolucoes.com.br/
        
        """
    )


if __name__ == "__main__":
    run()
