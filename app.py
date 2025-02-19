import streamlit as st 
from operator import add, sub, mul, truediv

# Configurazione della pagina
st.set_page_config(page_title="Calcolatrice Pari 🧮", page_icon="➗")

# Stile CSS personalizzato per migliorare l'aspetto
st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        border-radius: 10px;
        margin: 3px;
    }
    .number { background-color: #4a4a4a !important; color: white !important; }
    .operator { background-color: #ff9500 !important; color: white !important; }
    .special { background-color: #a6a6a6 !important; color: black !important; }
    </style>
""", unsafe_allow_html=True)

# Inizializzazione dello stato della sessione
if "display" not in st.session_state:
    st.session_state.display = ""
if "first_num" not in st.session_state:
