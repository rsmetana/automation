import csv
with open('air.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]
    print(year_1958)

    max_1958 = max(year_1958.values())

    #for row in reader:
     #   print(row)