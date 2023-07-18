import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Cadastro tabela')
    
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira seu nome:')
        input_desc = st.text_input(label='Insira a descricao:')
        input_preco = st.number_input(label='Insira o preco')
        input_id = st.number_input(label='Insira o id ')
        input_date = st.date_input(label='insira data')
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(int(input_id),input_name,input_desc, input_preco, input_date)
            st.success('Cliente incluido com sucesso')