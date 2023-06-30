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
        BI - https://app.powerbi.com/view?r=eyJrIjoiNTljM2U2MTMtZTNiOS00OGI3LWJhMTgtYmQ2NTIyOTQ4MWU4IiwidCI6IjE2MGU1NmZkLTFiOWYtNDNkOS1iOWI2LTk0NWEwYjQxM2ZmMiJ9  
        SGR - https://sgr.hinova.com.br/sgr/sgrv2/#/access/signin  
        SAFECAR - https://www.safecar.net.br/associacoes/  
          
        PLATAFORMAS:  
          
        GETRAK - https://sistema.getrak.com/mobili/msumario/index  
        SOFTRUCK - https://app.softruck.com/  
        LÓGICA - https://mobili.logicasolucoes.com.br/  

        CHIPS:  
          
        GETRAK - https://getrak.saitro.com/sistema/login/  
        ALLMANAGER - http://allmanager.com.br/  
        HINOVA - https://arya.hinovaconecta.com.br/  
        SOFTRUCK - 
        
        """
    )


if __name__ == "__main__":
    run()
