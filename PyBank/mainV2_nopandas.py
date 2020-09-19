import os
import csv

data_file = os.path.join('Resources', 'budget_data.csv')
print('Financial Analysis')
print('--------------------------------')

with open(data_file, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)
    data = list(reader)
    #print(data)
    months = len(data)
    print(f'Total Months: {months}')

"""for i in range(len(data)):
    print(i, end = " ")
    print(data[i])"""
    

net = []
for row in data:
    net.append(int(row[1]))
print(f'Total: ${sum(net)}')

Changes = 0
#print(Changes)
for i in range(1,len(data)):
    #print(int(data[i][1]))
    dif = int(data[i][1]) - int(data[i-1][1])
    #print(dif)
    Changes += dif
    #print(Changes)
avecng = Changes/(len(data)-1)
avecng_form = "${:,.2f}".format(avecng)
print(f'Average Change: {avecng_form}')


"""increase = [0,0]
current_row = 0
for row in data:
    bigup_row_val = max(row)
    bigup_row_indx = row.index(bigup_row_val)
    if bigup_row_val > data[increase[0]][increase[1]]:
        increase = (current_row,bigup_row_indx)
    current_row += 1
print(increase)"""


