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

#Data input required 
recipe_no = input('Recipe Number: ')
recipe_no = int(recipe_no)
num = input('Number of recipes: ')   #Number of recipes we currently have
num = int(num)
type_run = input('Electronic or Manual: ')

                  
##Data input from new input
##Electronic input of data
if type_run == 'Electronic':
#    file_name1 = input('File Name 1: ')   #First_test.csv
    
    data1 = pandas.read_csv('First_test.csv', parse_dates=['TimeStamp']) 
    data1 = data1['Value']
    
    #Plotting data from continuous control over time to see visually change in values
    #Assume data changing over time for a particular batch so single value required per batch
    #Finding average value of data during the batch
    vals_per_batch =  data1.tolist()
    time_stamp = range(1, len(data1) + 1)     
    
    pyplot.figure()
    pyplot.title('Continuous Control' )
    pyplot.xlabel('Time')
    pyplot.ylabel('Controlled Variable')
    pyplot.plot(time_stamp, vals_per_batch, 'g-')
    pyplot.legend()                                
    pyplot.show()    #return error message
       
    av_value = numpy.mean(vals_per_batch)
    
#Manual input of data
if type_run == 'Manual':
    av_value = input('Batch Value: ')
    av_value = float(av_value)  #Return error message and Temperature on graph
    
    
##Data input from storage

#file_name2 = input('File Name 2: ')   #'Storage.csv'
data2 = pandas.read_csv('First_storage2.csv') 

data2_values = list(data2['Values'])
data2_range = list(data2['Ranges'])
data2_recipe = list(data2['Recipes'])

#Creating a list that can be used in SPC by combining storage and new data
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

print (length_data)

for b in range(1, length_data + 1):
    batch_list.append(b)
    
    print (value_rlist)
    
    if length_data < 4 and len(value_rlist) < 3:
        value_rlist.append(1)
        
    print (value_rlist)
        
    
#Functions for SPC plots
    
def plot_stats(x_points, ym_points, yr_points, title_1, title_2, title_3, title_4, xlabel, ylabel ):
    pyplot.figure()
   
    
    pyplot.subplot(1, 2, 1)
    pyplot.title(title_1)
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    pyplot.plot(x_points, ym_points,"k-", marker='o', label = title_3)
    
    plot_mean()
    
    pyplot.subplot(1, 2, 2)
    pyplot.title(title_2)
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    pyplot.plot(x_points, yr_points,"k-", marker='o', label = title_4)

    plot_range()

def plot_mean():
    
    pyplot.axhline(value_mean, 0, max(batch_list), label='Process mean', color = 'g')
    pyplot.axhline(UAL_mean, 0, max(batch_list), label='UAL', color = 'r')
    pyplot.axhline(UWL_mean, 0, max(batch_list), label='UWL', color = 'y')
    pyplot.axhline(LWL_mean, 0, max(batch_list), label='LWL', color = 'y')     
    pyplot.axhline(LAL_mean, 0, max(batch_list), label='LAL', color = 'r')     
    pyplot.legend(loc = 'best')
    
def plot_range():    
    pyplot.axhline(value_range, 0, max(batch_list), label='Process mean range', color = 'g')    
    pyplot.axhline(UAL_range, 0, max(batch_list), label='UAL', color = 'r')
    pyplot.axhline(UWL_range, 0, max(batch_list), label='LWL', color = 'y')
    pyplot.legend(loc = 'best')
        
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
            
    #Recipe comparison    
    recipes = range(1, num + 1, 1)

    for j in recipes:
        
        recipe_mcomp = []
        recipe_rcomp = []
        batch_comp = []
        
        l = 0
        for k in recipe_list4:
            if j == k:
                recipe_mcomp.append(value_mlist4[l])
                batch_comp.append(batch_list4[l])
                recipe_rcomp.append(value_rlist4[l])
            l = l + 1
        
        #Plotting of recipe comparison results
        
        if len(recipe_mcomp)>=2:
            
            
           plot_stats(batch_comp, recipe_mcomp, recipe_rcomp, 
           'Moving mean control chart for Recipe No {}'.format(j), 'Moving range control chart for Recipe No {}'.format(j), 'Process data','Process range data', 'Batch number', 'Controlled variable')
            
           pyplot.show()
           
    plot_stats(batch_list4, value_mlist4, value_rlist4, 
               'Moving mean control chart', 'Moving range control chart', 'Process data', 'Process range data', 'Batch number', 'Controlled variable')
            

    pyplot.show()
    
 

#Updating storage

print (batch_list)
print (value_mlist)
print (value_rlist)
print (recipe_no_list)

data3 = pandas.DataFrame({'Batches': batch_list,'Values': value_mlist, 'Ranges': value_rlist, 'Recipes': recipe_no_list})



print (data3)

data3.to_csv('First_storage2.csv')






    
    

    
    
    
    
    