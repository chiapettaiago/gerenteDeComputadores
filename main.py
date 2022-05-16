import streamlit as st
from classes import *

st.title("Gerenciamento de computadores da Speed Fiber")
st.markdown('# Setor de TI e desenvolvimento')
setor = st.sidebar.selectbox("Setor", ["Cobrança", "Call Center", "Financeiro", "Gerencia", "Caixa", "Atendimento SAC", "Vendas"])

cobranca1 = Computadores("Windows 10", "Intel Core 2 Quad", "3GB", "14 anos de idade", "Juliana Menon")
cobranca2 = Computadores("Windows 11", "Intel Pentium Gold", "8 GB", "3 anos de idade", "Monique Mattos")

if setor == "Cobrança":
    col1, col2, col3, col4 = st.columns(4) 
    with col1:
        st.subheader("Cobranca 01")
        st.text(cobranca1.os)
        st.text(cobranca1.processador)
        st.text(cobranca1.memoria)
        st.text(cobranca1.idade)
        st.text(cobranca1.utilizador)
    with col2:
        st.subheader("Cobranca 02")
        st.text(cobranca2.os)
        st.text(cobranca2.processador)
        st.text(cobranca2.memoria)
        st.text(cobranca2.idade)
        st.text(cobranca2.utilizador)

