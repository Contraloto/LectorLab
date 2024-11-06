import streamlit as st
import PyPDF2

def extraer_texto_pdf(ruta_archivo):
    with open(ruta_archivo, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        texto_completo = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            texto_completo += page.extract_text()
        return texto_completo

def main():
    st.title("Extractor de Texto de PDF")

    # Botón para seleccionar el archivo
    uploaded_file = st.file_uploader("Selecciona un archivo PDF", type="pdf")

    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        with open("temp.pdf", "wb") as out:
            out.write(bytes_data)

        # Extraer el texto y mostrarlo en la interfaz
        texto = extraer_texto_pdf("temp.pdf")
        st.text_area("Texto extraído:", texto)

if __name__ == "__main__":
    main()