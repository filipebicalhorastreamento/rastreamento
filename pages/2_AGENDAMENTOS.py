import streamlit as st
import pandas as pd
import requests
import altair as alt
import datetime
from datetime import date
import numpy as np

st.set_page_config(layout="wide")
st.title('AGENDAMENTOS')

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
            chave_api = 'c5b79e7ce0c72d6e3c9842a51433c726'
            veiculo_url = f'https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/buscar_agendamento/{chave_api}'
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

dados = load_data(10000000)
df = pd.DataFrame.from_dict(dados)
f_date = date.today()

col1, col2, col3, col4 = st.columns([1, 4, 1, 4])
uf = df['uf'].value_counts().to_frame()
servico = df['servico'].value_counts().to_frame()
df_uf = pd.DataFrame({'Situação': uf.index, 'Nº': uf['count']})
df_servico = pd.DataFrame({'Serviço': servico.index, 'Nº': servico['count']})

c = alt.Chart(df_uf).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Nº", type="quantitative"),
    color=alt.Color(field="Situação", type="nominal"),
)
c2 = alt.Chart(df_servico).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Nº", type="quantitative"),
    color=alt.Color(field="Serviço", type="nominal"),
)

col1.subheader('Por Estado')
col1.dataframe(df_uf,use_container_width=True ,hide_index=True)
col2.altair_chart(c, use_container_width=True)
col1.subheader('Por Serviço')
col3.dataframe(servico,use_container_width=True ,hide_index=True)
col4.altair_chart(c2, use_container_width=True)


st.subheader('LISTA DE AGENDAMENTOS')
nova_ordem = ['servico', 'contratante', 'placa', 'situacao', 'tecnico', 'telefone', 'data_inicial', 'cidade', 'uf']
agendamento = df[nova_ordem]
st.dataframe(data=agendamento, use_container_width=True, hide_index=True)
