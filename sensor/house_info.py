from datetime import date #import date from datetime module
from datetime import datetime #import datetime from datetime module

class HouseInfo:
    def __init__(self, data): #HouseInfo class contructor
        self.data = data #assigning the input of data to a class attribute

    def get_data_by_area(self,field,rec_area=0): #method that filters data with rec_area as key and field as value
        field_data = []
        for record in self.data: #iterate over self.data
            if (rec_area == 0):
                field_data.append(record[field])
            elif (rec_area == int(record['area'])):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(self,field,rec_date=date.today()): #method that filters data with rec_date as key and field as value
        field_data = []
        for record in self.data: #iterate over self.data
            if (rec_date.strftime("%m/%d/%y") == record['date']):
                field_data.append(record[field])
        return field_data
