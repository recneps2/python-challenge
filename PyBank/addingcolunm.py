import os
import csv

data_file = os.path.join('Resources', 'budget_data.csv')
#print('Financial Analysis')
#print('--------------------------------')

"""with open(data_file, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    print(header)
    firstMrow = next(reader)
    #secondMrow = next(reader)
    #print(firstMrow)
    #print(secondMrow)
    all = []
    header.append('Chng from Prev Month')
    all.append(firstMrow)
    print(header)
    #curMpl = int(row[2])
    #print(curMpl)
    #nxtMpl = int(first_row[1])
   
    for row in reader:
        #print(row[1])
        row.append(row[1])
        all.append(row)
        print(row[2])"""
    
"""months = 0
for row in reader
    months ="""

    #2.3 activity udemy
    #2.4 wrestling activity
    #2.3 house of py

    #stat w total months, count
#lists to store data
date = []
curMpl = []
prevMpl = []
momPLcng = []

with open(data_file, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    for row in reader:
         #add dates
         date.append(row[0])

         #add current month
         curMpl.append(int(row[1]))

         #add prev month
         prevMpl.append(int(row[1]))

#print(date)
#print(curMpl)

prevMpl.pop(0)
prevMpl.append(0)
#print(prevMpl)

for i in range(len(date)):
    momPLcng.append(int(prevMpl[i]) - (curMpl[i]))
#print(momPLcng)
#print(len(date))

totmonths = len(date)
totalpl = sum(curMpl)
avemomplcng = sum(momPLcng)/totmonths
maxval = max(momPLcng)
maxvalindex = momPLcng.index(maxval)
maxvaldate = date[maxvalindex]

minval = min(momPLcng)
minvalindex = momPLcng.index(minval)
minvaldate = date[minvalindex]

print('Financial Analysis')
print('--------------------------------')
print(f'Total Months: {totmonths}')
print(f'Total: ${totalpl}')
print(f'Average Change: ${avemomplcng}')
print(f'Greatest Increase in Profits: {maxvaldate} ${maxval}')
print(f'Greatest deacrease in Profits: {minvaldate} ${minval}')

txtfile = open('PyBankoutput.txt', 'w+')
txtfile.write('Financial Analysis\n')
txtfile.write('--------------------------------\n')
txtfile.write(f'Total Months: {totmonths}\n')
txtfile.write(f'Total: ${totalpl}\n')
txtfile.write(f'Average Change: ${avemomplcng}\n')
txtfile.write(f'Greatest Increase in Profits: {maxvaldate} ${maxval}\n')
txtfile.write(f'Greatest Decrease in Profits: {minvaldate} ${minval}\n')
txtfile.close
