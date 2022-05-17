import streamlit as st
from classes import *
from PIL import Image

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Gerenciamento de computadores da Speed Fiber")
st.markdown('# Setor de TI e desenvolvimento')
st.sidebar.title("Opções")
setor = st.sidebar.selectbox("Setor", ["Selecionar...","Cobrança", "Call Center", "Financeiro", "Gerencia", "Caixa", "Atendimento SAC", "Vendas"])

cobranca1 = Computadores("Windows 10", "Intel Core 2 Quad", "3GB", "14 anos de idade", "Sem Registro")
cobranca2 = Computadores("Windows 11", "Intel Pentium Gold", "8 GB", "3 anos de idade", "Sem Registro")
cobranca3 = Computadores("Windows 11", "Intel Core i3", "6 GB", "6 anos de uso", "07 de abril de 2022")
cobranca4 = Computadores("Windows 11", "Intel Core i5", "8 GB", "3 anos de idade", "07 de fevereiro de 2022")

if setor == "Cobrança":
    col1, col2, col3, col4 = st.columns(4) 
    with col1:
        st.subheader("C 01")
        st.text(cobranca1.os)
        st.text(cobranca1.processador)
        st.text(cobranca1.memoria)
        st.text(cobranca1.idade)
    with col2:
        st.subheader("C 02")
        st.text(cobranca2.os)
        st.text(cobranca2.processador)
        st.text(cobranca2.memoria)
        st.text(cobranca2.idade)
    with col3:
        st.subheader("C 03")
        st.text(cobranca3.os)
        st.text(cobranca3.processador)
        st.text(cobranca3.memoria)
        st.text(cobranca3.idade)
        st.text(cobranca3.dataFormatacao)
    with col4:
        st.subheader("C 04")
        st.text(cobranca4.os)
        st.text(cobranca4.processador)
        st.text(cobranca4.memoria)
        st.text(cobranca4.idade)
        st.text(cobranca4.dataFormatacao)

    image = Image.open('fluxos/cobranca.png')
    st.image(image, caption='Organização de computadores da Cobrança')

elif setor == "Selecionar...":
    st.markdown('Este software fornece gerenciamento computadorizado e automatizado a todos os computadores da Speed Fiber.')
        


