# python code goes here
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figure from the user
    """
    print("please enter sales data from the last market")
    print("data should be six numbers, separated by commas")
    print("Example: 10, 20, 30, 40, 50, 60 \n")

    data_str = input("Enter your data here:")
    sales_data = data_str.split(",")
    
    validate_data(sales_data)

def validate_data(values):
    """
    Raise error if strings cannot be converted in integer
    or we dont have exactly 6 values
    """
    try:
        if len(values) != 6:
            raise ValueError(
        f"Exactly 6 values required, you provided {len(values)}"
        )
    except ValueError as e:
        print(f"Invalid data {e}, please retry.")


get_sales_data()