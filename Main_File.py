# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 06:24:23 2017

@author: user
"""

from matplotlib import pyplot
import csv

#Electronic input of data

#1. Confrirm electronic input works

data = []

with open('First test data_Tlog_2.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for cnt, row in enumerate(csvreader):
        if cnt == 0:
            headings = row
        else:
            data.append(row)

#Getting lists from matrix

print len(data)

#vals_per_batch = data[:,1]
#time_stamp = data[:,0]    

#Data input required for recipe analysis
recipe_no = input('Recipe Number: ')
num = input('Number of recipes: ')   #Number of recipes we currently have

recipe_no_list = []
recipe_no_list.append(recipe_no)

#Assume data changing over time for a particular batch so single value required per batch
#Plot to see visually change in values

#2. Determine standard for what is acceptable or not when analysing slope of data

time_stamp = data[0]
vals_per_batch = data[1]


#pyplot.figure()
#pyplot.plot(time_stamp, vals_per_batch, 'g-', label = 'values per batch')
#pyplot.legend()
#pyplot.show()

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

num = 10

##Manual input of data
#
#value_mlist = [1.0, 1.2, 1.3, 1.4, 1.3, 1.1, 1.2]  
#batch_list = [1, 2, 3, 4, 5, 6 ,7]
#value_rlist = [0.2, 0.3, 0.2,0.3, 0.1, 0.3, 0.2]
#recipe_no_list = [1, 2, 1, 3, 5, 1, 1]

#Parameters
sample  =  4
A_2 = 0.73
two_thirds_A2 = 0.49
D1_1 = 2.57
D1_25 = 1.93

#3. Individual chart for first 3 batches in order to start getting a graph instead
#   of waiting for four batches. Can use if statement

#Moving range and moving mean chart from 4th batch onwards
if batch_list[-1] >= sample:   #Only starts plotting if more than 4 batches
    
    #Calculate mean and range from previous 4 batches
    values_4 = []
    batch_4 = []
    for j in range(-1, -5, -1):
        values_4.append(value_mlist[j])
        batch_4.append(batch_list[j])
        
    print values_4

    value_mean = sum(values_4)/len(batch_4)   
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
            
    recipes = range(1, num + 1)

    for k in recipes:
        
        recipe_mcomp = []
        recipe_rcomp = []
        batch_comp = []
        
        m = 0
        for l in recipe_list4:
            if k == l:
                recipe_mcomp.append(value_mlist4[m])
                batch_comp.append(batch_list4[m])
                recipe_rcomp.append(value_rlist[m])
            m = m + 1
        
        if len(recipe_mcomp)>=2:
            pyplot.figure()
            pyplot.subplot(1,2,1)
            
            pyplot.plot(batch_comp, recipe_mcomp,"k-", label = "Recipe Comparison")
            pyplot.plot(batch_comp, recipe_mcomp,"ko")
            
            pyplot.plot(batch_list, value_mean_list, "g-", label = "Data_mean")
            pyplot.plot(batch_list, UAL_mean_list, "r-", label = "UAL" )
            pyplot.plot(batch_list, UWL_mean_list, "y-", label = "UWL" )
            pyplot.plot(batch_list, LWL_mean_list, "y-", label = "LWL" )
            pyplot.plot(batch_list, LAL_mean_list, "r-", label = "LAL" )
            #pyplot.legend()
            
            pyplot.subplot(1,2,2)  
            
            pyplot.plot(batch_comp, recipe_rcomp,"k-", label = "Recipe Comparison")
            pyplot.plot(batch_comp, recipe_rcomp,"ko")
            
            pyplot.plot(batch_list, value_range_list, "g-", label = "Data_mean_range") 
            pyplot.plot(batch_list, UAL_range_list, "r", label = "UAL")
            pyplot.plot(batch_list, UWL_range_list, "y-", label = "UWL")
            
            #pyplot.legend()
            pyplot.show()
        
        
    pyplot.figure()
    pyplot.subplot(1, 2, 1)

    pyplot.plot(batch_list4, value_mlist4, "k-", label = "Data")
    pyplot.plot(batch_list4, value_mlist4, "ko")
    pyplot.plot(batch_list, value_mean_list, "g-", label = "Data_mean")
    
    pyplot.plot(batch_list, UAL_mean_list, "r-", label = "UAL" )
    pyplot.plot(batch_list, UWL_mean_list, "y-", label = "UWL" )
    pyplot.plot(batch_list, LWL_mean_list, "y-", label = "LWL" )
    pyplot.plot(batch_list, LAL_mean_list, "r-", label = "LAL" )
    #pyplot.legend()
    
    pyplot.subplot(1, 2, 2)
    pyplot.plot(batch_list4, value_rlist4, "k-", label = "Data_range")   #Range Data
    pyplot.plot(batch_list4, value_rlist4, "ko")
    pyplot.plot(batch_list, value_range_list, "g-", label = "Data_mean_range")    
    
    pyplot.plot(batch_list, UAL_range_list, "r", label = "UAL")
    pyplot.plot(batch_list, UWL_range_list, "y-", label = "UWL")
    #pyplot.legend()
    pyplot.show()   
    

    
#4. Fixing created lists for errors
    
#change_val = input('Value Change: ')
#change_batch = input('Batch Number')
#
#value_mlist[change_batch - 1] = change_val
    
#Comment out import code and averaging code when making changes  and uncomment error code
    
# Fix issue of running code several times
    
#5. Polishing of code


    
    

    
    
    
    
    