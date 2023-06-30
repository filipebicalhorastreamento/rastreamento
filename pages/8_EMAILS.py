import streamlit as st
st.title('MODELOS DE EMAIL')
col1, col2, col3 = st.columns([3, 3, 3])
col1.write('Atenção: Aviso de Veículos Desatualizados')
col1.code('''
    ***Atenção: Aviso de Veículos Desatualizados***

    Veículos Desatualizados:
    Prezado cliente, segue a lista de 3 veículo(s) sem atualização há pelo menos 96 horas.

    A desatualização de veículos pode ser ocasionada pelos motivos abaixo:

    Fora da cobertura de GSM (celular)
    Desligado desde a ultima atualização
    Em manutenção.
    Equipamento com problema.

    Caso o seu veículo não esteja em nenhuma das 3 primeiras situações, entre em contato pelo telefone (31) 2535-6060 [ ON SIG RASTREAMENTO ] solicitando uma verificação do equipamento.
    ''')

st.markdown(
        """
        **LINKS ÚTEIS:**  
        Atenção: Aviso de Veículos Desatualizados

Veículos Desatualizados:
Prezado cliente, segue a lista de 3 veículo(s) sem atualização há pelo menos 96 horas.

A desatualização de veículos pode ser ocasionada pelos motivos abaixo:

Fora da cobertura de GSM (celular)
Desligado desde a ultima atualização
Em manutenção.
Equipamento com problema.

Caso o seu veículo não esteja em nenhuma das 3 primeiras situações, entre em contato pelo telefone (31) 2535-6060 [ ON SIG RASTREAMENTO ] solicitando uma verificação do equipamento.
        
        """
    )
