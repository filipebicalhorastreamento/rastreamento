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
tab2, tab1 = st.tabs(["📈 Chart", "🗃 Data"])
situações = data['SITUAÇÃO'].value_counts()
situações = data['SITUAÇÃO'].value_counts().to_frame().rename(columns={'SITUAÇÃO': 'ocorrências'})
#situações = situações.set_index('SITUAÇÃO')
situações_invertido = situações.T
tab1.subheader("A tab with the data")
tab1.write(situações_invertido)
tab2.subheader("A tab with a chart")
tab2.bar_chart(situações)


# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('DADOS BRUTOS PARA CONFERÊNCIA')
if st.checkbox('Mostrar dados'):
    st.subheader('Dataframe')
    st.write(data)
