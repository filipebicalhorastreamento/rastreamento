import streamlit as st
import pandas as pd
import requests
import altair as alt
import datetime
from datetime import date
import numpy as np

st.set_page_config(layout="wide")
st.title('RETIRADAS PENDENTES')

chave_api = 'c5b79e7ce0c72d6e3c9842a51433c726'

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
            indice += 200

        # Exibe os dados no Streamlit
        return dados
    else:
        print('Erro na autenticação. Verifique as credenciais.')
    return dados

def load_sheets(nrows):
    datasheets = load_data2(st.secrets["public_gsheets_url2"])
    uppercase = lambda x: str(x).upper()
    datasheets.rename(uppercase, axis='columns', inplace=True)
    return datasheets

def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

dadossheets = load_sheets(10000000)
dados = load_data(10000000)
dfagendamentos = pd.DataFrame.from_dict(dadossheets)
dfinstalacoes = pd.DataFrame.from_dict(dados)
nova_ordem = dfinstalacoes[["placa_veiculo", "nome_cliente","situacao_veiculo","modelo_veiculo","cidade_veiculo","uf_veiculo","ultima_atualizacao"]]
dfinstalacoes = nova_ordem
filtro = (dfinstalacoes['situacao_veiculo'] == 'RETIRADA')
filtered_data = dfinstalacoes[filtro]

Status = filtered_data['uf_veiculo'].value_counts().to_frame()
DFStatus = pd.DataFrame({'Status': Status.index, 'Qntd': Status['count']})

c = alt.Chart(DFStatus).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Qntd", type="quantitative"),
    color=alt.Color(field="Status", type="nominal"),
)

st.dataframe(data=Status.T, use_container_width=True, hide_index=True)
col1, col2 = st.columns([2, 5])
col1.altair_chart(c, use_container_width=True)
col2.dataframe(data=filtered_data, use_container_width=True, hide_index=True)

col3, col4 = st.columns([2, 5])

st.dataframe(data=dfagendamentos, use_container_width=True, hide_index=True)


