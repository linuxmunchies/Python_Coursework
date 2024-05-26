import csv

# Open file and use delimiter to read into a dictionary. Then store results in csvList.
with open("employee_database.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    csvList = []
    for row in reader:
        csvList.append(row)

# Get list of departments
departList = []
for x in range(len(csvList)):
    if csvList[x]["Department ID"] not in departList:
        departList.append(csvList[x]["Department ID"])
    elif csvList[x]["Department ID"] in departList:
        pass
    else:
        print("An error has occured.")
        quit()

# Initialize both salary and worker lists to proper amount of indexes
salaryList = [0 for x in departList]
workerAmountList = [0 for x in departList]

# Create a highest salary and HSIndex variable to store the X VALUE (Department #) of the highest salary worker
highestSalary = 0
hSIndex = 0

# Create the same variables, but for the lowest index.
lowestSalary = 0
lSIndex = 0

# Create variable for brackete
sevNinBracket = 0

# Get total salary amounts  as well as number of employees per department, highestSal, LowestSal,
# and number of employees within 70000 and 90000 salary bracket.
for x in range(len(csvList)):
    for y in range(len(departList)):
        if x == 0 and departList[y] == csvList[x]["Department ID"]:
            salaryList[y] = int(csvList[x]["Salary"])
            workerAmountList[y] = 1
            # Assign initial values for highest and lowest.
            highestSalary = int(csvList[x]["Salary"])
            lowestSalary = int(csvList[x]["Salary"])
            # Check if they are within the bracket
            if int(csvList[x]["Salary"]) > 70000 and int(csvList[x]["Salary"]) < 90000:
                sevNinBracket = 1
            break
        elif departList[y] == csvList[x]["Department ID"]:
            salaryList[y] += int(csvList[x]["Salary"])
            workerAmountList[y] += 1
            # Check if this worker's salary is higher than the previous highest
            if highestSalary > int(csvList[x]["Salary"]):
                pass
            elif highestSalary < int(csvList[x]["Salary"]):
                highestSalary = int(csvList[x]["Salary"])
                hSIndex = x
            # Now do the same for the lowest salary
            if lowestSalary < int(csvList[x]["Salary"]):
                pass
            elif lowestSalary > int(csvList[x]["Salary"]):
                lowestSalary = int(csvList[x]["Salary"])
                lSIndex = x
            # Check for salary bracket
            if int(csvList[x]["Salary"]) > 70000 and int(csvList[x]["Salary"]) < 90000:
                sevNinBracket += 1
            break
        else:
            pass

# Find how many unique salaries exist in the company
uniqueSals = []
for x in range(len(csvList)):
    if x == 0:
        uniqueSals.append(csvList[x]["Salary"])
    elif csvList[x]["Salary"] in uniqueSals:
        pass
    elif csvList[x]["Salary"] not in uniqueSals:
        uniqueSals.append(csvList[x]["Salary"])
    else:
        print("Something has gone wrong! ERR:Unique Salaries.")

#!!! We will calculate the total number of unique salaries in the print statement.

# Test statements for debugging
# print(departList)
# print(salaryList)
# print(workerAmountList)
# print(highestSalary)
# print(hSIndex)
# print(csvList[hSIndex]["Department ID"])
# print(lowestSalary)
# print(lSIndex)
# print(csvList[lSIndex]["Department ID"])
# print(f"Highest salary Dep: {departList[salaryList.index(max(salaryList))]} at ${max(salaryList)}")
# print(sevNinBracket)
# print(uniqueSals)

# PRINT FINAL RESULTS

print("\n| Data Analyze Section |")
print(f"The Company has {len(departList)} departments.")
print(f"Highest Salary: ${highestSalary} in {csvList[hSIndex]['Department ID']}")
print(f"Lowest Salary: ${lowestSalary} in {csvList[lSIndex]['Department ID']}")
print(f"Highest Budget Department: {departList[salaryList.index(max(salaryList))]} at ${max(salaryList)}")
print(f"The Company has {len(departList)} departments.")
print(f"There are {sevNinBracket} within the specified pay bracket. (70000 > x < 90000)")
print(f"There are {len(uniqueSals)} unique salaries.\n")
for y in range(len(departList)):
    print(f"| {departList[y]} |")
    print(f"Total Employees: {workerAmountList[y]}\nBudget: ${salaryList[y]}\n")
