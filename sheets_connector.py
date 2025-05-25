import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def load_data(sheet_name):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    
    # ✅ Vérification de la connexion
    print("✅ Connexion réussie avec :", creds.service_account_email)

    client = gspread.authorize(creds)
    
    # Ouverture de la feuille par son identifiant
    sheet = client.open_by_key("1fFjvk0X6vvvM7ZEBfF03yGpNEQhzL1IkM2YrAxJCc70").worksheet(sheet_name)
    
    # Récupération des données
    data = sheet.get_all_records()
    return pd.DataFrame(data)
