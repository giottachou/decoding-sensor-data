from house_info import HouseInfo #import HouseInfo class from house_info.py
from datetime import datetime #import datetime from datetime module
from datetime import date #import date from datetime module

class HumidityData(HouseInfo):  #HumidityData class processes the humidity data field
    def _convert_data(self,data): 
        recs = []
        for rec in data: 
            recs.append(float(rec)*100) #The humidity field information is converted from percentage to a float number
        return recs

    def get_data_by_area(self,rec_area=0): #method that filters humidity field data by area
        recs = super().get_data_by_area("humidity",rec_area) #access get_data_by_area() method of HouseInfo class
        return self._convert_data(recs)

    def get_data_by_date(self,rec_date = date.today()): #method that filters humidity field data by date
        recs = super().get_data_by_date("humidity",rec_date) #access get_data_by_date() method of HouseInfo class
        return self._convert_data(recs)
        