import streamlit as st
import pandas as pd
from sheets_connector import load_data

st.set_page_config(page_title="SalesOps Manager – Start.io 2025", layout="wide")

st.title("📊 SalesOps Manager – Start.io 2025")

tab1, tab2, tab3 = st.tabs(["Prospects", "Consultants", "Candidats"])

with tab1:
    st.header("🧲 Prospects")
    df = load_data("Prospects")
    st.dataframe(df)

with tab2:
    st.header("🧠 Consultants")
    df = load_data("Consultants")
    st.dataframe(df)

with tab3:
    st.header("👤 Candidats")
    df = load_data("Candidats")
    st.dataframe(df)
