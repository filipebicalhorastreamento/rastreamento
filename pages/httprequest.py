import requests

url = "https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/headers_authorization?cliente=3542&nome=operacional&senha=WR3D5K"

payload = {}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)
data = response.json()

print(response.text)


# Verifica se a autenticação foi bem-sucedida
if response.status_code == 200 and data.get('Error') == 'false':
    # Obtém o token de autenticação
    Accept = ('application/json')
    Autorization = data['Headers']['Authorization']
    XAuthToken = data['Headers']['X-Auth-Token']
    headers = {'Accept': Accept, 'X-Auth-Token': XAuthToken, 'Authorization': Autorization}
    print(headers)
    # Faz uma solicitação GET para buscar um veículo específico
    chave_api = 'c5b79e7ce0c72d6e3c9842a51433c726'
    veiculo_url = f'https://sgr.hinova.com.br/sgr/sgrv2_api/service_api/servicos/buscar_veiculo/{chave_api}'
    veiculo_response = requests.get(veiculo_url, headers=headers)
    veiculo_data = veiculo_response.json()

    # Exibe os dados no Streamlit
    print('Dados do Veículo')
    print(veiculo_data)
else:
    print('Erro na autenticação. Verifique as credenciais.')
