import streamlit as st

import controller.cliente as cliente

def deletar():
    st.title(' Deletar Dados')

    with st.form(key='delet'):
        input_id = st.number_input(label= 'insira o id' , format='%i')

        button_submit = st.form_submit_button('Enviar')

        if button_submit:
            cliente.Excluir(int(input_id))
            