import streamlit as st
import datetime
from datetime import date
import pandas as pd
import numpy as np
import altair as alt
import requests
st.set_page_config(layout="wide")
st.title('MOBILI - AGENDAMENTO')

url = "https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/headers_authorization?cliente=3542&nome=operacional&senha=WR3D5K"

payload = {}
headers = {}

session = requests.Session()
response = session.post(url=url, headers=headers, data=payload)
data = response.json()
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
    dados = []
    indice = 0

    while True:
        # Faz uma solicitação GET para buscar um veículo específico
        chave_api = 'c5b79e7ce0c72d6e3c9842a51433c726'
        veiculo_url = f'https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/buscar_veiculo/{chave_api}'
        params = {'indice': str(indice)}
        veiculo_response = session.get(url=veiculo_url, params=params)
        veiculo_data = veiculo_response.json()

        # Se dar algum erro, ou não retonar 200, quebrar o loop pois chegou no fim da lista
        if veiculo_response.status_code != 200 or veiculo_data.get('error') == True or len(veiculo_data.get('data')) == 0:
            break

        # Adicionar dados na lista de dados
        dados.extend(veiculo_data.get('data'))

        # Subir indice, para procurar no proximo indice
        print(f"{indice} {veiculo_response.status_code} {veiculo_data.get('error')} {len(veiculo_data.get('data'))} {len(dados)}")
        indice += 1

        # Exibe os dados no Streamlit
        return dados
    else:
        print('Erro na autenticação. Verifique as credenciais.')
        return dados

def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

dados = load_data(10000)

data_frame = pd.DataFrame.from_dict(dados)

st.subheader('DADOS BRUTOS PARA CONFERÊNCIA')
if st.checkbox('Mostrar dados'):
    st.subheader('Dataframe')
    st.write(dados)
    st.write(data_frame)

