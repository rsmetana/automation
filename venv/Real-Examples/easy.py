import csv
import sys
with open('monswt.csv') as data:
    ip_list = csv.reader(data)
    for row in ip_list:
        site = row[0]
        closet = row[6]
print(f"{site}")

