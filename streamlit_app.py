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
    Este es un espacio donde puedes subir tus documentos de laboratorio para ser analizados por la IA. Recuerda que este servicio no reemplaza la opinión, el criterio, la recomendación ni mucho menos el rol de un médico. Este servicio, solo te permite tener una orientación para enriquecer tu conocimiento acerca de tus resultados.
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
else:
    st.write("No has seleccionado ningún archivo.")
