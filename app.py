import streamlit as st
from operator import add, sub, mul, truediv

# Configurazione della pagina
st.set_page_config(page_title="Calcolatrice Pari 🧮", page_icon="🧮", layout="centered")

# Stile CSS personalizzato per migliorare l'interfaccia
st.markdown("""
    <style>
        .stButton>button {
            width: 100px;
            height: 50px;
            font-size: 20px;
            margin: 5px;
            border-radius: 10px;
        }
        .stTextInput>div>div>input {
            font-size: 24px !important;
            text-align: right;
        }
    </style>
""", unsafe_allow_html=True)

# Inizializzazione dello stato della sessione
if "display" not in st.session_state:
    st.session_state.display = ""
if "first_num" not in st.session_state:
    st.session_state.first_num = None
if "operation" not in st.session_state:
    st.session_state.operation = None

# Funzione per controllare se un numero è pari
def controlla_pari(num):
    try:
        return int(num) % 2 == 0
    except ValueError:
        return False

# Funzione per aggiornare il display
def update_display(value):
    st.session_state.display += value

# Funzione per impostare l'operazione
def set_operation(op):
    if st.session_state.display:
        st.session_state.first_num = int(st.session_state.display)
        st.session_state.operation = op
        st.session_state.display = ""

# Funzione per eseguire il calcolo
def calculate():
    if st.session_state.first_num is not None and st.session_state.display:
        try:
            num2 = int(st.session_state.display)
            
            # Controllo che entrambi i numeri siano pari
            if not controlla_pari(st.session_state.first_num) or not controlla_pari(num2):
                st.error("⚠️ Entrambi i numeri devono essere pari!")
                reset()
                return
                
            ops = {"+": add, "-": sub, "×": mul, "÷": truediv}
            result = ops[st.session_state.operation](st.session_state.first_num, num2)
            
            st.session_state.display = str(result)
            st.session_state.first_num = None
            st.session_state.operation = None
            
        except ZeroDivisionError:
            st.error("❌ Errore: divisione per zero non permessa!")
            reset()

# Funzione per resettare il display
def reset():
    st.session_state.display = ""
    st.session_state.first_num = None
    st.session_state.operation = None

# Layout della calcolatrice
st.title("Calcolatrice Pari 🧮")

# Display della calcolatrice
st.text_input("", value=st.session_state.display, key="calc_display", disabled=True)

# Griglia pulsanti
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=update_display, args=("7",))
    st.button("4", on_click=update_display, args=("4",))
    st.button("1", on_click=update_display, args=("1",))
    st.button("0", on_click=update_display, args=("0",))

with col2:
    st.button("8", on_click=update_display, args=("8",))
    st.button("5", on_click=update_display, args=("5",))
    st.button("2", on_click=update_display, args=("2",))
    st.button("C", on_click=reset)

with col3:
    st.button("9", on_click=update_display, args=("9",))
    st.button("6", on_click=update_display, args=("6",))
    st.button("3", on_click=update_display, args=("3",))
    st.button("=", on_click=calculate)

with col4:
    st.button("÷", on_click=set_operation, args=("÷",))
    st.button("×", on_click=set_operation, args=("×",))
    st.button("-", on_click=set_operation, args=("-",))
    st.button("+", on_click=set_operation, args=("+",))

# Messaggio di avviso
st.warning("⚠️ Solo numeri pari! I risultati possono essere pari o dispari.")

