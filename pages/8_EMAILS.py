import streamlit as st
import smtplib
st.title('MODELOS DE EMAIL')
col1, col2, col3 = st.columns([3, 3, 3])
col1.write('Atenção: Rastreador sem comunicação.')
col1.code('''
    Prezado [nome_associado], o rastreamento do seu veículo de placa: [placa] está sem atualização há pelo menos 96 horas.

    A desatualização de veículos pode ser ocasionada pelos motivos abaixo:

    1. Fora da cobertura de GSM (celular)
    2. Veículo desligado desde a ultima atualização
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
col3.write('Agendamento de retirada')
col3.code('''
    Olá [nome_associado], tudo bem?
    
    Gostaria de agendar com você a retirada do equipamento rastreador do seu veículo.
    Lembrando que o *equipamento rastreador é entregue como comodato, para o uso dos serviços de rastreamento em quanto associado Mobili - Veja o Regulamento de Rastreador, aqui.
    Entre em contato, no número 31999409900 (Clique aqui para começar uma conversa via WhatsApp).

    Caso já tenha retirado o equipamento, favor desconsiderar esse e-mail.

    *Regulamento do Rastreador Mobili:
    Cláusula 3ª - O equipamento será cedido pela MOBILI em regime de comodato, de modo que fica o associado obrigando a devolvê-lo no prazo máximo de 07 (sete) dias úteis em caso de cancelamento, nas mesmas condições em que o receber. A não devolução do aparelho acarretará cobrança de multa no valor de 800,00 (oitocentos reais), contemplando essa o valor do equipamento e as despesas da MOBILI com procedimentos administrativos, judiciais e extrajudiciais para ressarcimento. Por sua vez, o inadimplemento da referida multa ensejará a inclusão do nome do associado nos órgãos de proteção ao crédito, além de legitimar procedimentos de cobrança, como citado, judiciais e extrajudiciais.


    Tem dúvidas? Entre em contato no seu canal preferido:
    Mobili Express: 31999409900



    ''')
col4, col5, col6 = st.columns([3, 3, 3])
col4.write('Desprotegido')
col4.code('''
Prezado(a), venho como lembrete que seu veículo estará desprotegido até que o equipamento rastreador for instalado devidamente.

Entre em contato para agendar a instalação através no WhatsApp pelo (31)99940-9900 ou ligue para nossa central através do (31) 2515-1616.

Lembrete da cláusula 3.6.1 do FAM:
"3.6.1 – Para todos os veículos citados na cláusula 3.6 e seus parágrafos, os eventos danosos reparáveis e irreparáveis em casos de furto e roubo somente serão amparados pelo FAM após a instalação do equipamento." 

REAGENDAMENTO: basta entrar em contato com antecedência mínima de 24h através no WhatsApp pelo (31)99940-9900 ou ligue para nossa central através do (31) 2515-1616. 
IMPRODUTIVA: Em casos devido a desencontro proporcionado pelo associado ou não comunicado com antecedência, terá um custo de instalação adicional de R$50,00 cobrado na próxima mensalidade.


Tem dúvidas? Entre em contato no seu canal preferido:
Mobili Express: 31999409900
Telefone Fixo: 31 2515-1616
E-mail: rastreador@gomobili.com.br

Qualquer dúvida ou sugestão estou à disposição.
''')
