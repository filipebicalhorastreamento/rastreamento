import streamlit as st
import datetime
from datetime import date
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(layout="wide")
st.title('AGENDAMENTOS - INSTALAÇÕES')
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

@st.cache_data
def load_data(nrows):
    data = load_data2(st.secrets["public_gsheets_url3"])
    uppercase = lambda x: str(x).upper()
    data.rename(uppercase, axis='columns', inplace=True)
    return data

def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

dados = load_data(10000000)

df = pd.DataFrame.from_dict(dados)
Status = df['STATUS'].value_counts().to_frame()
DFStatus = pd.DataFrame({'Status': Status.index, 'Count': Status['count']})

c = alt.Chart(DFStatus).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Count", type="quantitative"),
    color=alt.Color(field="Status", type="nominal"),
)

col1, col2 = st.columns([1, 5])
col1.altair_chart(c, use_container_width=True)

col2.dataframe(data=dados, use_container_width=True, hide_index=True)
