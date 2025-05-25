import gspread
import pandas as pd
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

def load_data(sheet_name):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds_dict = st.secrets["credentials"]  # ✅ NE PAS UTILISER json.loads
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key("1fFjvk0X6vvvM7ZEBfF03yGpNEQhzL1IkM2YrAxJCc70")  # 👈 Ton ID de Google Sheet
    worksheet = sheet.worksheet(sheet_name)
    data = worksheet.get_all_records()

    return pd.DataFrame(data)
