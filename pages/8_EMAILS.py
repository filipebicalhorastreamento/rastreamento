import streamlit as st
st.title('MODELOS DE EMAIL')
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Sentiment:', run_sentiment_analysis(txt))
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
