# First I import the os module
# This will allow us to create file paths across operating systems

import os

# Import the Module for reading CSV files

import csv

# Use an absolute path to locate the csv file (copy the path from explorer then add the file name using r to ensure that python reads it exactly)

Budget_data = r"G:\My Drive\BOOTCAMP\Data_Boot_Camp_Homework_GW\python_challenge\PyBank\Resources\budget_data.csv"


# Reading the file using CSV module

with open(Budget_data) as csvfile:

    # CSV reader specifies delimiter and a variable called Budget_data that holds contents

    Budget_data = csv.reader(csvfile, delimiter=',')
    
    # Reads the header row first and prints it

    header = next(Budget_data)

    print(" ")

    print(header)

    # define the variables and set initial values for the number of rows, sum of values, Average Change, Greatest Increase and Greatest Decrease

    num_rows = 0
    sum_values = 0
    Average_Change = 0
    Greatest_Increase = 0
    Greatest_Decrease = 0

   
    for row in Budget_data:
       
        # define a variable for counting the dates in the Date column excluding the Header and for summing up the values in the Profit/Losses column

        num_rows += 1
        sum_values += int(row[1])
        

print(" ")

print("Finacial Analysis")

print("-------------------")

# print the sum of rows

print(f"Total Months: {str(num_rows)}")

# print the sum of values

print(f"Total: ${str(sum_values)}")

# TODO here I want to calculate the changes in Profit/Loss from month to month and then calculate the average 


# print the average change
print(f"Average Change: ${str()}")

# TODO here I want to find the highest value change and the date that it happened


# print the Greatest Increase in profits
print(f"Greatest Increase in profits ${str()} ")

# TODO here I want to find the lowest value change and the date that it happened


# print the greatest decrease in profit and the dat it happened
print(f"Greatest Decrease in profits ${str()} ")


# output results to a text file
f = open(r"G:\My Drive\BOOTCAMP\Data_Boot_Camp_Homework_GW\python_challenge\PyBank\Analysis\PyBank.txt", 'w')
f.writelines(["Finacial Analysis","\n","------------------","\n",f"Total Months: {str(num_rows)}","\n",f"Total: ${str(sum_values)}","\n",f"Average Change: ${str()}","\n",f"Greatest Increase in profits ${str()} ","\n",f"Greatest Decrease in profits ${str()} "])
f.close()