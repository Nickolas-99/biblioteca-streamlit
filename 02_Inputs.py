import streamlit as st

# Comandos de inputs:
nome = st.text_input("Digite o seu nome:")
    
idade = st.number_input("Digite sua idade:", 0, 100)

if st.button("Enviar"):
    st.write(f"seja bem vindo {nome}")
    st.write(f"sua idade é {idade}")
    
# Comandos de Seleções:
opoes = st.selectbox("Qual sua cor favorita?", ["azul", "verde", "vemelho", "branco"])

multiplas = st.multiselect("Comidas favoritas:", ["frango", "baião", "salada", "sorvete"])

checkbox = st.checkbox("Aceito os Termos e Condições da Plataforma.")

radio = st.radio("marque a resposta",(1,2,3,4,5))
