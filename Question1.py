# Write a program to read users.csv and create users-sorted.csv by applying
# sorting algorithm on firstName / Name / Username (Field of your choice
# based on your dataset)


import csv
import random
import pandas as pd
with open('users.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  # for line in csv_reader:
  #   print(line)
price = 0
# opening our " data to be sorted " file
file = open('users.csv','r')
 
# Reading as csv
csv_reader = csv.reader(file,delimiter=',')

# converting csv_object to list object
csv_list = list(csv_reader)

file.close()
# opening new file where the sorted results are stored
file1 = open('users-sorted.csv','w')

# Inserting 1st row which contains names of columns along with input id ahead of the whole row
rows = csv_list[0]
# print(rows)
file1.write("INPUT_ID,")
for i in rows:
    if i == rows[-1]:
        file1.write(i)
    else:
        file1.write(i + ',')
file1.write('\n')

# deducing 1st row and reverse sorting the csv_list
csv_list = csv_list[1:]
csv_list.sort(key= lambda x: x[-1], reverse=False)
pprint(csv_list)

# inserting each sorted row along with rank into sorted file
for i in csv_list:
    if price == 0:
        prev_i = csv_list[csv_list.index(i)]    # previous data
        price += 1
    else:
        prev_i = csv_list[csv_list.index(i) - 1] # previous data  used to check whether two cryptocurrency got same price or not
    if prev_i[-2] == i[-2]:           #if previous price is equal to current price rank wont change
      price = price
    else:
       price = random.randint(0,10000)                     # else input id 
    file1.write(f'{price},')           # writing price to file
    for j in i:                       # writing remaining rows to file
        if j == i[-1] :
            file1.write(j)
        else:
            file1.write(j + ',')
    file1.write('\n')

# closing the opened files
file.close()
file1.close()
