import serial
import time
import re
import subprocess
import sys
import datetime
import gspread
# ===========================================================================
# Google Account Details
# ===========================================================================

# Account details for google docs
email       = 'rpidetalist@rpidatelist.iam.gserviceaccount.com'
password    = ''
spreadsheet = 'rpigdlist'

# ===========================================================================
# Example Code
# ===========================================================================


# Login with your Google account
try:
  gc = gspread.login(email, password)
except:
  print "Unable to log in.  Check your email address/password"
  sys.exit()

# Open a worksheet from your spreadsheet using the filename
try:
  worksheet = gc.open(spreadsheet).sheet1
  # Alternatively, open a spreadsheet using the spreadsheet's key
  # worksheet = gc.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')
except:
  print "Unable to open the spreadsheet.  Check your filename: %s" % spreadsheet
  sys.exit()


# Set Channel 
ser = serial.Serial('/dev/ttyACM0', 9600)

# buffer clear
start_time = time.time()
while 1 :
    output = ser.readline()
    print output
    
    if time.time() - start_time > 15:
     print time.time() - start_time
     break

# Reading sensor data
while 1 :
    output = ser.readline()
    match = re.search("sensor\:\s(\w+)", output)
    if match:
        status = match.group(1)
#        print match.group(1)
        continue
        
    match = re.search("Humidity\s\(\%\)\:\s(\d+)", output)
    if match:
        Humidity = float(match.group(1))
#        print "Humidity:",Humidity
        continue
    
    match = re.search("Temperature\s\(oC\)\:\s(\d+)", output)
    if match:
        TempC = float(match.group(1))
#       print "Temp:", float(match.group(1)),"oC"
        continue

    match = re.search("Temperature\s\(oF\)\:\s(\d+)", output)    
    if match:
        TempF = float(match.group(1))
#        print "Temp:", float(match.group(1)),"oF"
        continue   
    
    match = re.search("Temperature\s\(K\)\:\s(\d+)", output)    
    if match:
        TempK = float(match.group(1))
#        print "Temp:", float(match.group(1)),"K"
        continue  
    
    match = re.search("Dew\sPoint\s\(oC\)\:\s(\d+)", output)    
    if match:
        Dew = float(match.group(1))
#        print "Dew:", float(match.group(1)),"oC"
        continue  
    
    match = re.search("Dew\sPointFast\s\(oC\)\:\s(\d+)", output)    
    if match:
        DewFast = float(match.group(1))
#        print "Dew PointFast:", float(match.group(1)),"oC"
    else:
        continue
# Insert data    
    try:
        values = [datetime.datetime.now(), status, Humidity, TempC, TempF, TempK, Dew, DewFast]
        worksheet.append_row(values)
    except:
        print "Unable to append data.  Check your connection?"
        sys.exit()
    
#    print status, Humidity, TempC, TempF, TempK, Dew, DewFast
    time.sleep(0.5)