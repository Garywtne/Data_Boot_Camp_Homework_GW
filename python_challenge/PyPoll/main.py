
# Import the os module

import os

# Then import the Module for reading CSV files

import csv

# Use an absolute path to locate the csv file (copy the path from explorer then add the file name with r infront of the string so that python reads it exactly)

election_data = r"G:\My Drive\BOOTCAMP\Data_Boot_Camp_Homework_GW\python_challenge\PyPoll\Resources\election_data.csv"

# Read the file using CSV module

with open(election_data) as csvfile:




# define a varialbe called votes to count the total votes excluding the Header

    votes = -1

# TODO now I want to define a varialble called candiates to count the candidates excluding the Header

    

    
for row in open(election_data):
    votes += 1

print(" ")
# print "Election Results" and "--------------------"

print("Election Results")
print("----------------------")

# print the total number of votes cast

print(f"Total Votes: {str(votes)}")

# print "--------------------"

print("----------------------")

# output to a text file
f = open(r"G:\My Drive\BOOTCAMP\Data_Boot_Camp_Homework_GW\python_challenge\PyPoll\Analysis\PyPoll.txt", 'w')
f.writelines(["Election Results","\n","----------------------","\n",f"Total Votes: {str(votes)}","\n","----------------------"])
f.close()
