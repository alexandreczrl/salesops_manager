import streamlit as st
import pandas as pd
from sheets_connector import load_data

# Configuration de la page
st.set_page_config(page_title="SalesOps Manager – Prospects", layout="wide")

# Titre principal
st.title("📊 Dashboard des Prospects – SalesOps Manager")

# Chargement des données depuis Google Sheets
try:
    df = load_data("Prospects")  # 👉 Mets ici le nom EXACT de l’onglet de ton Google Sheet

    # Affichage du tableau de données
    st.subheader("Liste des prospects")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("❌ Erreur lors du chargement des données :")
    st.exception(e)
