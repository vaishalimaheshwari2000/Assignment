# Write a program to Input Id or Username of an user and return the details of
# that user in the output of the program



import pandas as pd
# Read a comma-separated values (csv) file into DataFrame and also load the csv into a dataframe
data = pd.read_csv("users-sorted.csv") 
ch = input("Enter Input Id: ")
# This line take the input_id col as index and compare with the input value and display the whole row of that column value
print(data[data['INPUT_ID']== int(ch)])