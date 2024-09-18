import csv

infile = open('customers.csv', 'r')

csv_obj = csv.reader(infile)


header = next(csv_obj) #this skips the first row

#print(header)

for rec in csv_obj:
    print(rec) #list, need index values for list, start at 0
    print(f"First Name: {rec [1]}")
    print(f"Last Name: {rec [2]}")

    input() #pauses the code after iteration (row)
