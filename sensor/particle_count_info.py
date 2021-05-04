from house_info import HouseInfo
from datetime import datetime
from datetime import date

class ParticleData(HouseInfo): #ParticleData class processes the particle count data field
    def _convert_data(self,data):
        recs = []
        for rec in data:
            recs.append(float(rec)) #The particle field is converted from scientific notation to a float number
        return recs
    
    def get_data_by_area(self, rec_area=0): #method that filters data by area
        recs = super().get_data_by_area("particulate", rec_area) #access get_data_by_area() method of HouseInfo class
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()): #method that filters data by date
        recs = super().get_data_by_date("particulate", rec_date) #access get_data_by_date() method of HouseInfo class
        return self._convert_data(recs)
    
    def get_data_concentrations(self,data):
        particulate = {"good" : 0,"moderate" : 0,"bad" : 0}
        for rec in data: #iterate over data
            if (rec <= 50.0):
                particulate ["good"] += 1
            elif (rec >= 50.0 and rec <=100.0):
                particulate ["moderate"] += 1
            elif (rec >= 100.0):
                particulate ["bad"] += 1
        return particulate

