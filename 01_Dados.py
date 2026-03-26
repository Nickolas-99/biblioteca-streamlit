import streamlit as st

dicionario = {
    "Nome" : ["Rodrigo", "Hyana", "Carlos", "Matheus"],
    "Idade": [17, 22, 25, 30],
    "Area": ["Front-end", "back-end", "T.I", "Dados"]
}
# Comandos de Tabelas e colunas:

col1, col2 = st.columns(2)

with col1:
    st.dataframe(dicionario)
    
with col2:
    st.table(dicionario)
    
    # Seção de visualização de dados expansiva
    with st.expander("Clique aqui para ver mais"):
        st.subheader("Visualizando dados escondidos:")
        st.write("Dados complementares...")
