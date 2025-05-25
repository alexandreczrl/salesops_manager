import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def load_data(sheet_name):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("1fFjvk0X6vvvM7ZEBfF03yGpNEQhzL1IkM2YrAxJCc70")
    worksheet = sheet.worksheet(sheet_name)
    data = worksheet.get_all_records()
    return pd.DataFrame(data)
