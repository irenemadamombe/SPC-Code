# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 06:24:23 2017

@author: user
"""

from matplotlib import pyplot
import numpy
import pandas

#Parameters 
sample  =  4
A_2 = 0.73
two_thirds_A2 = 0.49
D1_1 = 2.57
D1_25 = 1.93

#Data input required for recipe analysis
#recipe_no = input('Recipe Number: ')
#num = input('Number of recipes: ')   #Number of recipes we currently have

recipe_no = 1
num = 10

##Electronic input of data
##Data input from new input

#file_name1 = input('File Name 1: ')   #First_test.csv
#print('filename',file_name1)

data1 = pandas.read_csv('First_test.csv', parse_dates=['TimeStamp']) 
data1 = data1['T1']

##Data input from storage
#file_name2 = input('File Name 2: ')   #'Storage.csv'

data2 = pandas.read_csv('First_storage.csv') 

data2_values = list(data2['Values'])
data2_range = list(data2['Ranges'])
data2_recipe = list(data2['Recipes'])

#Plotting data from continuous control over time to see visually change in values
#Assume data changing over time for a particular batch so single value required per batch
#Finding average value of data during the batch
vals_per_batch =  data1.tolist()
time_stamp = range(1, len(data1) + 1)     

pyplot.figure(1)
pyplot.plot(time_stamp, vals_per_batch, 'g-', label = 'values per batch')
pyplot.legend()                                
pyplot.show(1)    
   
av_value = numpy.mean(vals_per_batch)

#Creating a list that can be used in SPC by combining storage and new data
batch_list = []
value_mlist = []
value_rlist = []
recipe_no_list = []

recipe_no_list.extend(data2_recipe)
recipe_no_list.append(recipe_no)

print (recipe_no_list)

value_mlist.extend(data2_values)
value_mlist.append(av_value)

value_rlist.extend(data2_range)

length_data = len(value_mlist)

for b in range(1, length_data + 1):
    batch_list.append(b)
        
#Moving range and moving mean chart from 4th batch onwards
#Only starts plotting if more than 4 batches
if batch_list[-1] >= sample:   
    
    #Calculate mean and range from previous 4 batches
    values_4 = []
    for c in range(-1, -5, -1):
        values_4.append(value_mlist[c])

    value_mean =  numpy.mean(values_4)
    value_range = max(values_4)-min(values_4)
            
    value_rlist.append(value_range)
    
    
    #Chart limits
    UAL_mean = value_mean + A_2*value_range
    UWL_mean = value_mean + two_thirds_A2*value_range
    LWL_mean = value_mean - two_thirds_A2*value_range
    LAL_mean = value_mean - A_2*value_range

    UAL_range = D1_1*value_range
    UWL_range = D1_25*value_range

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
            
#    #Recipe comparison    
#    recipes = range(1, num + 1, 1)
#
#    for j in recipes:
#        
#        recipe_mcomp = []
#        recipe_rcomp = []
#        batch_comp = []
#        
#        l = 0
#        for k in recipe_list4:
#            if j == k:
#                recipe_mcomp.append(value_mlist4[l])
#                batch_comp.append(batch_list4[l])
#                recipe_rcomp.append(value_rlist4[l])
#            l = l + 1
#            
#        #Plotting of recipe comparison results
#        
#        if len(recipe_mcomp)>=2:
#            pyplot.figure(2)
#            pyplot.subplot(1, 2, 1)
#            pyplot.plot(batch_comp, recipe_mcomp,"k-", label = "Recipe Comparison")
#            pyplot.plot(batch_comp, recipe_mcomp,"ko")
#            
#            pyplot.axhline(value_mean, 0, max(batch_list), label='Data_mean')
#            pyplot.axhline(UAL_mean, 0, max(batch_list), label='UAL')
#            pyplot.axhline(UWL_mean, 0, max(batch_list), label='UWL')
#            pyplot.axhline(LWL_mean, 0, max(batch_list), label='LWL')     
#            pyplot.axhline(LAL_mean, 0, max(batch_list), label='LAL')
#            pyplot.legend()
#            
#            pyplot.subplot(1, 2, 2)  
#            pyplot.plot(batch_comp, recipe_rcomp,"k-", label = "Recipe Comparison")
#            pyplot.plot(batch_comp, recipe_rcomp,"ko")
#            
#            pyplot.axhline(value_range, 0, max(batch_list), label='Data_mean_range') 
#            pyplot.axhline(UAL_range, 0, max(batch_list), label='UAL')
#            pyplot.axhline(UWL_range, 0, max(batch_list), label='LWL')
#            pyplot.legend()
#            
#            pyplot.show(2)
            
    pyplot.figure(3)
    pyplot.subplot(1, 2, 1)
    pyplot.plot(batch_list4, value_mlist4, "k-", label = "Data")
    pyplot.plot(batch_list4, value_mlist4, "ko")
    
    pyplot.axhline(value_mean, 0, max(batch_list), label='Data_mean', color = 'g')
    pyplot.axhline(UAL_mean, 0, max(batch_list), label='UAL', color = 'r')
    pyplot.axhline(UWL_mean, 0, max(batch_list), label='UWL', color = 'y')
    pyplot.axhline(LWL_mean, 0, max(batch_list), label='LWL', color = 'y')     
    pyplot.axhline(LAL_mean, 0, max(batch_list), label='LAL', color = 'r')     
    pyplot.legend(loc = 'best')
    
    pyplot.subplot(1, 2, 2)
    pyplot.plot(batch_list4, value_rlist4, "k-", label = "Data_range")   #Range Data
    pyplot.plot(batch_list4, value_rlist4, "ko")
    
    pyplot.axhline(value_range, 0, max(batch_list), label='Data_mean_range', color = 'g')    
    pyplot.axhline(UAL_range, 0, max(batch_list), label='UAL', color = 'r')
    pyplot.axhline(UWL_range, 0, max(batch_list), label='LWL', color = 'y')
    pyplot.legend(loc = 'best')
    
    pyplot.show(3)   
    
#Updating storage
headings3 = ['Batches', 'Values', 'Ranges', 'Recipes']
data3 = numpy.column_stack([batch_list, value_mlist, value_rlist, recipe_no_list])

print (data3)






    
    

    
    
    
    
    