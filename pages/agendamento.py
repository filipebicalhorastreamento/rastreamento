import streamlit as st
import datetime
from datetime import date
import pandas as pd
import numpy as np
import altair as alt
import requests
st.set_page_config(layout="wide")
st.title('MOBILI - AGENDAMENTO')

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

@st.cache_data
def load_data(nrows):

    url = "https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/headers_authorization?cliente=3542&nome=operacional&senha=WR3D5K"

    payload = {}
    headers = {}

    session = requests.Session()
    response = session.post(url=url, headers=headers, data=payload)
    data = response.json()

    # Verifica se a autenticação foi bem-sucedida
    if response.status_code == 200 and data.get('error') == False:
        # Faz uma solicitação GET para buscar um veículo específico
        chave_api = 'c5b79e7ce0c72d6e3c9842a51433c726'
        veiculo_url = f'https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/buscar_veiculo/{chave_api}'
        veiculo_response = session.get(url=veiculo_url)
        data = veiculo_response.json()

        # Exibe os dados no Streamlit
        return data
    else:
        print('Erro na autenticação. Verifique as credenciais.')
        return data

def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

data = load_data(10000)

data_frame = pd.DataFrame.from_dict(data)

st.subheader('DADOS BRUTOS PARA CONFERÊNCIA')
if st.checkbox('Mostrar dados'):
    st.subheader('Dataframe')
    st.write(data)
    st.write(data_frame)

