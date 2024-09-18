import csv

#reads employee data
infile= open('employee_data.csv', 'r')
csv_obj= csv.reader(infile)
next(csv_obj)

for rec in csv_obj:
    name = rec[1]
    salary = int(rec[3])
    bonus_percentage= float(rec[7])
    bonus_pay= bonus_percentage*salary
    pay=salary + (salary*bonus_percentage)

#prints detail of each employee with calculations
    print(f"\nName: {name}")
    print(f"Salary: $ {salary:9,.2f}")
    print(f"Bonus: $ {bonus_pay:9,.2f}")
    print(f"Pay: $ {pay:9,.2f}\n")