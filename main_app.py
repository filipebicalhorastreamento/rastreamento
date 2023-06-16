import streamlit as st
import pandas as pd
import numpy as np

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


st.subheader('Veículos por situação.')
situações = data['SITUAÇÃO'].value_counts()
#situações = situações.rename({'count': 'ocorrências'}, axis='count')
situações_invertido = situações.T
st.bar_chart(situações)
st.table(situações)
st.write(situações_invertido)
# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('DADOS BRUTOS PARA CONFERÊNCIA')
if st.checkbox('Mostrar dados'):
    st.subheader('Dataframe')
    st.write(data)
