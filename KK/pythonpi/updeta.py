import gspread

# Login with your Google account
gc = gspread.login('sduum82@gmail.com', '22476103')

# Open a worksheet from spreadsheet with one shot
wks = gc.open("https://docs.google.com/spreadsheets/d/1VTBT4a607jucISoMhvGQOSUipgMhKrNK4eFVS6olvgY/edit#gid=0").sheet1

wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
cell_list = wks.range('A1:B7')