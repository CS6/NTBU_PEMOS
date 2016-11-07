import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://docs.google.com/spreadsheets/d/1VTBT4a607jucISoMhvGQOSUipgMhKrNK4eFVS6olvgY/edit?usp=sharing']

credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread-april-2cd … ba4.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Where is the money Lebowski?").sheet1