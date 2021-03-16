#Write a Python program to read specific columns of a given CSV file and print the content
of the columns
import csv
with open('D:\depart.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   print(row['department_id'],row['department_name'])
