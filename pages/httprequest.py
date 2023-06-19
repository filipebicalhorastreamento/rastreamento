import requests

url = "https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/headers_authorization?cliente=3542&nome=operacional&senha=WR3D5K"

payload = {}
headers = {}

session = requests.Session()
response = session.post(url=url, headers=headers, data=payload)
data = response.json()

# Verifica se a autenticação foi bem-sucedida
if response.status_code == 200 and data.get('error') == False:
    # Faz uma solicitação GET para buscar um veículo específico
    chave_api = 'c5b79e7ce0c72d6e3c9842a51433c726'
    veiculo_url = f'https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/buscar_veiculo/{chave_api}'
    veiculo_response = session.get(url=veiculo_url)
    veiculo_data = veiculo_response.json()

    # Exibe os dados no Streamlit
    st.write(veiculo_data)
else:
    print('Erro na autenticação. Verifique as credenciais.')
