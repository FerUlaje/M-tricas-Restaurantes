import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Métricas :red[*DeLeña*] y :red[*Arracház*]')

metrica = st.radio("Selecciona el indicador:", 
                   ["Redes Sociales", "**Plataformas Delivery**"],
                   captions=["Seguidores, Indicadores de Campañas, Comparativas.",
                             "Top Uber Eats."])

if metrica == "Redes Sociales":
    st.write("Seguidores")