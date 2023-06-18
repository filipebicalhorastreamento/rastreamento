import streamlit as st
import datetime
from datetime import date
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.title('MOBILI - RASTREAMENTO')

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

@st.cache_data
def load_data(nrows):
    data = load_data2(st.secrets["public_gsheets_url"])
    uppercase = lambda x: str(x).upper()
    data.rename(uppercase, axis='columns', inplace=True)
    return data

def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

data = load_data(10000)
data_frame = data
data_frame ['DATA/HORA ALTERAÇÃO'] = pd.to_datetime(data_frame['DATA/HORA ALTERAÇÃO']).dt.date
situações = data_frame['SITUAÇÃO'].value_counts().to_frame()

situações_inv = situações.T

st.subheader('SITUAÇÕES')
tab1, tab2 = st.tabs(["📈 Gráfico", "🗃 Números"])
tab1.bar_chart(data=situações, y="count", use_container_width=True)
tab2.dataframe(situações_inv,use_container_width=True ,hide_index=True)

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
