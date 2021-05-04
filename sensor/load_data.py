import os
import glob
import csv

def load_sensor_data(): #function that loads the sensor data stored in the data file
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv')) #get data from csv file and put it in sensor_files variable
    for sensor_file in sensor_files: #iterate over sensor_files
        with open (sensor_file, 'r') as data_file: 
            data_reader = csv.DictReader(data_file,delimiter=',')
            for row in data_reader:
                sensor_data.append(row)
    return sensor_data

            

