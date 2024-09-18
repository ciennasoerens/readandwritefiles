import csv

#reads the file
infile = open('customers.csv', 'r') 
csv_obj = csv.reader(infile, delimiter = ',')
header= next(csv_obj)

#creates new file
outfile= open('customer_country.csv', 'w')
outfile.write("Full Name, Country \n")

count = 0

#include name and country
for rec in csv_obj:
   outfile.write(f"{rec[1]} {rec[2]},{rec[4]}\n")
   count += 1

#displaying total count
outfile.write(f"Total Customers: {count}")

infile.close
outfile.close

