import os
import csv
import json
import argparse

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Function to load the configuration from the specified file
def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

# Command-line argument parsing
parser = argparse.ArgumentParser(description='Google Sheets API Quickstart')
parser.add_argument('config_file', help='Path to the configuration JSON file')
args = parser.parse_args()

# Load configuration
config = load_config(args.config_file)

SCOPES = config["SCOPES"]
SAMPLE_SPREADSHEET_ID = config["SPREADSHEET_ID"]
SAMPLE_RANGE_NAME = config["SAMPLE_RANGE_NAME"]
UPDATE_RANGE = config["UPDATE_RANGE"]
CLEAR_RANGE = config["CLEAR_RANGE"]

# Used for creating/updating new values
body = {
    'values': [
        ["update"]  # Data to write to the cells
    ]
}

# Used for deletion
clear_body = {
    'values': [[""]]  # Adjust as needed
}

def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Ensure the credentials file path is not hard-coded
            creds_file = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'credentials.json')
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_file, SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        print("Data found")

        with open('output.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(values)

        # Looping through the sheet
        for row in values:
            # Print columns A and C, which correspond to indices 0 and 2.
            col_a = row[0] if len(row) > 0 else "No data"
            col_c = row[2] if len(row) > 2 else "No data"
            print(f"{col_a}, {col_c}")

        # Adding values to the sheet
        update_result = sheet.values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=UPDATE_RANGE,
            valueInputOption="RAW",
            body=body
        ).execute()
        print(f"{update_result.get('updatedCells')} cells updated.")

        # Deleting values from the sheet
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=CLEAR_RANGE,
            valueInputOption="RAW",
            body=clear_body
        ).execute()
        print(f"Cleared {result.get('updatedCells')} cells.")

    except HttpError as err:
        print(err)

if __name__ == "__main__":
    main()