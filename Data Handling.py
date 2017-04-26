# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:32:08 2017

@author: user
"""

import csv
from matplotlib import pyplot

#Raw data
data = []
#1. Using Bernie's data logging confirm the csv method of aquiring data
#Open the storage from the database in form of csv to get data for a particular batch
with open('storage.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for cnt, row in enumerate(csvreader):
        if cnt == 0:
            headings = row
        else:
            data.append(row)
         
print headings, data

#Getting lists from matrix
vals_per_batch = data[:,1]
time_stamp = data[:,1]    

#Assume data changing over time for a particular batch so single value required per batch
#Plot to see visually change in values
#2. Determine standard for what is acceptable or not when analysing slope of data

pyplot.figure(1)
pyplot.plot(time_stamp, vals_per_batch, 'g-', label = 'values per batch')
pyplot.legend()
pyplot.show(1)

#Finding average value of data during the batch
av_value = sum(vals_per_batch)/len(vals_per_batch)   

#Creating a list that can be used in SPC file
batch_list = []
value_mlist = []

value_mlist.append(av_value)

length_data = len(value_mlist)

for i in range(1, length_data + 1):
    batch_list.append(i)
    
print batch_list, value_mlist
    
#Fixing list for for possible errors only when necessary
    
#change_val = input('Value Change: ')
#change_batch = input('Batch Number')
#
#value_mlist[change_batch - 1] = change_val
    
#Comment out import code and averaging code when making changes  and uncomment error code
    
#3. Create functions within the same file to avoid repeating code when trying to fix
#   code so as to avoid commenting and uncommenting
    
#4. Sort out how to get lists to SPC file
    
#5. Recipe number should be incorporated into the code for recipe comparison


    



















        
        
    



            
   