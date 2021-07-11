# First we'll import the os module
# This will allow us to create file paths across operating systems

import os

# Then import the Module for reading CSV files

import csv

# Use an absolute path to locate the csv file (copy the path from explorer then add the file name)

csvpath = r"G:\My Drive\BOOTCAMP\Data_Boot_Camp_Homework_GW\python_challenge\PyPoll\Resources\election_data.csv"


# Reading the file using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable called csv.reader that holds contents

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Reads the header row first and print it

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    
# TODO now I want to count the total votes excluding the Header

# Num_rows = -1 excludes the first row

num_rows = -1

for row in open(csvpath):
    num_rows += 1

print(num_rows)

# TODO now I want to print "Election Results"

print("Election Results")

# TODO now I want to print the total number of votes cast

print(f"Total Votes: {str(num_rows)}")

# TODO now I want to print a list of the candidates









