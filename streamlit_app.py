import streamlit as st
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import tempfile

# Configura la ruta de Tesseract si es necesario
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Interfaz Streamlit
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
archivo = st.file_uploader("Selecciona un archivo", type=["png", "jpg", "jpeg", "pdf"])

if archivo is not None:
    st.write("Archivo cargado exitosamente:")
    st.write(f"Nombre del archivo: {archivo.name}")
    st.write(f"Tamaño del archivo: {archivo.size} bytes")

    # Botón para procesar OCR
    if st.button("Procesar OCR"):
        with st.spinner("Procesando el archivo..."):
            if archivo.name.endswith(".pdf"):
                # Convierte PDF a imágenes
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                    temp_file.write(archivo.read())
                    temp_path = temp_file.name
                images = convert_from_path(temp_path)

                # Extraer texto de cada página
                texto_extraido = ""
                for i, page in enumerate(images):
                    texto_extraido += pytesseract.image_to_string(page) + "\n"
            else:
                # Leer imagen directamente
                imagen = Image.open(archivo)
                texto_extraido = pytesseract.image_to_string(imagen)

            # Mostrar el texto extraído
            st.subheader("Texto extraído:")
            st.text_area("Contenido del documento", texto_extraido, height=300)
else:
    st.write("No has seleccionado ningún archivo.")

