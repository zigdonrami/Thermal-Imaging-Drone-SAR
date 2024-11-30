import datetime;
import csv
import os
from pathlib import Path

time_data_file = "/detection_output.csv" 

"""
def write_time_stamp():
    ct = datetime.datetime.now()
    print("current time:-", ct)
    write_to_file(time_data_file,ct)
"""

def write_to_file(file_path,data):
    create_file_ifnot_exist(file_path)
    with open(file_path+time_data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def create_file_ifnot_exist(file_path):
    if(os.path.exists(file_path+time_data_file)):
        pass 
    else:
        file = open(file_path+time_data_file, 'w+')
        #with open(file_path+time_data_file, 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Image name",'LAT','LON'])
        file.close()
