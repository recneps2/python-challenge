import os
import csv

data_file = os.path.join('Resources', 'budget_data.csv')

#defining veriables
date = [] #column 1, date of pl
curMpl = [] #column 2, p/l of listed month
prevMpl = [] #new list, previous month's p/l, needed to get month over month change
momPLcng = [] #new list, month over month change for each line item

#open/read csv and add content to lists
with open(data_file, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    for row in reader:
         #add dates
         date.append(row[0])

         #add current month
         curMpl.append(int(row[1]))

         #add additional current month list to use as "previous month's PL"
         prevMpl.append(int(row[1]))

#removing the first value from the list of previous month pl valuse
prevMpl.pop(0)
#adding a 0 to the end of the list to make it the same length as the other lists
prevMpl.append(0)

#addting content to list of month over month changes
for i in range(len(date)):
    momPLcng.append(int(prevMpl[i]) - int(curMpl[i]))
momPLcng.pop()


totmonths = len(date) #total number of records, excluding headers
totalpl = sum(curMpl) #sum of total profit and llosses
totalmomplcng = sum(momPLcng) #sum of total month over month changes in profit and losses
avemomplcng = round(totalmomplcng/len(momPLcng),2) #average month over month change of profit and losses
maxval = max(momPLcng) #value of greatest increase in profit and losses
maxvalindex = momPLcng.index(maxval) #index of greatest increase in profit and losses
maxvaldate = date[maxvalindex] #date of the greatest increase in profit and losses
minval = min(momPLcng) #value of greatest decrease in profit and losses
minvalindex = momPLcng.index(minval) #index of greatest decrease in profit and losses
minvaldate = date[minvalindex] #date of the greatest decrease in profit and losses

#printing to terminal
print('Financial Analysis')
print('--------------------------------')
print(f'Total Months: {totmonths}')
print(f'Total: ${totalpl}')
print(f'Average Change: ${avemomplcng}')
print(f'Greatest Increase in Profits: {maxvaldate} ${maxval}')
print(f'Greatest deacrease in Profits: {minvaldate} ${minval}')

#writing to txt file
txtfile = open('PyBankoutput.txt', 'w+')
txtfile.write('Financial Analysis\n')
txtfile.write('--------------------------------\n')
txtfile.write(f'Total Months: {totmonths}\n')
txtfile.write(f'Total: ${totalpl}\n')
txtfile.write(f'Average Change: ${avemomplcng}\n')
txtfile.write(f'Greatest Increase in Profits: {maxvaldate} ${maxval}\n')
txtfile.write(f'Greatest Decrease in Profits: {minvaldate} ${minval}\n')
txtfile.close
