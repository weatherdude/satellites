import requests
import pandas as pd
import csv


lat = 52.262297
lon = 10.522219
altitude = 75
search_angle = 70
category = 1 # brightest satellites
key = ""

# get all current satellites above position
url = "https://api.n2yo.com/rest/v1/satellite/above/"+str(lat)+"/"+str(lon)+"/"+str(altitude)+"/"+str(search_angle)+"/"+str(category)+"/&apiKey="+key+""
data = requests.get(url)
data = data.json()

# get more info on found satellites (azimuth and elevation)
id = 20663
sec = 1 # retrieve position for next x sec
url = "https://api.n2yo.com/rest/v1/satellite/positions/"+str(id)+"/"+str(lat)+"/"+str(lon)+"/"+str(altitude)+"/"+str(sec)+"/&apiKey="+key+""
data2 = requests.get(url)
data2 = data2.json()


def above(lat,lon,altitude,search_angle,category,key):
    url = "https://api.n2yo.com/rest/v1/satellite/above/"+str(lat)+"/"+str(lon)+"/"+str(altitude)+"/"+str(search_angle)+"/"+str(category)+"/&apiKey="+key+""
    data = requests.get(url)
    data = data.json()
    return data

def sat_position(id,lat,lon,altitude,sec,key):
    url = "https://api.n2yo.com/rest/v1/satellite/positions/"+str(id)+"/"+str(lat)+"/"+str(lon)+"/"+str(altitude)+"/"+str(sec)+"/&apiKey="+key+""
    data = requests.get(url)
    data = data.json()
    return data

