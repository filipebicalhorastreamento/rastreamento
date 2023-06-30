import streamlit as st
import smtplib
st.title('MODELOS DE EMAIL')
col1, col2, col3 = st.columns([3, 3, 3])
col1.write('Atenção: Rastreador sem comunicação.')
col1.code('''
    ***Atenção: Rastreador sem comunicação.***

    Prezado [nome_associado], seu veículo de placa: [placa] está sem atualização há pelo menos 96 horas.

    A desatualização de veículos pode ser ocasionada pelos motivos abaixo:

    1. Fora da cobertura de GSM (celular)
    2. Desligado desde a ultima atualização
    3. Veículo em manutenção.
    4. Equipamento com problema.

    Caso o seu veículo não esteja em nenhuma das 3 primeiras situações, entre em contato através dos canais abaixo e solicite uma verificação do equipamento.

    Mobili Express: 31999409900 WhatsApp
    Telefone Fixo: 31 2515-1616
    E-mail: rastreador@gomobili.com.br
    
    Caso já tenha solicitado a verificação, favor desconsiderar esse e-mail.
    Cláusula 3.6.3 do FAM – Fundo de Amparo Mobili:
    "3.6.3 – A responsabilidade da fiscalização de funcionamento e manutenção do equipamento é de inteira responsabilidade do associado. Se porventura na data do evento danoso o equipamento estiver inoperante, o associado não terá o amparo do FAM para os casos de despesas reparáveis e irreparáveis oriundas de furto e roubo." 
    ''')

col2.write('Contato sem sucesso.')
col2.code('''
   Olá [nome_associado], tudo bem? 

   Tentamos contato através do telefone de cadastro, porém não obtivemos sucesso.
   Realize o agendamento do Serviço de Instalação - Rastreamento Mobili, através dos canais abaixo: 
   Mobili Express: 31999409900 WhatsApp
   Telefone Fixo: 31 2515-1616
   E-mail: rastreador@gomobili.com.br
   Cláusula 3.6.1 do FAM – Fundo de Amparo Mobili:
   "3.6.1 – Para todos os veículos citados na cláusula 3.6 e seus parágrafos, os eventos danosos reparáveis e irreparáveis em casos de furto e roubo somente serão amparados pelo FAM após a instalação do equipamento." 
   Veja o Regulamento do FAM, aqui.
   Veja o Regulamento de Rastreador, aqui.

   *Para reagendamento basta entrar em contato com antecedência de 24h. Em caso de visita improdutiva sem aviso do associado com antecedência, terá um custo de instalação adicional de R$50,00 cobrado na próxima mensalidade.
   Caso já tenha instalado ou solicitado a instalação, favor desconsiderar esse e-mail.
   Qualquer dúvida ou sugestão estou à disposição. 

    ''')
