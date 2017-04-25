# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 06:24:23 2017

@author: user
"""

from matplotlib import pyplot

#import numpy
#import csv

#Data set of old and new data
#1. Importing storage file of the previous batches.
#    should be able to go into code and correct error
#    Code in different script for data handling required instead

#data = []
#
#with open('storage.csv', 'rb') as csvfile:
#    csvreader = csv.reader(csvfile, delimiter=',')
#    for cnt, row in enumerate(csvreader):
#        if cnt == 0:
#            headings = row
#        else:
#            data.append(row)
#            
#print headings, data
#
#value_list = data[]
#batch_list = data[]

value_mlist = [1.0, 1.2, 1.3, 1.4]  
batch_list = [1, 2, 3, 3]
value_rlist = [0.2, 0.3, 0.2,0.3]

#Parameters
sample  = 4
A_2 = 0.73
two_thirds_A2 = 0.49
D1_1 = 2.57
D1_25 = 1.93

#Inputs
batch = input("Batch No: ")
value = input("Value: ")
value_mlist.append(value)
batch_list.append(batch)

#Fix the SPC method to improve return of results
if batch >= sample:   #Only starts plotting if more than 4 batches
    
    #Calculate mean and range from previous 4 batches
    values_4 = []
    for j in range(-1, -5, -1):
        values_4.append(value_mlist[j])
        
    print values_4

    value_mean = sum(values_4)/batch
    value_range = max(values_4)-min(values_4)
    
    value_rlist.append(value_range)
    
    #Mean and range lines for graphs
    value_mean_list  = []
    value_range_list = []
    for i in range(1, batch + 1):
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
    
    
    for i in range(1, batch + 1):
        UAL_mean_list.append(UAL_mean)
        UWL_mean_list.append(UWL_mean)
        LWL_mean_list.append(LWL_mean)
        LAL_mean_list.append(LAL_mean)
        
    #Range chart limits
    UAL_range_list = []
    UWL_range_list = []
    
    UAL_range = D1_1*value_range
    UWL_range = D1_25*value_range
    
    
    for i in range(1, batch + 1):
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

#else:    #Values from when the process was thought to be in statistical process control i.e. 4 values 
                                    #so can start plotting graphs instead of waiting for 4 batches
    
#4. Write to storage i.e. csv file in order to update for batch and SG list
     #Another python script required for this instead of csv file

#headings = ["batch list", "SG number"]
#data = numpy.matrix([[batch, SG]])
#
#with open("storage.csv", "wb") as a csv file:
#    csvwriter = csv.writer(csvfile, delimiter = ",")
#    csvwriter.writerow(headings)
#    for row_data in data:
#        csvwriter.writerow(row_data)
    
#5. Split the code into separate files for easier use of code
#6. Should be able to plot for different periods and compare
    

    
    
    
    
    