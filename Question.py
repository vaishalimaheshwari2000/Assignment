# Write a program to GET random data of an user and write it in a File named
# users.csv. Each GET request must have an interval time of 1 second and append the
# information in a comma separated format. You can use any open source mock rest
# api endpoints available on the internet or use Random Data API
# (https://random-data-api.com/documentation)


import urllib
import requests
import pandas as pd
import json                 # Used to load data into JSON format
from pprint import pprint   # pretty-print
from requests.api import head
import csv

url = "http://api.coincap.io/v2/assets"

headers = {
    'Accept': 'application/json',
    'Content-type': 'application/json'
}
response_API = requests.request("GET",url,headers=headers,data={})
myjson = response_API.json()

ourdata = []
csvheader = ['SYMBOL','NAME','PRICE(USD)']
# For append the data with the new array
for item in myjson["data"]:
    listing= [item["symbol"],item["name"],item["priceUsd"]]
    ourdata.append(listing)

pprint(ourdata)

# Used for write data into the csv file 
with open('users.csv','w',encoding='UTF-8',newline='') as f:
  writer = csv.writer(f)


  writer.writerow(csvheader)
  writer.writerows(ourdata)
