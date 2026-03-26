import streamlit as st

if "nome" not in st.session_state:
    st.session_state.nome = ""
    
# Comando de escrita:
st.title("Jhon Nickolas")
st.header("Curso Desenvolvedor Full Stack")
st.subheader("Módulo Python")
st.write("Biblioteca Streamlit ;)")

st.divider()

