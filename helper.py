import klass.common as klass
fake = klass.fake
random = klass.random
user = klass.Users()
mate = klass.Mates()
room = klass.Rooms()
coord = klass.Coordinates()
date = klass.Date()

def mergeDict(*dict1):
    merged_dict = {}
    for items in dict1:        
        merged_dict.update({**items})
    return merged_dict

class GenerateJson: 
    def __init__(self, is_mate=None, is_host=None, value=None):
        self.is_mate = is_mate
        self.is_host = is_host   
        self.value = value     
        
    def do_it(self):

        if self.value == "mate":
            if self.is_mate == True and self.is_host == True:
                self.is_host == True
                final = mergeDict(self.user_generate(),self.mate_generate())
                return final
            if self.is_mate == True and self.is_host == False:
                self.is_host == False
                final = mergeDict(self.user_generate(),self.mate_generate())
                return final
            if self.is_mate == False and self.is_host == True:
                self.is_host == True
                finall = mergeDict(self.user_generate())
                return finall
            if self.is_mate == False and self.is_host == False:
                self.is_host == False
                finall = mergeDict(self.user_generate())
                return finall
        
    def do_it1(self):
        
        if self.value == "host":
            if self.is_mate == True and self.is_host == True:
                self.is_mate == True
                final = self.room_generate()
                return final
            if self.is_mate == True and self.is_host == False:
                self.is_mate == True
                final = None
                return "remove_this"
            if self.is_mate == False and self.is_host == True:
                self.is_mate == False
                final = self.room_generate()
                return final
            if self.is_mate == False and self.is_host == False:
                self.is_mate == False
                final = None
                return "remove_this"

        



    def user_generate(self):
        user_template = {
            "user_id": _oid,
            "profile_pic":_profile_pic,
            "name": _name,        
            "gender": user.gender(),
            "email": fake.email(),
            "phone_no": user.phone_no(),
            "company": fake.company(),
            "college": user.college(),
            "about": fake.sentence(),
            "is_mate": self.is_mate,
            "is_host": self.is_host,            
            "DOB": {"$date": date.dob()},
            "occupation": (random.randint(0,2))
        }
        return user_template
    
    def mate_generate(self):
        mate_template = {        
            "mate_post": {
            "prefer_sex": mate.prefer_sex(),
            "budget": mate.budget(),
            "prefer_room_type": random.randint(0,2),
            "available_from": {"$date": date.mate_available_from_date()},
            "house_restrictions" : mate.hres(),
            "mate_loc": {
                "type": "MultiPoint",
                "coordinates": [coord.mate_coordinates(), coord.mate_coordinates(), coord.mate_coordinates()]
                }
            }
        }
        return mate_template
    
    def room_generate(self):
        room_template = {
            "hosted_by": {
                "user_id": _oid,
                "profile_pic": _profile_pic,
                "name": _name,
            },
            "room_pic": room.room_pic(),
            "room_type": random.randint(0,2),
            "room_code": room.room_code(),
            "price": room.price(),
            "room_sex": random.randint(0,2),
            "address": fake.address(),
            "amenities": room.amenities(),
            "room_about": fake.sentence(),
            "room_loc": {
                "type": "Point",
                "coordinates": coord.room_coordinates(),
            },
            "nop" : room.nop(),
            "attached_bathroom": random.randint(0,1),
            "flatno" : room.flatno(),
            "landmark" : room.landmark(),
            "house_restrictions" : room.hres(),
            "owner_type" : (random.randint(0,2))        
        }
        return room_template




# print(gs.do_it())
# import json
# print(json.dumps(gs.do_it(), indent=4, sort_keys=False))

############################################################################################################################################################################################################

# import klass.common as klass
# fake = klass.fake
# random = klass.random
# user = klass.Users()
# mate = klass.Mates()
# room = klass.Rooms()
# coord = klass.Coordinates()
# date = klass.Date()

# def mergeDict(*dict1):
#     merged_dict = {}
#     for items in dict1:        
#         merged_dict.update({**items})
#     return merged_dict

# class GenerateJson:

#     def __init__(self, is_mate=None, is_host=None):
#         self.is_mate = is_mate
#         self.is_host = is_host        
    
#     def do_it(self):
#         if self.is_mate == True and self.is_host == True:
#             final = mergeDict(self.user_generate(),self.mate_generate(), self.room_generate())
#             return final
        
#         elif self.is_mate == True and self.is_host == False:
#             user =  mergeDict(self.user_generate(),self.mate_generate())
#             return user

#         elif self.is_mate == False and self.is_host == True:
#             user =  mergeDict(self.user_generate(),self.room_generate())
#             return user
        
#         else:
#             user =  self.user_generate()
#             return user
    
#     def do_it1(self):
#         if self.is_mate == True and self.is_host == True:
#             final = mergeDict(self.user_generate(),self.mate_generate(), self.room_generate())
#             return final
        
#         elif self.is_mate == True and self.is_host == False:
#             user =  mergeDict(self.user_generate(),self.mate_generate())
#             return user

#         elif self.is_mate == False and self.is_host == True:
#             user =  mergeDict(self.user_generate(),self.room_generate())
#             return user
        
#         else:
#             user =  self.user_generate()
#             return user


#     def user_generate(self):
#         user_template = {
#             "user_id": _oid,
#             "profile_pic":_profile_pic,
#             "name": _name,        
#             "gender": user.gender(),
#             "email": fake.email(),
#             "phone_no": user.phone_no(),
#             "company": fake.company(),
#             "college": user.college(),
#             "about": fake.sentence(),
#             "is_mate": self.is_mate,
#             "is_host": self.is_host,            
#             "DOB": {"$date": date.date()},
#             "occupation": (random.randint(0,2))
#         }
#         return user_template
    
#     def mate_generate(self):
#         mate_template = {        
#             "mate_post": {
#             "prefer_sex": mate.prefer_sex(),
#             "budget": mate.budget(),
#             "prefer_room_type": random.randint(0,2),
#             "available_from": {"$date": date.date()},
#             "house_restrictions" : mate.hres(),
#             "mate_loc": {
#                 "type": "MultiPoint",
#                 "coordinates": [coord.mate_coordinates(), coord.mate_coordinates(), coord.mate_coordinates()]
#                 }
#             }
#         }
#         return mate_template
    
#     def room_generate(self):
#         room_template = {
#             "hosted_by": {
#                 "user_id": _oid,
#                 "profile_pic":_profile_pic,
#                 "name": _name,
#             },
#             "room_pic": room.room_pic(),
#             "room_type": random.randint(0,2),
#             "room_code": room.room_code(),
#             "price": room.price(),
#             "room_sex": random.randint(0,2),
#             "address": fake.address(),
#             "amenities": room.amenities(),
#             "room_about": fake.sentence(),
#             "room_loc": {
#                 "type": "Point",
#                 "coordinates": coord.room_coordinates(),
#             },
#             "nop" : room.nop(),
#             "attached_bathroom": random.randint(0,1),
#             "flatno" : room.flatno(),
#             "landmark" : room.landmark(),
#             "house_restrictions" : room.hres(),
#             "owner_type" : (random.randint(0,2))        
#         }
#         return room_template

        


# # print(gs.do_it())
# # import json
# # print(json.dumps(gs.do_it(), indent=4, sort_keys=False))
