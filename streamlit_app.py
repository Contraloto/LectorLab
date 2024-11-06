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
import os

def seleccionar_archivo():
    """Abre un diálogo para seleccionar un archivo y devuelve su ruta."""
    try:
        # Intenta utilizar la biblioteca tkinter para una interfaz más nativa
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()
        ruta_archivo = filedialog.askopenfilename()
        return ruta_archivo
    except ImportError:
        # Si tkinter no está instalado, utiliza streamlit-file-uploader
        try:
            import streamlit.components.v1 as components
            uploaded_file = components.file_uploader("Selecciona un archivo", type=["csv", "txt", "pdf"])  # Ajusta las extensiones según tus necesidades
            if uploaded_file is not None:
                return uploaded_file.name
            else:
                return None
        except ImportError:
            # Si ninguna de las opciones anteriores funciona, muestra un mensaje de error
            st.error("No se pudo importar ninguna biblioteca para seleccionar archivos. Verifica las instalaciones.")

# Botón para seleccionar el archivo
st.button("Seleccionar Archivo", on_click=seleccionar_archivo)

# Mostrar la ruta del archivo seleccionado (opcional)
ruta = seleccionar_archivo()
if ruta:
    st.write("Has seleccionado el archivo:", ruta)
