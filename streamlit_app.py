import streamlit as st

st.title('Hola, Mundo!')
st.write('Esta es mi primera aplicación en Streamlit.')

nombre = st.text_input('Escribe tu nombre:')
if nombre:
    st.write(f'¡Hola, {nombre}!')