# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 06:24:23 2017

@author: user
"""

from matplotlib import pyplot
from Auxiliary_File import data_aquis

#Data set from Data_Handling_2

#1. Improve return from csv file in order to call correct data correctly e.g for time stamp and vals_per_batch
#    Maybe do a raw input line for file name

file_name = 'storage.csv'    
data = data_aquis(file_name)

#Assume data changing over time for a particular batch so single value required per batch
#Plot to see visually change in values

#2. Determine standard for what is acceptable or not when analysing slope of data

time_stamp = data[1]
vals_per_batch = data[2]

pyplot.figure(1)
pyplot.plot(time_stamp, vals_per_batch, 'g-', label = 'values per batch')
pyplot.legend()
pyplot.show(1)

#Finding average value of data during the batch

av_value = sum(vals_per_batch)/len(vals_per_batch) 

#Creating a list that can be used in SPC 

batch_list = []
value_mlist = []
value_rlist = []

value_mlist.append(av_value)

length_data = len(value_mlist)

for i in range(1, length_data + 1):
    batch_list.append(i)
    
#Parameters
sample  =  4
A_2 = 0.73
two_thirds_A2 = 0.49
D1_1 = 2.57
D1_25 = 1.93

#2. Fix the SPC method to improve return of results i.e plot from 4th batch for moving range and moving mean 
#   chart
#3. Individual chart for first 3 batches in order to start getting a graph instead
#   of waiting for four batches. Can use else statement

if batch_list[-1] >= sample:   #Only starts plotting if more than 4 batches
    
    #Calculate mean and range from previous 4 batches
    values_4 = []
    for j in range(-1, -5, -1):
        values_4.append(value_mlist[j])
        
    print values_4

    value_mean = sum(values_4)/batch_list[-1]
    value_range = max(values_4)-min(values_4)
            
    value_rlist.append(value_range)
    
    #Mean and range lines for graphs
    value_mean_list  = []
    value_range_list = []
    for i in range(1, batch_list[-1] + 1):
        value_mean_list.append(value_mean)
        value_range_list.append(value_range)
      
    #Mean Chart limits
    UAL_mean_list = []
    UWL_mean_list = []
    LWL_mean_list = []
    LAL_mean_list = []   
    
    UAL_mean = value_mean + A_2*value_range
    UWL_mean = value_mean + two_thirds_A2*value_range
    LWL_mean = value_mean - two_thirds_A2*value_range
    LAL_mean = value_mean - A_2*value_range 
    
    
    for i in range(1, batch_list[-1] + 1):
        UAL_mean_list.append(UAL_mean)
        UWL_mean_list.append(UWL_mean)
        LWL_mean_list.append(LWL_mean)
        LAL_mean_list.append(LAL_mean)
        
    #Range chart limits
    UAL_range_list = []
    UWL_range_list = []
    
    UAL_range = D1_1*value_range
    UWL_range = D1_25*value_range
    
    
    for i in range(1, batch_list[-1] + 1):
        UAL_range_list.append(UAL_range)
        UWL_range_list.append(UWL_range)
    
    print len(UAL_mean_list), len(batch_list)
    
    pyplot.figure(1)
    pyplot.subplot(1, 2, 1)

        
    pyplot.plot(batch_list, value_mlist, "k-", label = "Data")
    pyplot.plot( batch_list, value_mlist, "ko")
    pyplot.plot(batch_list, value_mean_list, "g-", label = "Data_mean")
    
    pyplot.plot(batch_list, UAL_mean_list, "r-", label = "UAL" )
    pyplot.plot(batch_list, UWL_mean_list, "y-", label = "UWL" )
    pyplot.plot(batch_list, LWL_mean_list, "y-", label = "LWL" )
    pyplot.plot(batch_list, LAL_mean_list, "r-", label = "LAL" )
    pyplot.legend()
    
    pyplot.subplot(1, 2, 2)
    pyplot.plot(batch_list, value_rlist, "k-", label = "Data_range")   #Range Data
    pyplot.plot(batch_list, value_range_list, "g-", label = "Data_mean_range")    
    
    pyplot.plot(batch_list, UAL_range_list, "r", label = "UAL")
    pyplot.plot(batch_list, UWL_range_list, "y-", label = "UWL")
    pyplot.legend()
    pyplot.show(1)   
        
    
#5. Want to be alerted by form of a graph of
#   within this SPC file by a plot when similar recipes done 
    
#6. Recipe number should be incorporated into the code for recipe comparison
    
#7. Fixing created lists for errors
    
#change_val = input('Value Change: ')
#change_batch = input('Batch Number')
#
#value_mlist[change_batch - 1] = change_val
    
#Comment out import code and averaging code when making changes  and uncomment error code
    
#8. Polishing of code


    
    

    
    
    
    
    