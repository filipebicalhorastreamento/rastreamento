import streamlit as st
import datetime
from datetime import date
import pandas as pd
import numpy as np
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
import io

# buffer to use for excel writer
buffer = io.BytesIO()
f_date = date.today()

st.set_page_config(layout="wide")
st.title('VEÍCULOS ATIVOS')
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

@st.cache_data
def load_data(nrows):
    veiculos_ativos = load_data2(st.secrets["veiculos_ativos"])
    uppercase = lambda x: str(x).upper()
    veiculos_ativos.rename(uppercase, axis='columns', inplace=True)
    logica_monitoramento = load_data2(st.secrets["logica_plataforma"])
    logica_monitoramento.rename(uppercase, axis='columns', inplace=True)
    softruck_monitoramento = load_data2(st.secrets["softruck_plataforma"])
    softruck_monitoramento.rename(uppercase, axis='columns', inplace=True)
    getrak_monitoramento = load_data2(st.secrets["getrak_plataforma"])
    getrak_monitoramento.rename(uppercase, axis='columns', inplace=True)
    return veiculos_ativos, logica_monitoramento, softruck_monitoramento, getrak_monitoramento

def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)
    
def convert_to_csv(dfbase):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return dfbase.to_csv(index=False).encode('utf-8')

veiculos_ativos, logica_monitoramento, softruck_monitoramento, getrak_monitoramento = load_data(10000000)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["ATIVOS SGR", "LÓGICA MONITORAMENTO", "SOFTRUCK", "GETRAK", "SAFECAR"])

dfveiculosativos =pd.DataFrame.from_dict(veiculos_ativos)
dflogica = pd.DataFrame.from_dict(logica_monitoramento)
dflogica.rename(columns = {'VEICULO PLACA':'PLACA'}, inplace = True)

dfsoftruck =pd.DataFrame.from_dict(softruck_monitoramento)
dfgetrak = pd.DataFrame.from_dict(getrak_monitoramento)

tab1.subheader('ATIVOS SGR')
ordem_sgr = dfveiculosativos[["NOME", "PLACA","SITUAÇÃO","CIDADE CLIENTE","ESTADO CLIENTE","OBSERVAÇÃO"]]
sgrfiltrado = ordem_sgr
dfveiculosativosshape = sgrfiltrado.shape
tab1.dataframe(data=sgrfiltrado, use_container_width=True, hide_index=True)
tab1.write(dfveiculosativosshape)

tab2.subheader('LOGICA MONITORAMENTO')
ordem_logica = dflogica[["PLACA", "ÚLTIMA TRANSMISSÃO","GPRS DATA","MARCA","MODELO","TELEFONE"]]
logicafiltrado = ordem_logica
logicafiltradoshape = logicafiltrado.shape
tab2.dataframe(data=logicafiltrado, use_container_width=True, hide_index=True)
tab2.write(logicafiltradoshape)

tab3.subheader('SOFTRUCK')
ordem_softruck = dfsoftruck[["PLACA", "ÚLTIMO ENVIO DE POSIÇÃO PARA O SERVIDOR","ÚLTIMA CONEXÃO COM O SERVIDOR","MARCA DO DISPOSITIVO","APELIDO DO MODELO","LINHA"]]
softruckfiltrado = ordem_softruck
softruckfiltradoshape = softruckfiltrado.shape
tab3.dataframe(data=softruckfiltrado, use_container_width=True, hide_index=True)
tab3.write(softruckfiltradoshape)

tab4.subheader('GETRAK')
ordem_getrak = dfgetrak[["PLACA", "DATA GPS"]]
getrakfiltrado = ordem_getrak
getrakfiltradoshape = getrakfiltrado.shape
tab4.dataframe(data=getrakfiltrado, use_container_width=True, hide_index=True)
tab4.write(getrakfiltradoshape)

transmissaoativos = dfveiculosativos[["NOME", "PLACA","SITUAÇÃO"]]
transmissaologica = dflogica[["PLACA", "ÚLTIMA TRANSMISSÃO"]]
transmissaosoftruck = dfsoftruck[["PLACA", "ÚLTIMA CONEXÃO COM O SERVIDOR"]]
transmissaogetrak = dfgetrak[["PLACA", "DATA GPS"]]

dfbase = transmissaoativos.merge(transmissaosoftruck,how ='left').merge(transmissaogetrak,how ='left').merge(transmissaologica,how ='left')
conditions = [
    dfbase['ÚLTIMA TRANSMISSÃO'].notnull(),
    dfbase['ÚLTIMA CONEXÃO COM O SERVIDOR'].notnull(),
    dfbase['DATA GPS'].notnull()
]

values = ['logica', 'softruck', 'getrak']

dfbase['ÚLTIMA TRANSMISSÃO'] = pd.to_datetime(dfbase['ÚLTIMA TRANSMISSÃO'] ,dayfirst=True)
dfbase['ÚLTIMA CONEXÃO COM O SERVIDOR'] = pd.to_datetime(dfbase['ÚLTIMA CONEXÃO COM O SERVIDOR'],dayfirst=True)
dfbase['DATA GPS'] = pd.to_datetime(dfbase['DATA GPS'],dayfirst=True)

dfbase['ultima_transmissao'] = dfbase['ÚLTIMA TRANSMISSÃO'].fillna(dfbase['ÚLTIMA CONEXÃO COM O SERVIDOR']).fillna(dfbase['DATA GPS'])
dfbase['ultima_transmissao'] = pd.to_datetime(dfbase['ultima_transmissao']).dt.date
dfbase['ultima_transmissao'] = dfbase['ultima_transmissao'].fillna(pd.to_datetime('1969-12-31').date())
dfbase['Nº DIAS'] = (f_date - dfbase['ultima_transmissao']) / np.timedelta64(1, 'D')

dfbase['plataforma'] = np.select(conditions, values, default='')
ordem_dfbase = dfbase[["NOME","PLACA", "ultima_transmissao", "plataforma", "Nº DIAS"]]
dfbasefiltrado = ordem_dfbase
st.dataframe(data=dfbasefiltrado, use_container_width=True, hide_index=True)

csv = convert_to_csv(dfbase)

# download button 1 to download dataframe as csv
download1 = st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='base rastreada.csv',
    mime='text/csv'
)

