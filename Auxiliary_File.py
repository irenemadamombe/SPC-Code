# -*- coding: utf-8 -*-
"""
Created on Tue May 02 21:43:25 2017

@author: user
"""

import csv
import numpy

def data_call(file_name):
    
    data = []
    with open(file_name, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for cnt, row in enumerate(csvreader):
            if cnt == 0:
                headings = row
            else:
                new_row = []                             
                for a in range(1, len(row)):
                    new_row.append(row[a])
                new_row = map(float, new_row)
                data.append(new_row)
        data = numpy.array(data) 
        
    return headings,data
    
    
def data_write(file_name, headings, data):
    
    with open(file_name, 'wb') as csvfile:
        # initialize the csv.writer object
        csvwriter = csv.writer(csvfile, delimiter=',')
        # write the headings for the data
        csvwriter.writerow(headings)
        # write each row of the data list to file
        for row_data in data:
            csvwriter.writerow(row_data)
    