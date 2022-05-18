import streamlit as st
from classes import *
from PIL import Image
import requests

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

cx1 = Computadores("Windows 11", "Intel Pentium Gold", "8GB", "3 anos de idade", "07 de março de 2022")
cx2 = Computadores("Windows 10", "Intel Pentium Gold", "8GB", "3 anos de idade", "27 de janeiro de 2022")

if setor == "Cobrança":
    st.subheader('Setor de Cobrança')
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
    st.image(image, caption='Organização de computadores da Cobrança', use_column_width=True)

elif setor == "Selecionar...":
    st.markdown('Este software fornece gerenciamento computadorizado e automatizado a todos os computadores da Speed Fiber.')
elif setor == "Call Center":
    image3 = Image.open('fluxos/Sala Sac Pronto.png')
    st.image(image3, caption='Organização de computadores do Sac', use_column_width=True)
elif setor == "Financeiro":
    st.warning('Ainda estamos coletando esses dados. Aguarde só mais um pouco.')
elif setor == "Gerencia":
    st.warning('Ainda estamos coletando esses dados. Aguarde só mais um pouco.')
elif setor == "Caixa":
    st.subheader('Caixas')
    cxCol1, cxCol2 = st.columns(2)
    with cxCol1:
        st.subheader('CX 01')
        st.text(cx1.os)
        st.text(cx1.processador)
        st.text(cx1.memoria)
        st.text(cx1.idade)
        st.text(cx1.dataFormatacao)
    with cxCol2:
        st.subheader('CX 02')
        st.text(cx2.os)
        st.text(cx2.processador)
        st.text(cx2.memoria)
        st.text(cx2.idade)
        st.text(cx2.dataFormatacao)
    imageCX = Image.open('fluxos/caixas.png')
    st.image(imageCX, caption='Organização de computadores do Caixa', use_column_width=True)
elif setor == "Atendimento SAC":
   imageAtendimentoSac = Image.open('fluxos/Atendimento Sac.png')
   st.image(imageAtendimentoSac, caption='Organização de computadores do Caixa', use_column_width=True)
elif setor == "Vendas":
    st.warning('Ainda estamos coletando esses dados. Aguarde só mais um pouco.')
        


