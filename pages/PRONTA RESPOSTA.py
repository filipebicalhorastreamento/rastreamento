import streamlit as st
import datetime
from datetime import date
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(layout="wide")
st.title('MOBILI - RASTREAMENTO')
st.subheader('PRONTA RESPOSTA')
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

@st.cache_data
def load_data(nrows):
    data = load_data2(st.secrets["public_gsheets_url2"])
    uppercase = lambda x: str(x).upper()
    data.rename(uppercase, axis='columns', inplace=True)
    return data

def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

dados = load_data(10000000)

data_frame = pd.DataFrame(dados)
data_frame ['DATA'] = pd.to_datetime(data_frame ['DATA']).dt.date

estado = data_frame['ESTADO'].value_counts().to_frame()
estado_count = pd.DataFrame({'ESTADO': estado.index, 'Count': situações['count']})

c = alt.Chart(estado_count).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Count", type="quantitative"),
    color=alt.Color(field="ESTADO", type="nominal"),
)

col1, col2, col3 = st.columns([3, 3, 3])
col1.altair_chart(c, use_container_width=True)


st.dataframe(data=data_frame, use_container_width=True, hide_index=True)
