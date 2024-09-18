import csv

#open file and read 
steps=open('steps.csv','r')
csv_file= csv.reader(steps)

next(csv_file)

#create empty list for each month
January=[]
February=[]
March=[]
April=[]
May=[]
June=[]
July=[]
August=[]
September=[]
October=[]
November=[]
December=[]

#for loop
for line in csv_file:
    month=int(line[0])
    step=int(line[1])

    if month ==1:
        January.append(step)
    elif month == 2:
        February.append(step)
    elif month == 3:
        March.append(step)
    elif month == 4:
        April.append(step)
    elif month == 5:
        May.append(step)
    elif month == 6:
        June.append(step)
    elif month == 7:
        July.append(step)
    elif month == 8:
        August.append(step)
    elif month == 9:
        September.append(step)
    elif month == 10:
        October.append(step)
    elif month == 11:
        November.append(step)
    elif month == 12:
        December.append(step)

#calculate average per month
def avgsteps (month_name,steps):
    if steps:
        avgsteps= sum(steps)/len(steps)

    else:
        avgsteps=0
    print(f"{month_name} {avgsteps:.2f}")

#displaying with print function
avgsteps("January - ", January)
avgsteps("February - ", February)
avgsteps("March - ", March)
avgsteps("April - ", April)
avgsteps("May - ", May)
avgsteps("June - ", June)
avgsteps("July - ", July)
avgsteps("August - ", August)
avgsteps("September - ", September)
avgsteps("October - ", October)
avgsteps("November - ", November)
avgsteps("December - ", December)

