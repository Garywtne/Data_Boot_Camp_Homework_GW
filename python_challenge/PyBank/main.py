# First we'll import the os module
# This will allow us to create file paths across operating systems

import os

# Then import the Module for reading CSV files

import csv

# Use an absolute path to locate the csv file (copy the path from explorer then add the file name)

csvpath = r"G:\My Drive\BOOTCAMP\Data_Boot_Camp_Homework_GW\python_challenge\PyBank\Resources\budget_data.csv"


# Reading the file using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable called csv.reader that holds contents

    csvreader = csv.reader(csvfile, delimiter=',')

   

    # Reads the header row first and print it

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    num_rows = 0
    sum_rows = 0

    # Reads and prints each row of data after the header

    for row in csvreader:
       
# TODO now I want to count the dates in the Date column excluding the Header

#for row in open(csvpath):
        num_rows += 1
        sum_rows += int(row[1])

print(sum_rows)

print(f"Total Months: {str(num_rows)}")

# TODO here I want to sum up all of the values in the second column.


print(f"Total: ${str(num_rows)}")

# TODO here I want to calculate the changes in Profit/Loss from month to month, write them to the csv and then calculate the average 

print(f"Average Change: ${str(num_rows)}")

# TODO here I want to find the highest value change and the date that it happened

print(f"Greatest Increase in profits {str(num_rows)} ${str(num_rows)} ")

# TODO here I want to find the lowest value change and the date that it happened

print(f"Greatest Decrease in profits {str(num_rows)} ${str(num_rows)} ")


