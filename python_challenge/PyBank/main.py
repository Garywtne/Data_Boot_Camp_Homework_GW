# First I import the os module
# This will allow us to create file paths across operating systems

import os

# Then import the Module for reading CSV files

import csv

# Use an absolute path to locate the csv file (copy the path from explorer then add the file name using r to ensure that python reads it exactly)

Budget_data = r"G:\My Drive\BOOTCAMP\Data_Boot_Camp_Homework_GW\python_challenge\PyBank\Resources\budget_data.csv"


# Reading the file using CSV module

with open(Budget_data) as csvfile:

    # CSV reader specifies delimiter and variable called csv.reader that holds contents

    csvreader = csv.reader(csvfile, delimiter=',')

    # Reads the header row first and print it

    csv_header = next(csvreader)


    # set initial values for the number of rows and the sum of values

    num_rows = 0
    sum_rows = 0

    # Reads and prints each row of data after the header

    for row in csvreader:
       
# TODO now I want to count the dates in the Date column excluding the Header

#for row in open(csvpath):
        num_rows += 1
        sum_rows += int(row[1])

print(" ")

print("Finacial Analysis")

print("-------------------")

# print(sum_rows)

print(f"Total Months: {str(num_rows)}")

# TODO here I want to sum up all of the values in the second column.

print(f"Total: ${str(sum_rows)}")




# TODO here I want to calculate the changes in Profit/Loss from month to month, write them to the csv and then calculate the average 

print(f"Average Change: ${str()}")

# TODO here I want to find the highest value change and the date that it happened

print(f"Greatest Increase in profits ${str()} ")

# TODO here I want to find the lowest value change and the date that it happened

print(f"Greatest Decrease in profits ${str()} ")


# TODO now I want to output to a text file
f = open(r"G:\My Drive\BOOTCAMP\Data_Boot_Camp_Homework_GW\python_challenge\PyBank\Analysis\PyBank.txt", 'w')
f.writelines(["Finacial Analysis"," ","------------------"," ",f"Total Months: {str(num_rows)}"," ",f"Total: ${str(sum_rows)}"," ",f"Average Change: ${str()}"," ",f"Greatest Increase in profits ${str()} "," ",f"Greatest Decrease in profits ${str()} "])
f.close()