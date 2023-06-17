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

st.subheader('SITUAÇÕES')
tab2, tab1 = st.tabs(["📈 Chart", "🗃 Data"])
situações = data_frame['SITUAÇÃO'].value_counts().to_frame()

situações_invertido = situações.T
tab1.subheader("A tab with the data")
tab1.write(situações_invertido)
tab2.subheader("A tab with a chart")
tab2.bar_chart(situações)

st.subheader('LISTA DE VEÍCULOS POR SITUAÇÃO')
col1, col2 = st.columns([1, 5])
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
col2.write(filtered_data)


st.subheader('DADOS BRUTOS PARA CONFERÊNCIA')
if st.checkbox('Mostrar dados'):
    st.subheader('Dataframe')
    st.write(data)
