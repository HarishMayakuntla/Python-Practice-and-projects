## ============================ Open CSV file using Python =========================


## using csvmodule

import csv

with open("students.csv", "r") as file:
    data = csv.reader(file)

    for row in data:
        print(row)


## output :

['name', 'age', 'marks']
['Harish', '21', '85']
['Rohith', '22', '90']
['Kumar', '20', '78']

## Read CSV as dictionary

import csv

with open("students.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        print(row)

## output:

{'name': 'Harish', 'age': '21', 'marks': '85'}
{'name': 'Rohith', 'age': '22', 'marks': '90'}
{'name': 'Kumar', 'age': '20', 'marks': '78'}

