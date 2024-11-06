import streamlit as st

with st.container():
    st.markdown(
        """
        <div style='text-align: center; font-size: 3rem; color: #4CAF50;'>
        Bienvenidos a LectorLab
        </div>
        """, unsafe_allow_html=True
    )
st.markdown(
    """
    <div style='text-align: center;'>
    Este es un espacio donde puedes subir tus documentos de laboratorio para ser analizados. Recuerda que este servicio no reemplaza la opinión de un médico, es solo una orientación para enriquecer tu conocimiento
    </div>
    """, unsafe_allow_html=True
)

import streamlit as st
import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

st.button('Seleccionar Archivo', on_click=seleccionar_archivo)
