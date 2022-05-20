#Bibliotecas importadas
import streamlit as st
from classes import *
from PIL import Image

#Remove menu de hamburguer do streamlit
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#Remove rodapé do streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#Informações do app mostradas na tela inicial
st.title("Sistema Legionário")
st.markdown('# Setor de TI e desenvolvimento')
st.sidebar.title("Opções")
setor = st.sidebar.selectbox("Gerenciamento de Computadores por Setor", ["Selecione...","Cobrança", "Call Center", "Financeiro", "Gerencia", "Caixa", "Atendimento SAC", "Vendas", "Sede RCA"])
about = st.sidebar.selectbox("Informações do sistema Legionário", ["Selecione...","Sobre", "Política de Privacidade", "Termos de Uso"])

#Tipos de Computadores e especiificações
cobranca1 = Computadores("Windows 10", "Intel Core 2 Quad", "3GB", "14 anos de idade", "Sem Registro")
cobranca2 = Computadores("Windows 11", "Intel Pentium Gold", "8 GB", "3 anos de idade", "Sem Registro")
cobranca3 = Computadores("Windows 11", "Intel Core i3", "6 GB", "6 anos de uso", "07 de abril de 2022")
cobranca4 = Computadores("Windows 11", "Intel Core i5", "8 GB", "3 anos de idade", "07 de fevereiro de 2022")

cx1 = Computadores("Windows 11", "Intel Pentium Gold", "8GB", "3 anos de idade", "07 de março de 2022")
cx2 = Computadores("Windows 11", "Intel Pentium Gold", "8GB", "3 anos de idade", "27 de janeiro de 2022")

vendas1 = Computadores("Windows 10","Intel Core i3", "2 GB", "6 anos de idade", "31 de janeiro de 2022")
vendas2 = Computadores("Windows 10","Intel Core i3", "2 GB", "6 anos de idade", "13 de janeiro de 2020")

atendimentoSac1 = Computadores("Windows 11 Pro","Intel Duo E7500","4GB","12 Anos de Idade","11 de Abril de 2022")
atendimentoSac2 = Computadores("Windows 11 Home","Intel I5 3330","8GB","2 Anos de Idade","03 de Maio de 2022")

CallC7 = Computadores("Windows 11 Pro","Intel 5 3330","8Gb","2 Anos de Idade","16 de Maio de 2022")
CallC8 = Computadores("Windows 11 Pro","AMD Athalon 200GE","GB","1 ano","09 de Fevereiro de 2022")
CallC10 = Computadores("Windows 11 Pro","AMD Athlon 200GE","8GB","4 Anos de Idade","12 de Abril de 2022")
CallC11 = Computadores("Windows 11 Pro","AMD Athlon 200GE","8GB","3 Anos de Idade","12 de Abril de 2022")
CallC2 = Computadores("Windows 11 Pro","Intel 3 550","8GB","11 Anos de Idade","20 de Abril de 2022")
CallC3 = Computadores("Windows 11 Pro","Intel 3 550","6GB","11 Anos de Idade","07 de Março de 2022")
CallC4 = Computadores("windows 11 Pro","AMD Atholon 200GE","8GB","1 Ano de Idade","05 de Maio de 2022")
CallC5= Computadores("Windows 10 Pro","Intel 3 550","4GB","11 Anos de Idade","25 de Janeiro de 2022")
CallC6= Computadores("Windows 10 Pro","Intel 3 550","4GB","11 Anos de Idade","07 de Abril de 2022")
CallC1= Computadores("Windows 11 Home","Intel 5 3330","8GB","2 Anos de Idade","31 de Março de 2022")

#Variáveis de conteúdo na tela principal relacionado com a sidebar  
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

elif setor == "Call Center":
   
    fila7,fila8,fila9,fila10,fila11 = st.columns(5)
    with fila7:
        st.subheader("CallC7")
        st.text(CallC7.os)
        st.text(CallC7.processador)
        st.text(CallC7.memoria)
        st.text(CallC7.idade)
        st.text(CallC7.dataFormatacao)
    with fila8:
        st.subheader("CallC8")
        st.text(CallC8.os)
        st.text(CallC8.processador)
        st.text(CallC8.memoria)
        st.text(CallC8.idade)
        st.text(CallC8.dataFormatacao)
    with fila10:
        st.subheader("CallC10")
        st.text(CallC10.os)
        st.text(CallC10.processador)
        st.text(CallC10.memoria)
        st.text(CallC10.idade)
        st.text(CallC10.dataFormatacao)
    with fila11:
        st.subheader("CallC11")
        st.text(CallC11.os)
        st.text(CallC11.processador)
        st.text(CallC11.memoria)
        st.text(CallC11.idade)
        st.text(CallC11.dataFormatacao)
    fila2,fila3,fila4,fila5,fila6 = st.columns(5)
    with fila2:
        st.subheader("CallC2")
        st.text(CallC2.os)
        st.text(CallC2.processador)
        st.text(CallC2.memoria)
        st.text(CallC2.idade)
        st.text(CallC2.dataFormatacao)
    with fila3:
        st.subheader("CallC3")
        st.text(CallC3.os)
        st.text(CallC3.processador)
        st.text(CallC3.memoria)
        st.text(CallC3.idade)
        st.text(CallC3.dataFormatacao)
    with fila4:
        st.subheader("CallC4")
        st.text(CallC4.os)
        st.text(CallC4.processador)
        st.text(CallC4.memoria)
        st.text(CallC4.idade)
        st.text(CallC4.dataFormatacao)
    with fila5:
        st.subheader("CallC5")
        st.text(CallC5.os)
        st.text(CallC5.processador)
        st.text(CallC5.memoria)
        st.text(CallC5.idade)
        st.text(CallC5.dataFormatacao)
    with fila6:
        st.subheader("CallC6")
        st.text(CallC6.os)
        st.text(CallC6.processador)
        st.text(CallC6.memoria)
        st.text(CallC6.idade)
        st.text(CallC6.dataFormatacao)
    fila1, fila18 = st.columns(2)
    with fila1:
        st.subheader("CallC1")
        st.text(CallC1.os)
        st.text(CallC1.processador)
        st.text(CallC1.memoria)
        st.text(CallC1.idade)
        st.text(CallC1.dataFormatacao)

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
    st.subheader('Antendimento SAC Presencial')
    colSac1, colSac2 = st.columns(2)
    with colSac1:
        st.subheader('AS 1')
        st.text(atendimentoSac1.os)
        st.text(atendimentoSac1.processador)
        st.text(atendimentoSac1.memoria)
        st.text(atendimentoSac1.idade)
        st.text(atendimentoSac1.dataFormatacao)
    with colSac2:
        st.subheader('AS 2')
        st.text(atendimentoSac2.os)
        st.text(atendimentoSac2.processador)
        st.text(atendimentoSac2.memoria)
        st.text(atendimentoSac2.idade)
        st.text(atendimentoSac2.dataFormatacao)


    imageAtendimentoSac = Image.open('fluxos/Atendimento Sac.png')
    st.image(imageAtendimentoSac, caption='Organização de computadores do Atendimento Presencial do Sac', use_column_width=True)
elif setor == "Vendas":
    st.subheader("Setor de Vendas")
    colVendas1, colVendas2 = st.columns(2)
    with colVendas1:
        st.subheader("V 01")
        st.text(vendas1.os)
        st.text(vendas1.processador)
        st.text(vendas1.memoria)
        st.text(vendas1.idade)
        st.text(vendas1.dataFormatacao)
    with colVendas2:
        st.subheader("V 02")
        st.text(vendas2.os)
        st.text(vendas2.processador)
        st.text(vendas2.memoria)
        st.text(vendas2.idade)
        st.text(vendas2.dataFormatacao)
elif setor == "Sede RCA":
    st.warning('Ainda estamos coletando esses dados. Aguarde mais um pouco.')

#Variaveis de informações sobre o sistema Legionário
if about == "Sobre":
    st.subheader('Sistema Legionário versão 0.12')
    st.text('Construído utilizando a linguagem Python e baseado na licença MIT.')
    st.text('Desenvolvido pelo setor de TI da Speed Fiber Teresópolis')
    st.text('Desenvolvedores: Iago Chiapetta, Patrick Gonçalves.')
elif about == "Termos de Uso":
    st.subheader("Termos de Uso")
    st.text("Este software foi produzido para ser utilizado por todos os funcionários \nda Speed Fiber e somente por eles.")
    st.text("Qualquer uso por outras pessoas além das citadas acima fere os termos de \nutilização e deve ser evitado.")
    st.text("Qualquer modificação nos equipamentos da Speed Fiber deve ser registrada aqui \ne só pode ser feita com o consentimento do Gerente Geral.")
    st.text("O uso de qualquer parte deste software em outros projetos ou \nsoftwares é totalmente proibido e pode acarretar em problemas legais.")
    st.text("Este software é propriedade intelectual de Iago Chiapetta.")
elif about == "Politica de Privacidade":
    st.subheader("Política de Privacidade")
    st.text('Este software coleta e exibe dados e informações sobre todas as máquinas e \ncomputadores atualmente em uso na Speed Fiber Teresópolis.')

        


