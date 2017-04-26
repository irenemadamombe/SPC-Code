# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:11:12 2017

@author: user
"""

import csv

#Data Aquisition

def data_aquis(file_name):
    
    #Raw data
    data = []
    #1. Using Bernie's data logging confirm the csv method of aquiring data
    #Open the storage from the database in form of csv to get data for a particular batch
    with open(file_name, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for cnt, row in enumerate(csvreader):
            if cnt == 0:
                headings = row
            else:
                data.append(row)

    #Getting lists from matrix
    vals_per_batch = data[:,1]
    time_stamp = data[:,0]    
    
    return [headings, vals_per_batch, time_stamp]


    
    

    

