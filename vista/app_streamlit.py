import streamlit as st
from analizador.analizador import analizador

def main():
    st.title("Analizador Sintáctico 👑")

    input_string = st.text_input("Ingrese la cadena a analizar:")

    if st.button("Analizar"):
        resultado = analizador(input_string)
        if "Error de sintaxis" in resultado:
            st.error(resultado)
            st.error("La cadena es sintacticamente incorrecta ")
        else:
            st.success(resultado)
            st.success("La cadena es sintacticamente correcta ")

if __name__ == "__main__":
    main()
