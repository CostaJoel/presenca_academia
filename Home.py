import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime
import os

def main():
    st.set_page_config(page_title="Rinha de Sedentários", page_icon="💪", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.write("<h1 style='text-align: center;'>Rinha de Sedentários!!! 💪</h1>", unsafe_allow_html=True)
    st.write("<h3 style='text-align: center;'>Quem ganhará esse tão esperado rodízio? 🍣🍤🍙", unsafe_allow_html=True)
    # Carrega as imagens
    foto_deny = Image.open("img/foto-deny.PNG")
    foto_fabricia = Image.open("img/foto-fabricia.jpg")

    # Redimensiona as imagens para exibição
    foto_deny = foto_deny.resize((400, 600))
    foto_fabricia = foto_fabricia.resize((400, 600))

    # Exibe as imagens
    col1, col2, col3 = st.columns([2,1,2])
    with col1:
        carrega_placar("Fabrícia")
        col1.image(foto_fabricia, caption="Competidora Fabrícia", width=400)
        button_clicked = col1.button("Marcar presença Fabrícia")
        if button_clicked:
            marca_presenca("Fabrícia")

    col2.write()
    with col3:
        carrega_placar("Deny")
        col3.image(foto_deny, caption="Competidora Deny", width=400)
        button_clicked = col3.button("Marcar presença Deny")
        if button_clicked:
            marca_presenca("Deny")

def marca_presenca(particicpante):
    if os.path.exists('database.xlsx'):
        df = pd.read_excel("database.xlsx")
        df = df[['participante', 'timestamp_presenca']]
    else:
        df = pd.DataFrame(columns=['participante', 'timestamp_presenca'])
    
    # Obter a data atual
    data_atual = datetime.now().date()

    # Verificar se a marcação já foi feita hoje
    marcação_hoje = df.loc[df.participante == particicpante, 'timestamp_presenca'].apply(lambda x: x.date() == data_atual).any()
    if marcação_hoje:
        st.error(f"{particicpante} você já marcou presença hoje! Está tentando roubar?", icon="🐀")
    else:
        novo_registro = pd.DataFrame({'participante': [particicpante],
                                      'timestamp_presenca': [data_atual]})
        df = pd.concat([df, novo_registro], axis=0, ignore_index=True)
        df.to_excel("database.xlsx", index=False)
        st.success(f"Presença registrada com sucesso! {particicpante} você está mais próxima do seu rodízio", icon="💪")
    pass

def carrega_placar(participante):
    if os.path.exists('database.xlsx'):
        df = pd.read_excel("database.xlsx")
    else:
        st.metric(label=participante, value="0 pontos")
    
    pontos = df.loc[df.participante == participante].shape[0]
    st.metric(label=participante, value=f"{pontos} pontos")

if __name__ == "__main__":
    main()

