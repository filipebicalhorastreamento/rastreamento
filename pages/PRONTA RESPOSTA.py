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

data = load_data(10000)
data = pd.DataFrame(data)
st.dataframe(data=data, use_container_width=True, hide_index=True)

st.subheader('DADOS BRUTOS PARA CONFERÊNCIA')
if st.checkbox('Mostrar dados'):
    st.subheader('Dataframe')
    st.write(data)
