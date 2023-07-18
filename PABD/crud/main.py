import streamlit as st

import page.insert as insert
import page.select as select
import page.delete as delete


#criando a barra lateral do menu
st.sidebar.title('Menu')
selectbox_a = st.sidebar.selectbox('Ação', ['Inserir', 'Consultar','deletar'])

if selectbox_a == 'Inserir':
    insert.inserir()

if selectbox_a == 'Consultar':
    select.consultar()

if selectbox_a == 'deletar':
    delete.deletar()