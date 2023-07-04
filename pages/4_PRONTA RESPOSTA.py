import streamlit as st
import datetime
from datetime import date
import pandas as pd
import numpy as np
import altair as alt
from streamlit_pandas_profiling import st_profile_report
st.set_page_config(layout="wide")
st.title('PRONTA RESPOSTA')
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

@st.cache_data
def load_data(nrows):
    data = load_data2(st.secrets["furtoeroubo"])
    uppercase = lambda x: str(x).upper()
    data.rename(uppercase, axis='columns', inplace=True)
    return data

def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

dados = load_data(10000000)

data_frame = pd.DataFrame(dados)
tab1, tab2 = st.tabs(["GERAL","Reporte"])

"""#data_frame ['DATA'] = pd.to_datetime(data_frame ['DATA']).dt.date

estado = data_frame['ESTADO'].value_counts().to_frame()
estado_count = pd.DataFrame({'ESTADO': estado.index, 'Count': estado['count']})
#trata os dados da fipe
faixas_preco = {
    '0 a 30 mil': (0, 30000),
    '30 a 50 mil': (30001, 50000),
    '50 a 70 mil': (50001, 70000),
    '70 mil ou mais': (70001, float('inf'))
}

FIPE = data_frame['FIPE'].value_counts().to_frame()
estado_count = pd.DataFrame({'ESTADO': estado.index, 'Count': estado['count']})
tabela_fipe['faixa_preco'] = pd.cut(data_frame['FIPE'], bins=[faixa[0] for faixa in faixas_preco.values()] + [float('inf')], labels=faixas_preco.keys())

estado = data_frame['ESTADO'].value_counts().to_frame()
estado_count = pd.DataFrame({'ESTADO': estado.index, 'Count': estado['count']})

c = alt.Chart(estado_count).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Count", type="quantitative"),
    color=alt.Color(field="ESTADO", type="nominal"),
)
c2 = alt.Chart(data_frame).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Count", type="quantitative"),
    color=alt.Color(field="ESTADO", type="nominal"),
)
c3 = alt.Chart(data_frame).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Count", type="quantitative"),
    color=alt.Color(field="FIPE", type="nominal"),
)

col1, col2, col3 = st.columns([3, 3, 3])
col1.subheader('POR ESTADO')
col1.altair_chart(c, use_container_width=True)
col2.subheader('POR FIPE')
col2.altair_chart(c2, use_container_width=True)
col3.subheader('POR MES')
col3.altair_chart(c3, use_container_width=True)"""


tab1.dataframe(data=data_frame, use_container_width=True, hide_index=True)

pr = data_frame.profile_report()

st_profile_report(pr)
