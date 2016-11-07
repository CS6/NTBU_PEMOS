import csv
import datetime
from datetime import datetime
from time import strftime

data = [['1', '2', '3', '4', '5', '6'], ['2', '3', '4', '5', '6', '7']]
fileDT = datetime.now().strftime('%Y%m%d_%H%M%S')
f = open(fileDT + ".csv", "w")
w = csv.writer(f)
w.writerows(data)
f.close()