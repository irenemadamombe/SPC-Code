# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 06:24:23 2017

@author: user
"""

from matplotlib import pyplot
from Auxiliary_File import data_call
import numpy
import csv

#Parameters 
sample  =  4
A_2 = 0.73
two_thirds_A2 = 0.49
D1_1 = 2.57
D1_25 = 1.93

#Data input required for recipe analysis
recipe_no = input('Recipe Number: ')
num = input('Number of recipes: ')   #Number of recipes we currently have

#Electronic input of data
#Data input from new input
file_name1 = raw_input('File Name 1: ')   #'First test data_Tlog_2.csv'

data1 = data_call(file_name1)

data1 = data1[1]
 
#Data input from storage
file_name2 = raw_input('File Name 2: ')   #'Storage.csv'

data2 = data_call(file_name2)

data2 = data2[1]

data2_values = list(data2[:,0])
data2_range = list(data2[:,1])
data2_recipe = list(data2[:,2])

#Plotting data from continuous control over time to see visually change in values
#Assume data changing over time for a particular batch so single value required per batch
#Finding average value of data during the batch

vals_per_batch =  list(data1[:,0])
time_stamp = range(1, len(data1) + 1)     

pyplot.figure(1)
pyplot.plot(time_stamp, vals_per_batch, 'g-', label = 'values per batch')
pyplot.legend()                                
pyplot.show(1)    
   
av_value = sum(vals_per_batch)/len(vals_per_batch) 

#Creating a list that can be used in SPC 

batch_list = []
value_mlist = []
value_rlist = []
recipe_no_list = []

recipe_no_list.extend(data2_recipe)
recipe_no_list.append(recipe_no)

value_mlist.extend(data2_values)
value_mlist.append(av_value)

value_rlist.extend(data2_range)

length_data = len(value_mlist)

for b in range(1, length_data + 1):                 #Improve and dont use for loop?
    batch_list.append(b)
        
#Moving range and moving mean chart from 4th batch onwards
#Only starts plotting if more than 4 batches
if batch_list[-1] >= sample:   
    
    #Calculate mean and range from previous 4 batches
    values_4 = []
    batch_4 = []
    for c in range(-1, -5, -1):
        values_4.append(value_mlist[c])
        batch_4.append(batch_list[c])
        
    value_mean = sum(values_4)/len(batch_4)   
    value_range = max(values_4)-min(values_4)
            
    value_rlist.append(value_range)
    
    #Mean and range lines for graphs
    value_mean_list  = []
    value_range_list = []
    for f in range(1, batch_list[-1] + 1):
        value_mean_list.append(value_mean)
        value_range_list.append(value_range)     #Improve and dont use for loop?
      
    #Mean Chart limits
    UAL_mean_list = []
    UWL_mean_list = []
    LWL_mean_list = []
    LAL_mean_list = []   
    
    UAL_mean = value_mean + A_2*value_range
    UWL_mean = value_mean + two_thirds_A2*value_range
    LWL_mean = value_mean - two_thirds_A2*value_range
    LAL_mean = value_mean - A_2*value_range 
    
    
    for g in range(1, batch_list[-1] + 1):
        UAL_mean_list.append(UAL_mean)
        UWL_mean_list.append(UWL_mean)     #Improve and dont use for loop?
        LWL_mean_list.append(LWL_mean)     
        LAL_mean_list.append(LAL_mean)
        
    #Range chart limits
    UAL_range_list = []
    UWL_range_list = []
    
    UAL_range = D1_1*value_range
    UWL_range = D1_25*value_range
    
    for h in range(1, batch_list[-1] + 1):
        UAL_range_list.append(UAL_range)
        UWL_range_list.append(UWL_range)    #Improve and dont use for loop?
    
    print len(UAL_mean_list), len(batch_list)
    
    #Creating plotting list to start at 4 batches
    
    batch_list4 = []
    value_mlist4 = []
    value_rlist4 = []
    recipe_list4 = []
    
    for i in range(1, batch_list[-1] + 1):
        if i >=4:
            batch_list4.append(i)
            value_mlist4.append(value_mlist[i-1])
            value_rlist4.append(value_rlist[i-1])
            recipe_list4.append(recipe_no_list[i-1])
            
    
    #Recipe comparison    
    recipes = range(1, num + 1)

    for j in recipes:
        
        recipe_mcomp = []
        recipe_rcomp = []
        batch_comp = []
        
        l = 0
        for k in recipe_list4:
            if j == k:
                recipe_mcomp.append(value_mlist4[l])
                batch_comp.append(batch_list4[l])
                recipe_rcomp.append(value_rlist[l])
            l = l + 1
        
        if len(recipe_mcomp)>=2:
            pyplot.figure(2)
            pyplot.subplot(1, 2, 1)
            
            pyplot.plot(batch_comp, recipe_mcomp,"k-", label = "Recipe Comparison")
            pyplot.plot(batch_comp, recipe_mcomp,"ko")
            
            pyplot.plot(batch_list, value_mean_list, "g-", label = "Data_mean")
            pyplot.plot(batch_list, UAL_mean_list, "r-", label = "UAL" )
            pyplot.plot(batch_list, UWL_mean_list, "y-", label = "UWL" )
            pyplot.plot(batch_list, LWL_mean_list, "y-", label = "LWL" )
            pyplot.plot(batch_list, LAL_mean_list, "r-", label = "LAL" )
            #pyplot.legend()
            
            pyplot.subplot(1, 2, 2)  
            
            pyplot.plot(batch_comp, recipe_rcomp,"k-", label = "Recipe Comparison")
            pyplot.plot(batch_comp, recipe_rcomp,"ko")
            
            pyplot.plot(batch_list, value_range_list, "g-", label = "Data_mean_range") 
            pyplot.plot(batch_list, UAL_range_list, "r", label = "UAL")
            pyplot.plot(batch_list, UWL_range_list, "y-", label = "UWL")
            
            #pyplot.legend()
            pyplot.show(2)
            
    pyplot.figure(3)
    pyplot.subplot(1, 2, 1)

    pyplot.plot(batch_list4, value_mlist4, "k-", label = "Data")
    pyplot.plot(batch_list4, value_mlist4, "ko")
    pyplot.plot(batch_list, value_mean_list, "g-", label = "Data_mean")
    
    pyplot.plot(batch_list, UAL_mean_list, "r-", label = "UAL" )
    pyplot.plot(batch_list, UWL_mean_list, "y-", label = "UWL" )
    pyplot.plot(batch_list, LWL_mean_list, "y-", label = "LWL" )     #Improve by creating a function to
    pyplot.plot(batch_list, LAL_mean_list, "r-", label = "LAL" )       #avoid repitition?
    #pyplot.legend()
    
    pyplot.subplot(1, 2, 2)
    pyplot.plot(batch_list4, value_rlist4, "k-", label = "Data_range")   #Range Data
    pyplot.plot(batch_list4, value_rlist4, "ko")
    pyplot.plot(batch_list, value_range_list, "g-", label = "Data_mean_range")    
    
    pyplot.plot(batch_list, UAL_range_list, "r", label = "UAL")
    pyplot.plot(batch_list, UWL_range_list, "y-", label = "UWL")
    #pyplot.legend()
    pyplot.show(3)   
    

#Updating storage

headings = ['Batches', 'Values', 'Ranges', 'Recipes']
data = numpy.column_stack([batch_list, value_mlist, value_rlist, recipe_no_list])

with open(file_name2, 'wb') as csvfile:
    # initialize the csv.writer object
    csvwriter = csv.writer(csvfile, delimiter=',')
    # write the headings for the data
    csvwriter.writerow(headings)
    # write each row of the data list to file
    for row_data in data:
        csvwriter.writerow(row_data)
            
# Polishing of code i.e. good code
# Code annotation




    
    

    
    
    
    
    