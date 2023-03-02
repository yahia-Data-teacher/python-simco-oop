import streamlit as st

options = ['Option 1', 'Option 2', 'Option 3']
selected_option = st.selectbox('Select an option', options)

st.write('You selected:', selected_option)