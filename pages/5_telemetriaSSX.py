import streamlit as st
import requests
from urllib3.exceptions import InsecureRequestWarning

# ! desativa o aviso de ssl, remover na versão final
# ! verificar ssl deve ser True, está sendo alterado para False para testes
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
verificar_ssl = False

# Autenticação
url = "https://integration.systemsatx.com.br/Login"
params = {'Username': 'filipebicalho.rastreamento@gmail.com',
    'Password': 'A@sU8e1Gzl',
    'HashAuth': 'ACB2CC74-D4E2-4835-9E49-41109C43D6CB'}

session = requests.Session()
authorization_request = session.post(url=url, params=params, verify=verificar_ssl)
authorization_data = authorization_request.json()

# Verifica se a autenticação foi bem-sucedida
if authorization_request.status_code == 200:
    # Faz uma solicitação POST
    headers = {
        "Authorization": authorization_data.get('AccessToken'),
        "Content-Type": "application/json"
    }
    json = [{
        "PropertyName": "TrackedUnitIntegrationCode",
        "Condition": "Equal",
        "Value": "CF-00044"
    }]

    url_historico_posicao = 'http://integration.systemsatx.com.br/Tracking/PositionHistory/List'
    historico_response = session.post(url=url_historico_posicao, json=json, headers=headers)
    historico_data = historico_response.json()

   df = pd.DataFrame.from_dict(historico_data)
    st.write(df)
else:
    print('Erro na autenticação. Verifique as credenciais.')
