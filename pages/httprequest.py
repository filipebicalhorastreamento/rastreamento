import streamlit as st
import pandas as pd
import requests
import altair as alt
import datetime
from datetime import date
import numpy as np

st.set_page_config(layout="wide")
st.title('MOBILI - VEÍCULOS POR SITUAÇÃO')

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
    
@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')



dados = load_data(10000000)
df = pd.DataFrame.from_dict(dados)
csv = convert_df(df)
situações = df['situacao_veiculo'].value_counts().to_frame()
situações_pizza = pd.DataFrame({'Situação': situações.index, 'Count': situações['count']})
df ['ultima_atualizacao'] = pd.to_datetime(df['ultima_atualizacao']).dt.date


st.subheader('SITUAÇÕES')
c = alt.Chart(situações_pizza).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Count", type="quantitative"),
    color=alt.Color(field="Situação", type="nominal"),
)
st.dataframe(situações.T,use_container_width=True ,hide_index=True)
st.altair_chart(c, use_container_width=True)

st.subheader('LISTA DE VEÍCULOS POR SITUAÇÃO')
col1, col2 = st.columns([1, 5])

situação_filtro = st.sidebar.selectbox(
    "Situação",
    ('AGENDADO',
    'ATIVO',
    'INATIVO',
    'MANUTENÇÃO',
    'MUZZI',
    'PENDENTE',
    'PENDENTE INSTALAÇÃO',
    'PROPRIO',
    'RECUSADO',
    'RETIRADA',
    'SAFECAR'))

uf = df['uf_veiculo'].unique()

df['DATA SITUAÇÃO'] = df['ultima_atualizacao']

f_date = date.today()
df['NÚMERO DE DIAS'] = (f_date - df['DATA SITUAÇÃO']) / np.timedelta64(1, 'D')
data_frame = df[["nome_cliente", "placa_veiculo", "situacao_veiculo","cidade_veiculo","uf_veiculo","ultima_atualizacao", "NÚMERO DE DIAS"]]
remover_filtro = st.sidebar.checkbox("Remover filtros")

if remover_filtro:
    filtered_data = data_frame
else:
    selecao = (data_frame['situacao_veiculo'] == situação_filtro) #& (df['uf_veiculo'] == make_choice)
    filtered_data = data_frame[selecao]
    
make_choice = st.sidebar.selectbox('Selecione um estado:', uf)
estado = filtered_data['uf_veiculo'].value_counts().to_frame()
dfsituacao = filtered_data
col1.dataframe(data=estado, use_container_width=True, hide_index=False)
col2.dataframe(data=filtered_data, use_container_width=True, hide_index=True)
st.download_button(
    "Press to Download",
    csv,
    "browser_visits.csv",
    "text/csv",
    key='browser-data'
)

st.dataframe(df)
