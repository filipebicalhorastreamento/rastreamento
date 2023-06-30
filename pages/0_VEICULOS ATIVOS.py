import streamlit as st
import datetime
from datetime import date
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(layout="wide")
st.title('VEÍCULOS ATIVOS')
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

@st.cache_data
def load_data(nrows):
    veiculos_ativos = load_data2(st.secrets["veiculos_ativos"])
    uppercase = lambda x: str(x).upper()
    veiculos_ativos.rename(uppercase, axis='columns', inplace=True)
    logica_monitoramento = load_data2(st.secrets["getrak_plataforma"])
    logica_monitoramento.rename(uppercase, axis='columns', inplace=True)
    return veiculos_ativos, logica_monitoramento

def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

veiculos_ativos, logica_monitoramento = load_data(10000000)

dfveiculosativos =pd.DataFrame.from_dict(veiculos_ativos)
dflogica = pd.DataFrame.from_dict(logica_monitoramento)

st.subheader('ATIVOS SGR')
st.dataframe(data=dfveiculosativos, use_container_width=True, hide_index=True)
st.subheader('LOGICA')
st.dataframe(data=dflogica, use_container_width=True, hide_index=True)
"""data_frame ['DATA/HORA ALTERAÇÃO'] = pd.to_datetime(data_frame['DATA/HORA ALTERAÇÃO']).dt.date


nova_ordem = data_frame[["NOME", "PLACA","SISTEMA DE MONITORAMENTO"]]
data_frame = nova_ordem"""


