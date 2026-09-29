import gspread
from google.oauth2.service_account import Credentials
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_sheet():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets"
    ]

    credentials = Credentials.from_service_account_file(
    os.path.join(BASE_DIR, "credentials.json"),
    scopes=scopes
    )
    
    client = gspread.authorize(credentials)

    spreadsheet = client.open_by_key("1SEI07-pk5nBh_tMfeihgWHubfi1GGSj2MtfvafRyWwg")
    sheet = spreadsheet.worksheet("Form responses 1")

    return sheet