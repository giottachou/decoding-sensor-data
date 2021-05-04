from house_info import HouseInfo #import HouseInfo class from house_info.py
from datetime import datetime #import datetime from datetime module
from datetime import date #import date from datetime module

class EnergyData(HouseInfo): #EneryData class is processing the energy consumption
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0F0

    def _get_energy(self,rec): 
        energy = int(rec,base=16) #The energy field is converted from a hexadecimal number to an integer with base 16 
        energy = energy & self.ENERGY_BITS #apply bitwise operation to isolate the relevant bits
        energy = energy >> 4
        return energy
    
    def _convert_data(self,data):
        recs = []
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs
    
    def get_data_by_area(self, rec_area=0): #method that filters energy field data by area
        recs = super().get_data_by_area("energy_usage", rec_area) #access get_data_by_area() method of HouseInfo class
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()): #method that filters energy field data by date
        recs = super().get_data_by_date("energy_usage", rec_date) #access get_data_by_date() method of HouseInfo class
        return self._convert_data(recs)

    def calculate_energy_usage(self,data):
        total_energy = sum([field * self.ENERGY_PER_BULB for field in data])
        return total_energy

