import streamlit as st
import time
import datetime
from datetime import date
import numpy as np
import pandas as pd
from app.rotinas import load_veiculos, readshets, load_clientes
st.set_page_config(page_title="MOBILI - RASTREAMENTO", layout="wide")
st.title('MOBILI - PENDENTE INSTALAÇÃO')
def load_data(nrows):
  veiculos = load_veiculos(10000000)
  safecar = readshets(st.secrets["safecar"])
  return veiculos, safecar
def convert_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False, sep=';')
f_date = date.today()
veiculos, safecar = load_data(10000000)
#CRIA OS DATAFRAMES
dfsafecar = pd.DataFrame.from_dict(safecar)
dfsafecar.rename(columns = {'ConcluÃ­do':'Conclusão','Placa':'PLACA'}, inplace = True)
dfsafecar = dfsafecar.apply(lambda x: x.astype(str).str.upper())
dfsafecar["Concluído"] = pd.to_datetime(dfsafecar["Concluído"]).dt.date
#dfsafecar["Concluído"] = pd.to_datetime(dfsafecar["Concluído"], format="%Y-%m-%d %H:%M")
#dfsafecar["Concluído"] = pd.to_datetime(dfsafecar["Concluído"], format="%d/%m/%Y", dayfirst=True)
dfveiculos = pd.DataFrame.from_dict(veiculos)
dfveiculos.rename(columns = {'placa_veiculo':'PLACA', 'nome_cliente':'NOME', 'situacao_veiculo':'SITUAÇÃO', 'fipe_valor_veiculo':'FIPE'}, inplace = True)
dfveiculos = dfveiculos.apply(lambda x: x.astype(str).str.upper())
pendentes = (dfveiculos['SITUAÇÃO'] == "PENDENTE INSTALAÇÃO") | (dfveiculos['SITUAÇÃO'] == "AGENDADO")| (dfveiculos['SITUAÇÃO'] == "RECUSADO")
dfveiculospendentes = dfveiculos[pendentes]
dfveiculospendentes = pd.merge(dfveiculospendentes, dfsafecar, on='PLACA', how='left')
#Processa os dataframes PENDENTE INSTALAÇÃO
dfveiculospendentes['ultima_atualizacao'] = pd.to_datetime(dfveiculospendentes['ultima_atualizacao']).dt.date
#dfveiculospendentes['Status'] = df = pd.merge(dfsafecar, dfveiculospendentes, on='PLACA', how='left')
dfveiculospendentes['Dias'] = (f_date - dfveiculospendentes['ultima_atualizacao']) / np.timedelta64(1, 'D')
dfveiculospendentes['Dias'] = pd.to_numeric(dfveiculospendentes['Dias'], errors='coerce').fillna(0).astype(int)
dfveiculospendentes['FIPE'] = pd.to_numeric(dfveiculospendentes['FIPE'], errors='coerce')
ordem_dfveiculospendentes = dfveiculospendentes[["NOME","PLACA","FIPE","cidade_veiculo", "Concluído", "SITUAÇÃO","Status","Dias"]]
dfveiculospendentes = ordem_dfveiculospendentes
agendado = (dfveiculospendentes['SITUAÇÃO'] == "AGENDADO")
dfagendado = dfveiculospendentes[agendado]
pendente = (dfveiculospendentes['SITUAÇÃO'] == "PENDENTE INSTALAÇÃO")
dfpendente = dfveiculospendentes[pendente]
recusado = (dfveiculospendentes['SITUAÇÃO'] == "RECUSADO")
dfrecusado = dfveiculospendentes[recusado]
novasinstalacoes = dfpendente['PLACA'].nunique()
statusnovasinstalacoes = dfpendente['Status'].value_counts()
statusnovasinstalacoes_texto = statusnovasinstalacoes.to_frame().to_string(header=False, index=True)
statusnovasinstalacoes_texto_com_quebra_de_linha = statusnovasinstalacoes_texto.replace('\n', ',\n')
agendados = dfagendado['PLACA'].nunique()
recusados = dfrecusado['PLACA'].nunique()
total_placas = dfveiculospendentes['PLACA'].nunique()
placas_por_situacao = dfveiculospendentes['SITUAÇÃO'].value_counts()
status_por_situacao = dfveiculospendentes.groupby('SITUAÇÃO')['Status'].nunique()
placas_acima_de_10_dias = dfveiculospendentes[dfveiculospendentes['Dias'] > 10]
#statusnovasinstalacoes_texto = statusnovasinstalacoes.to_frame().to_string()
st.write(f'Novas instalações: {novasinstalacoes} \n')
st.write(statusnovasinstalacoes_texto_com_quebra_de_linha)
st.write(f'Instalações agendadas: {agendados}\n')
st.write(f'Instalações recusadas: {recusados}\n')
#st.write('\nPlacas acima de 10 dias em uma mesma situação:\n', placas_acima_de_10_dias)
#st.write(f'Total de placas: {total_placas}\n')
dfveiculospendentes.sort_values(by='Status', ascending=True, inplace=True)
st.dataframe(data=dfveiculospendentes, use_container_width=True, hide_index=True)
csv1 = convert_to_csv(dfveiculospendentes)
download = st.download_button(
    label="Download",
    data=csv1,
    file_name='instalacoes.csv',
    mime='text/csv'
)
st.link_button("Atualiza planilhas", "https://webhookworkflow.swiftychat.com.br/webhook/d48eb156-79c6-4595-821b-b0d58ff9bc82")
st.link_button("Atualiza planilhas", "https://webhookworkflow.swiftychat.com.br/webhook/7d423110-29fd-4c58-a7c1-a0ab18cc761d")
st.link_button("Envia comunicados", "https://webhookworkflow.swiftychat.com.br/webhook/363ab170-45ff-4ff7-b8ff-3f3f96c2518a")
