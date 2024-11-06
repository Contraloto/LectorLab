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

# Botón para cargar archivo
archivo = st.file_uploader("Selecciona un archivo", type=None)

# Verifica si se seleccionó un archivo
if archivo is not None:
    st.write("Archivo cargado exitosamente:")
    st.write(f"Nombre del archivo: {archivo.name}")
    st.write(f"Tamaño del archivo: {archivo.size} bytes")

    # Si el archivo es de texto, puedes leerlo como ejemplo
    contenido = archivo.read()
    st.write("Contenido del archivo:")
    st.text(contenido.decode("utf-8", errors="ignore"))
else:
    st.write("No has seleccionado ningún archivo.")
