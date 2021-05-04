from load_data import load_sensor_data #import load_sensor_data class from load_data.py
from particle_count_info import ParticleData #import ParticleData class from particle_count_info.py
from temperature_info import TemperatureData #import TemperatureData class from temperature_info.py
from humidity_info import HumidityData #import HumidityData class from humidity_info.py
from energy_info import EnergyData #import EnergyData class from energy_info.py
from house_info import HouseInfo #import HouseInfo class from house_info.py
from datetime import datetime #import datetime from datetime module
from datetime import date #import date from datetime module
from statistics import mean #import mean from statistics module


data = []
print("Sensor Data App")


#load_data
data = load_sensor_data()
print("Loaded records: {}".format(len(data))) #format and print loaded records


#house_info
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area("id",rec_area=test_area) 
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs))) #format and print House sensor records for area

test_date = datetime.strptime("5/9/20","%m/%d/%y")
recs = house_info.get_data_by_date("id",rec_date=test_date)
print("\nHouse sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs))) #format and print House sensor records for date 


#temperature_info
temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)
print("\nHouse Temperature sensor records for area {} = {}".format(test_area, len(recs))) #format and print House Temperature sensor records for area
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs))) #format and print max and min House Temperature sensor records
recs = temperature_data.get_data_by_date(rec_date=test_date)
print("\nHouse Temperature sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs))) #format and print House Temperature sensor records for date
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs))) #format and print max and min House Temperature sensor records for area



#humidity_info
humidity_data = HumidityData(data)
recs = humidity_data.get_data_by_area(rec_area=test_area)
print("\nHouse Humidity sensor records for area {} = {}".format(test_area, len(recs))) #format and print House Humidity sensor records for area
print("\tAverage: {} humidity".format(mean(recs))) #format and print average mean House Humidity sensor records values for area

recs = humidity_data.get_data_by_date(rec_date=test_date)
print("House Humidity sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs))) #format and print House Humidity sensor records for date
print("\tAverrage: {} humidity".format(mean(recs))) #format and print average mean House Humidity sensor records values for area



#particle_count_info
particle_data = ParticleData(data)
recs = particle_data.get_data_by_area(rec_area=test_area)
print("\nHouse Particle sensor records for area {} = {}".format(test_area, len(recs))) #format and print House Particle sensor records for area


concentrations = particle_data.get_data_concentrations(data=recs)
print("\tGood Air Quality Recs: {}".format(concentrations["good"])) #format and print Good Air Quality Recs
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"])) #format and print Moderate Air Quality Recs
print("\tBad Air Quality Recs: {}".format(concentrations["bad"])) #format and print Bad Air Quality Recs

recs = particle_data.get_data_by_date(rec_date=test_date)
print("\nHouse Particle sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs))) #format and print House Particle sensor records for date


concentrations = particle_data.get_data_concentrations(data=recs)
print("\tGood Air Quality Recs: {}".format(concentrations["good"])) #format and print Good Air Quality Recs
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"])) #format and print Moderate Air Quality Recs
print("\tBad Air Quality Recs: {}".format(concentrations["bad"])) #format and print Bad Air Quality Recs



#energy_info
energy_data = EnergyData(data)
recs = energy_data.get_data_by_area(rec_area=test_area)
print("\nHouse Energy sensor records for area {} = {}".format(test_area, len(recs))) #format and print House Energy sensor records for area

total_energy = energy_data.calculate_energy_usage(data=recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy)) #format and print total energy usage in watts

recs = energy_data.get_data_by_date(rec_date=test_date)
print("House Energy sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs))) #format and print House Energy sensor records for date

total_energy = energy_data.calculate_energy_usage(data=recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy)) #format and print total energy usage in watts
