import gspread
from oauth2client.service_account import ServiceAccountCredentials

def writer():
    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    client = gspread.authorize(credentials=creds)

    sheet = client.open("Validations").sheet1

    return sheet
