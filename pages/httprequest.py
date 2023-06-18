import requests
import streamlit as st

# Define as informações de autenticação
auth_url = 'https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/headers_authorization'
auth_payload = {
    'cliente': '3542',
    'nome': 'operacional',
    'senha': 'WR3D5K'
}

# Faz a solicitação de autenticação
response = requests.post(auth_url, json=auth_payload)
data = response.json()

# Verifica se a autenticação foi bem-sucedida
if response.status_code == 200 and data.get('Error') == 'false':
    # Obtém o token de autenticação
    auth_token = data['Headers']['X-Auth-Token']
    headers = {'Authorization': auth_token}

    # Faz uma solicitação GET para buscar um veículo específico
    chave_api = 'sua_chave_api'
    veiculo_url = f'https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/buscar_veiculo/{chave_api}'
    veiculo_response = requests.get(veiculo_url, headers=headers)
    veiculo_data = veiculo_response.json()

    # Exibe os dados no Streamlit
    st.subheader('Dados do Veículo')
    st.write(veiculo_data)
else:
    st.error('Erro na autenticação. Verifique as credenciais.')

