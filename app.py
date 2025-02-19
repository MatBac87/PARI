import streamlit as st
from operator import add, sub, mul, truediv

st.set_page_config(page_title="Calcolatrice Pari 🧮", page_icon="🧮", layout="centered")

# Stile CSS ottimizzato
st.markdown("""
    <style>
        .operazione {
            font-size: 28px !important;
            font-weight: bold !important;
        }
        
        .stButton>button {
            width: 80px;
            height: 50px;
            margin: 5px;
            border-radius: 10px;
            border: 2px solid white !important;
        }
        
        /* Addizione - Rosso */
        div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-child button:nth-child(4) {
            background-color: #FF0000 !important;
            color: white !important;
        }
        
        /* Sottrazione - Blu */
        div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-child button:nth-child(3) {
            background-color: #0000FF !important;
            color: white !important;
        }
        
        /* Moltiplicazione - Marrone */
        div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-child button:nth-child(2) {
            background-color: #8B4513 !important;
            color: white !important;
        }
        
        /* Divisione - Verde */
        div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-child button:nth-child(1) {
            background-color: #008000 !important;
            color: white !important;
        }
        
        .stTextInput>div>div>input {
            font-size: 28px !important;
            height: 70px;
            text-align: right !important;
        }
    </style>
""", unsafe_allow_html=True)

# Stato della sessione
if "display" not in st.session_state:
    st.session_state.update({
        "display": "",
        "first_num": None,
        "operation": None
    })

# Funzioni
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
            # Correzione della condizione con parentesi bilanciate
            if not controlla_pari(st.session_state.first_num) or not controlla_pari(num2):
                st.error("Entrambi i numeri devono essere pari!")
                reset()
                return
                
            ops = {"+": add, "-": sub, "×": mul, "÷": truediv}
            result = ops[st.session_state.operation](st.session_state.first_num, num2)
            st.session_state.display = str(result)
            st.session_state.first_num = None
            st.session_state.operation = None
            
        except ZeroDivisionError:
            st.error("Errore: divisione per zero!")
            reset()

def controlla_pari(num):
    try:
        return int(num) % 2 == 0
    except ValueError:
        return False

def reset():
    st.session_state.display = ""
    st.session_state.first_num = None
    st.session_state.operation = None

# Interfaccia
st.title("Calcolatrice Pari 🧮")
st.text_input("Display", value=st.session_state.display, key="display", disabled=True)

cols = st.columns(4)

with cols[0]:
    st.button("7", on_click=update_display, args=("7",))
    st.button("4", on_click=update_display, args=("4",))
    st.button("1", on_click=update_display, args=("1",))
    st.button("0", on_click=update_display, args=("0",))

with cols[1]:
    st.button("8", on_click=update_display, args=("8",))
    st.button("5", on_click=update_display, args=("5",))
    st.button("2", on_click=update_display, args=("2",))
    st.button("C", on_click=reset)

with cols[2]:
    st.button("9", on_click=update_display, args=("9",))
    st.button("6", on_click=update_display, args=("6",))
    st.button("3", on_click=update_display, args=("3",))
    st.button("=", on_click=calculate)

with cols[3]:
    st.button("÷", on_click=set_operation, args=("÷",), key="div")
    st.button("×", on_click=set_operation, args=("×",), key="mul")
    st.button("-", on_click=set_operation, args=("-",), key="sub")
    st.button("+", on_click=set_operation, args=("+",), key="add")

st.warning("⚠️ Solo numeri pari! I risultati possono essere pari o dispari.")

