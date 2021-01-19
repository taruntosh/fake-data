from collections import defaultdict
import csv
import random
from faker import Faker
import time
fake = Faker()

def mergeDict(*dict1): #Pass two dictionary as argument - {"a":1},{"b":2}
    merged_dict = {}
    for items in dict1:        
        merged_dict.update({**items})
    return merged_dict # Result is - {"a":1, "b":2}

class Home:
    def home_pic(self):
        columns = defaultdict(list)
        with open('./assets/room_pics.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k,v) in row.items():
                    columns[k].append(v)                          
            home_pic_link = random.sample(set(columns['columns']), (random.randint(1, 10)) )
        return home_pic_link


    def room_code(self):
        room_codes = [
            "CHN-DN87", "CHN-AY57", "CHN-CV76", "CHN-MD84",
            "BNG-WB73", "MUM-XS80", "DEL-HD06", "HYD-NS32",
            "BNG-WB73", "BNG-WB73", "MUM-DL64", "MUM-AQ23",
            "MUM-ML98"
        ]
        return random.choice(room_codes)
    def amenities(self):
        amenities_list = [0,1,2,3,4,5,6,7,8,9]
        return random.sample(set(amenities_list), (random.randint(0,9))) #randint includes start number and end number
    def houseno(self):
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


class Order:
    pass
class Transactions:
    pass
class User:
    def profile_pic(self):
        with open('./assets/profile_pics.csv') as f:
            csv_reader = csv.reader(f)
            profile_pic_links = list(csv_reader)
            random_pick_from_list = random.choice(profile_pic_links)
            profile_pic_link = random_pick_from_list[0]
            return (profile_pic_link)

    def gender(self):
        gender = [
            1, 1, 1,
            0, 0,
            2 
        ]
        return random.choice(gender)
 
    def college(self):
        with open('./assets/colleges.csv') as f:
            csv_reader = csv.reader(f)
            colleges = list(csv_reader)
            random_pick_from_list = random.choice(colleges)
            college_name = random_pick_from_list[0]
        return (college_name)

