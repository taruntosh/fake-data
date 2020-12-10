import time
import csv
import random
from collections import defaultdict
from bson import ObjectId
from faker import Faker

def oid():
    return (str(ObjectId()))


# Gives fake ---> Email, Company, Address, Sentences(for ABOUT/BIO)
fake = Faker()


class Users:

    def user_id(self):
        return str(ObjectId())

    def profile_pic(self):
        with open('./assets/profile_pics.csv') as f:
            csv_reader = csv.reader(f)
            profile_pic_links = list(csv_reader)
            random_pick_from_list = random.choice(profile_pic_links)
            profile_pic_link = random_pick_from_list[0]
            return (profile_pic_link)

    def name(self):
        with open('./assets/names.csv') as f:
            csv_reader = csv.reader(f)
            names = list(csv_reader)
            random_pick_from_list = random.choice(names)            
            firstname = random_pick_from_list[0]
            lastname = random_pick_from_list[1]
            fullname = firstname, lastname
        return (" ".join([str(s) for s in list(fullname)]))

    def gender(self):
        gender = [
            1, 1, 1, 1, 1,
            0, 0, 0, 0,
            2 
        ]
        return random.choice(gender)
 
    def phone_no(self):
        return "+91 " + str((random.randint(6123456789, 9987456321)))   
 
    def college(self):
        with open('./assets/colleges.csv') as f:
            csv_reader = csv.reader(f)
            colleges = list(csv_reader)
            random_pick_from_list = random.choice(colleges)
            college_name = random_pick_from_list[0]
        return (college_name)

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
        return self.str_time_prop(start, end, '%Y/%m/%d %H:%M:%S', prop) #"%Y-%m-%d %H:%M:%S"          #%m/%d/%Y %I:%M %p

    def dob(self):
        return self.random_date("2001/12/12 22:59:59", "1980/12/12 22:59:59", random.random())    #2015/12/20 1:30 PM
    
    def mate_available_from_date(self):
        return self.random_date("2020/12/01 22:59:59", "2021/01/20 22:59:59", random.random())

    def room_available_from_date(self):
        return self.random_date("2015/12/20 22:59:59", "2020/12/18 22:59:59", random.random())


"""
Same co-ordinates(lat & long) applies for both 
[Rooms - Point] and [Mates - MultiPoint] 
"""

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

# print(Coordinates().mate_coordinates())
# print(Coordinates().room_coordinates())


class Mates:
    def budget(self):
        start = 1000
        end = 100000
        step = 1000
        return (random.randrange(start, end, step))

    def hres(self):
        no_of_hres = 2
        hres = list((random.randint(0,1)) for i in range(no_of_hres))
        return (hres)

    def prefer_sex(self):
        prefer_sex = [
            1, 1, 1, 1, 1,
            0, 0, 0, 0,
            2 
        ]
        return random.choice(prefer_sex)



class Rooms:
    def room_pic(self):
        columns = defaultdict(list)
        with open('./assets/room_pics.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k,v) in row.items():
                    columns[k].append(v)                          
            room_pic_link = random.sample(set(columns['columns']), (random.randint(1, 10)) )

        return room_pic_link


    def room_code(self):
        room_codes = [
            "CHN-DN87", "CHN-AY57", "CHN-CV76", "CHN-MD84",
            "BNG-WB73", "MUM-XS80", "DEL-HD06", "HYD-NS32",
            "BNG-WB73", "BNG-WB73", "MUM-DL64", "MUM-AQ23",
            "MUM-ML98"
        ]
        return random.choice(room_codes)

    def price(self):
        start = 1000
        end = 100000
        step = 1000
        return (random.randrange(start, end, step))

    def amenities(self):
        amenities_list = [0,1,2,3,4,5,6,7,8,9]
        return random.sample(set(amenities_list), (random.randint(0,9)))
    
    def nop(self):
        nop = list((random.randint(0,5)) for i in range(3))
        while True:            
            if (nop[0] | nop[1] | nop[2])!=0:
                return nop
            else:
                nop = list((random.randint(0,1)) for i in range(3))
    
    def flatno(self):
        flat_nums = [
            "#9/55", "#8", "#6a", "42",
            "F-3 1st floor", "no.34, S-3", "new no.4a/old no. #62",
            "12, Yoman apartments", "7, Roy palace 25th floor"
        ]
        return random.choice(flat_nums)

    def landmark(self):
        landmarks = [
            "Nvdia showroom", "Samsung mobile",
            "kfc", "McDonalds", "ktm showroom"
        ]
        return random.choice(landmarks)

    def hres(self):
        no_of_hres = 4
        hres = list((random.randint(0,1)) for i in range(no_of_hres))
        return (hres)
