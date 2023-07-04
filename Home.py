import streamlit as st
from PIL import Image

def main():
    st.write("# Rinha de Sedentários!!!")
    st.write("## Quem ganhará esse tão esperado rodízio?")
    # Carrega as imagens
    foto_deny = Image.open("img/foto-deny.PNG")
    foto_fabricia = Image.open("img/foto-fabricia.jpg")

    # Redimensiona as imagens para exibição
    foto_deny = foto_deny.resize((600, 300))
    foto_fabricia = foto_fabricia.resize((600, 300))

    # Exibe as imagens
    st.image([foto_deny, foto_fabricia], caption=["Competidor Deny", "Competidora Fabrícia"], width=600)

if __name__ == "__main__":
    main()

