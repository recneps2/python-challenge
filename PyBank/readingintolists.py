import os
import csv

data_file = os.path.join('Resources', 'budget_data.csv')
print('Financial Analysis')
print('--------------------------------')

with open(data_file, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    first_row = next(reader)
    total_months += 1
    total_net = int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        # track the total months 
        total_months += 1
        total_net +=int(row[1])
        
        #track the net change
        net_chng = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_chng_list += [net_chng]
        month_of_chng += [row[0]]
        
        # calc the greatest increase
        if net_chng > greatest_increase[1]:
            greatest_increase [0] = row[0]
            greatest_increase [1] = net_chng

        # calculate the greatest decrease
        if net_chng < greatest_deacrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_chng
