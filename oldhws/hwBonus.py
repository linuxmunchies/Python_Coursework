import csv

# Import everything that is needed. In this case, the CSV file. Split and store in a list variable.
with open('employee_database.csv') as csvFile:
    records = []
    for line in csv.reader(csvFile, delimiter=','):
        records.append(line)

# Find amount of unique departments, and store them in a new list.
departList = []

for iterOne in range(len(records)):
    if records[iterOne][3] == "Department ID":
        pass
    elif records[iterOne][3] in departList:
        pass
    else:
        departList.append(records[iterOne][3])

print(f"There are {len(departList)} departments in this company.\n\n***LIST OF DEPARTMENTS***")

for department in departList:
    print(f"{department}")

# Create a separate list for each department...
departDict = {}
for departmentNumber in range(len(departList)):
    departDict[f"Dep {departmentNumber}"] = departList[departmentNumber]
print(departDict)