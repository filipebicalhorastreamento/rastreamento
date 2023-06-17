import streamlit as st
import datetime
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
situações = data['SITUAÇÃO'].value_counts().to_frame()
st.subheader('SITUAÇÕES')
st.write(situações)
st.bar_chart(situações)

st.subheader('LISTA DE VEÍCULOS POR SITUAÇÃO')
col1, col2 = st.columns([1, 5])
data_frame['NÚMERO DE DIAS'] = '0'
data_frame = data[["PLACA", "SITUAÇÃO", "ESTADO CLIENTE", "DATA/HORA ALTERAÇÃO", "NÚMERO DE DIAS"]]
situação_filtro = col1.selectbox(
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

filtered_data = data_frame[data_frame['SITUAÇÃO'] == situação_filtro]
estado = filtered_data['ESTADO CLIENTE'].value_counts().to_frame()
col1.write(estado)
col2.write(filtered_data)
st.subheader('LISTA DE VEÍCULOS POR ESTADO')


st.subheader('DADOS BRUTOS PARA CONFERÊNCIA')
if st.checkbox('Mostrar dados'):
    st.subheader('Dataframe')
    st.write(data)
