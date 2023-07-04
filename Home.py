import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime
import os

def main():
    st.write("# Rinha de Sedentários!!!")
    st.write("## Quem ganhará esse tão esperado rodízio?")
    # Carrega as imagens
    foto_deny = Image.open("img/foto-deny.PNG")
    foto_fabricia = Image.open("img/foto-fabricia.jpg")

    # Redimensiona as imagens para exibição
    foto_deny = foto_deny.resize((400, 600))
    foto_fabricia = foto_fabricia.resize((400, 600))


    # Exibe as imagens
    col1, col2, col3 = st.columns([2,1,2])
    with col1:
        col1.image(foto_fabricia, caption="Competidora Fabrícia", width=400)
        button_clicked = col1.button("Marcar presença Fabrícia")
        if button_clicked:
            marca_presenca("Fabrícia")


    col2.write()
    with col3:
        col3.image(foto_deny, caption="Competidora Deny", width=400)
        button_clicked = col3.button("Marcar presença Deny")
        if button_clicked:
            marca_presenca("Deny")

def marca_presenca(particicpante):
    if os.path.exists('database.xlsx'):
        df = pd.read_excel("database.xlsx")
    else:
        df = pd.DataFrame(columns=['participante', 'timestamp_presenca'])
    
    # Obter a data atual
    data_atual = datetime.now().date()

    # Verificar se a marcação já foi feita hoje
    marcação_hoje = df.loc[df.participante == particicpante, 'timestamp_presenca'].apply(lambda x: x.date() == data_atual).any()
    if marcação_hoje:
        st.error(f"{particicpante} você já marcou presença hoje! Está tentando roubar?")
    else:
        novo_registro = pd.DataFrame({'participante': [particicpante],
                                      'timestamp_presenca': [data_atual]})
        df = pd.concat([df, novo_registro], axis=0, ignore_index=True)
        df.to_excel("database.xlsx")
        st.success(f"Presença registrada com sucesso! {particicpante} você está mais próxima do seu rodízio")
    pass

if __name__ == "__main__":
    main()

