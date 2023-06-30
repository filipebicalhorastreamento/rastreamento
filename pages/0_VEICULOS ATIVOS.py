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
    data = load_data2(st.secrets["veiculos_ativos"])
    data = data.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    datagetrak = load_data2(st.secrets["getrak_plataforma"])
    datagetrak = datagetrak.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    return data, datagetrak


def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

dados = load_data(10000000)

data_frame = pd.DataFrame(dados)
st.write(dados)
"""data_frame ['DATA/HORA ALTERAÇÃO'] = pd.to_datetime(data_frame['DATA/HORA ALTERAÇÃO']).dt.date


nova_ordem = data_frame[["NOME", "PLACA","SISTEMA DE MONITORAMENTO"]]
data_frame = nova_ordem"""

st.dataframe(data=data_frame, use_container_width=True, hide_index=True)
