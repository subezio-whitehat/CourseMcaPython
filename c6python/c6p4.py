import csv
with open('D:\depart.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   print(row['department_id'],row['department_name'])