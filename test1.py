import csv
csv_file="tests/data/example_one.csv"
data=[]
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if row:
            data.append(row)
print(data)