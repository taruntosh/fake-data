import time
import random
import csv

class Date:
    def str_time_prop(self, start, end, format, prop):
        """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))
        ptime = stime + prop * (etime - stime)
        return time.strftime(format, time.localtime(ptime))

    def random_date(self, start, end, prop):
        return self.str_time_prop(start, end, '%Y/%m/%d %H:%M:%S', prop)

    #Template date
    def dob(self):
        return self.random_date("1975/12/12 22:59:59", "2002/12/12 22:59:59", random.random())   

    def date(self):
        return self.random_date("2015/12/20 22:59:59", "2020/12/18 22:59:59", random.random())


class Coordinates:
    def __init__(self):
        with open('./assets/coordinates.csv') as f:
            csv_reader = csv.reader(f)
            coordinates = list(csv_reader)
            random_pick_from_list = random.choice(coordinates)
            coordinates = float(random_pick_from_list[0]), float(random_pick_from_list[1])

        self.enter_coord_here = coordinates
        self.original_lat = self.enter_coord_here[0]
        self.added_lat = self.enter_coord_here[0]+0.05
        self.original_long = self.enter_coord_here[1]
        self.added_long = self.enter_coord_here[1]+0.05

    def mate_coordinates(self): # [lat, long]
        lat = round(random.uniform(self.original_lat, self.added_lat), 6)
        lon = round(random.uniform(self.original_long, self.added_long), 6)
        return [lat, lon]

    def room_coordinates(self): # [long, lat]
        lat = round(random.uniform(self.original_lat, self.added_lat), 6)
        lon = round(random.uniform(self.original_long, self.added_long), 6)
        return [lon, lat]

def phone_no():
        return "+91 " + str((random.randint(6123456789, 9987456321)))   