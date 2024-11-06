import streamlit as st

st.title("Bienvenidos a LectorLab")
st.write(
    "Este es un espacio donde puedes subir tus documentos de laboratorio para ser analizados. Recuerda que este servicio no reemplaza la opinión de un médico, es solo una orientación para enriquecer tu conocimiento"
)

import os

def abrir_explorador_archivos():
    """Abre el explorador de archivos del sistema operativo."""
    if os.name == 'nt':  # Si es Windows
        os.startfile('explorer')
    elif os.name == 'posix':  # Si es Linux o macOS
        os.system('xdg-open')

st.button('Buscar Archivo', on_click=abrir_explorador_archivos)
