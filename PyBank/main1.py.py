#!/usr/bin/env python
# coding: utf-8

# In[109]:


# Dependencies
import pandas as pd


# In[110]:


# Save path to data set in a variable
data_file = "Resources/budget_data.csv"


# In[111]:


# Use Pandas to read data
data_file_df = pd.read_csv(data_file)


# In[112]:


# formatting prefrences
print('Financial Analysis')
print('---------------------------')


# In[113]:


# Home work ask 1: The total number of months included in the dataset
# The count method counts every entry in the series
totalmonths = data_file_df["Date"].count()
print(f'Total Months: {totalmonths}')


# In[114]:


# Home work ask 2: The net total amount of "Profit/Losses" over the entire period
# The sum method adds every entry in the series
totalpl = data_file_df["Profit/Losses"].sum()
print(f'Total: ${totalpl}')


# In[115]:


# Home work ask 3: The average of the changes in "Profit/Losses" over the entire period
# in other words, I need to find the average of all month over month changes in "Profit/Losses"


# In[116]:


# step 1: I need to get the month over month change so creat new column with "Profit/Losses" shifted up by 1 row
previous_month = data_file_df["Profit/Losses"].shift(1)
data_file_df["Previous Month's P/L"] = previous_month


# In[117]:


# step 2: subtract "Profit/Losses" from "Following months P/L"
momchng = data_file_df["Profit/Losses"] - data_file_df["Previous Month's P/L"] 
data_file_df["Month over Month P/L Change"] = momchng


# In[118]:


#step 3: take the averave of the column "Month over Month P/l Change"
# The mean method averages the series
average = data_file_df["Month over Month P/L Change"].mean()
print(f'Average Change: ${average}')


# In[ ]:





# In[122]:


#Homework ask 4: The greatest increase in profits (date and amount) over the entire period
maxup = data_file_df["Month over Month P/L Change"].max()

maxup_date = data_file_df.loc[data_file_df["Month over Month P/L Change"] == maxup, 'Date'].iloc[0]
print(f'Greatest Increase in Profits: {maxup_date} ${maxup}\n')


# In[120]:


# Homework ask 5: The greatest decrease in losses (date and amount) over the entire period
maxdown = data_file_df["Month over Month P/L Change"].min()

maxdown_date = data_file_df.loc[data_file_df["Month over Month P/L Change"] == maxdown, 'Date'].iloc[0]
print(f'Greatest Decrease in Profits: {maxdown_date} ${maxdown}\n')


# In[125]:


txtfile = open('PyBank.txt', 'w+')
txtfile.write('Financial Analysis\n')
txtfile.write('-----------------------------\n')
txtfile.write(f'Total Months: {totalmonths}\n')
txtfile.write(f'Total: ${totalpl}\n')
txtfile.write(f'Average Change: ${average}\n')
txtfile.write('Greatest Increase in Profits: ')
txtfile.write(f' {maxup_date} ${maxup}\n')
txtfile.write('Greatest Decrease in Profits: ')
txtfile.write(f' {maxdown_date} ${maxdown}\n')
txtfile.close()


# In[ ]:




