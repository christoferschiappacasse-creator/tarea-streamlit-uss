"""Tarea evaluativa: componentes de la barra lateral y la zona principal."""
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Mi primera aplicación de Streamlit",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="expanded",
)

LOGO = Path(__file__).parent / "logo_uss_referencia.png"

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("Mi primera barra lateral de Streamlit")
    st.subheader("¡Hola, Barra Lateral!")
    st.write("Esto es una barra lateral")
    if LOGO.exists():
        st.image(str(LOGO), width=240)

    if st.button("Haz clic pero en la barra lateral", key="boton_lateral"):
        st.success("¡Hiciste clic en la barra lateral!")

    texto_lateral = st.text_input("Escribe algo en la barra:", key="texto_lateral")
    st.write("Escribiste en la barra:", texto_lateral)

# --- ÁREA PRINCIPAL ---
st.title("Mi primera aplicación de Streamlit")
st.header("¡Hola, Streamlit!")
st.write("Esta es una aplicación simple")
if LOGO.exists():
    st.image(str(LOGO), width=330)

if st.button("Haz clic", key="boton_principal"):
    st.success("¡Hiciste clic en el área principal!")

texto_principal = st.text_input("Escribe algo:", key="texto_principal")
st.write("Escribiste:", texto_principal)
