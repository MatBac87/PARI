import streamlit as st
from operator import add, sub, mul, truediv

# Configurazione della pagina
st.set_page_config(page_title="Calcolatrice Pari 🧮", page_icon="🧮", layout="centered")

# Stile CSS personalizzato con colori migliorati
st.markdown("""
    <style>
        .stButton>button {
            width: 80px;
            height: 50px;
            font-size: 20px;
            margin: 5px;
            border-radius: 10px;
            border: none;
            transition: all 0.3s ease;
        }
        
        /* Divisione - Verde */
        div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:nth-child(4) button:nth-child(1) {
            background-color: #4CAF50 !important;
            color: white !important;
        }
        
        /* Moltiplicazione - Marrone */
        div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:nth-child(4) button:nth-child(2) {
            background-color: #795548 !important;
            color: white !important;
        }
        
        /* Sottrazione - Blu */
        div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:nth-child(4) button:nth-child(3) {
            background-color: #2196F3 !important;
            color: white !important;
        }
        
        /* Addizione - Rosso */
        div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:nth-child(4) button:nth-child(4) {
            background-color: #F44336 !important;
            color: white !important;
        }
        
        .stTextInput>div>div>input {
            font-size: 24px !important;
            text-align: right !important;
            color: #333 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Inizializzazione stato sessione
if "display" not in st.session_state:
    st.session_state.display = ""
if "first_num" not in st.session_state:
    st.session_state.first_num = None
if "operation" not in st.session_state:
    st.session_state.operation = None

# Funzioni di controllo
def controlla_pari(num):
    try:
        return int(num) % 2 == 0
    except ValueError:
        return False

def update_display(value):
    st.session_state.display += value

def set_operation(op):
    if st.session_state.display:
        st.session_state.first_num = int(st.session_state.display)
        st.session_state.operation = op
        st.session_state.display = ""

def calculate():
    if st.session_state.first_num is not None and st.session_state.display:
        try:
            num2 = int(st.session_state.display)
            
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
            st.error("❌ Errore: divisione per zero!")
            reset()

def reset():
    st.session_state.display = ""
    st.session_state.first_num = None
    st.session_state.operation = None

# Interfaccia utente
st.title("Calcolatrice Pari 🧮")
display = st.text_input("Display", value=st.session_state.display, key="display", disabled=True)

# Layout pulsanti
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

st.warning("⚠️ Solo numeri pari! I risultati possono essere pari o dispari.")


