import streamlit as st
import datetime
from datetime import date
import pandas as pd
import numpy as np
import altair as alt
import requests
st.set_page_config(layout="wide")
st.title('MOBILI - AGENDAMENTO')

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

dados = load_data(10000000)

data_frame = pd.DataFrame.from_dict(dados)

data_frame ['DATA/HORA ALTERAÇÃO'] = pd.to_datetime(data_frame['DATA/HORA ALTERAÇÃO']).dt.date
situações = data_frame
situações = situações['SITUAÇÃO'].value_counts().to_frame()
situações_inv = situações.T

# Criar um novo DataFrame para o gráfico de pizza
situações_pizza = pd.DataFrame({'Situação': situações.index, 'Count': situações['count']})


# Plotar o gráfico de pizza usando o novo DataFrame
st.subheader('SITUAÇÕES')
c = alt.Chart(situações_pizza).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Count", type="quantitative"),
    color=alt.Color(field="Situação", type="nominal"),
)
st.dataframe(situações_pizza.T,use_container_width=True ,hide_index=True)
st.altair_chart(c, use_container_width=True)


st.subheader('LISTA DE VEÍCULOS POR SITUAÇÃO')
col1, col2 = st.columns([1, 5])

f_date = date.today()
data_frame['DATA SITUAÇÃO'] = data_frame['DATA/HORA ALTERAÇÃO']
data_frame['NÚMERO DE DIAS'] = (f_date - data_frame['DATA SITUAÇÃO']) / np.timedelta64(1, 'D')
data_frame = data[["NOME", "PLACA", "SITUAÇÃO","DATA SITUAÇÃO", "CIDADE CLIENTE", "ESTADO CLIENTE", "NÚMERO DE DIAS", "OBSERVAÇÃO"]]

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


uf = data_frame['ESTADO CLIENTE'].unique()
make_choice = st.sidebar.selectbox('Select your vehicle:', uf)

remover_filtro = st.sidebar.checkbox("Remover filtros")

if remover_filtro:
    filtered_data = data_frame
else:
    selecao = (data_frame['SITUAÇÃO'] == situação_filtro) & (data_frame['ESTADO CLIENTE'] == make_choice)
    filtered_data = data_frame[selecao]
    
estado = filtered_data['ESTADO CLIENTE'].value_counts().to_frame()
col1.dataframe(data=estado, use_container_width=True, hide_index=False)
col2.dataframe(data=filtered_data, use_container_width=True, hide_index=True)

st.subheader('DADOS BRUTOS PARA CONFERÊNCIA')
if st.checkbox('Mostrar dados'):
    st.subheader('Dataframe')
    st.write(data)


