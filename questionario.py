import streamlit as st
import pandas as pd
import os
from datetime import datetime

arquivo = 'interessados_workshop.csv'

st.title('👕 Interesse em Camisetas - NAUTEC')
st.warning('⚠️ Confirmação até dia 05. Envio para malharia dia 06.')

with st.form('Meu formulario'):
    nome = st.text_input('Seu nome')
    tamanho = st.radio('Seu tamanho:', ['Selecione', 'P', 'M', 'G', 'GG'])
    enviado = st.form_submit_button('Confirmar Interesse')

if enviado:
    if nome == '':
        st.error('Por favor, preencha o seu nome!')
    elif tamanho == 'Selecione':
        st.warning('Por favor, selecione um tamanho de camiseta!')
    else:
        
        ja_existe = False
        if os.path.exists(arquivo):
            df_existente = pd.read_csv(arquivo)
            if nome in df_existente['Nome'].values:
                ja_existe = True
        
        if ja_existe:
            st.error(f"O nome '{nome}' já está na lista! Não é necessário repetir.")
        else:
            data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            dados = {'Data/Hora': [data_atual], 'Nome': [nome], 'Tamanho': [tamanho]}
            df = pd.DataFrame(dados)
            
            header_necessario = not os.path.exists(arquivo)
            df.to_csv(arquivo, mode='a', index=False, header=header_necessario)
            st.success(f'Sucesso, {nome}! Registrado em {data_atual}.')

st.divider()

if st.checkbox('Visualizar lista de interessados (Admin)'):
    senha = st.text_input('Digite a senha de administrador', type='password')
    
    if senha == 'nautec2026': 
        if os.path.exists(arquivo):
            df_leitura = pd.read_csv(arquivo)
            st.dataframe(df_leitura)
            
    elif senha != '': 
        st.error('Senha incorreta!')
