from bson import ObjectId
from faker import Faker
fake = Faker()
import random
import pprint
from klasfunc import *
from common import Date,Coordinates,phone_no

class GenerateJson:

        
    def home_doc(self):
        return  {"_id": {
                "$oid": str(ObjectId())
                },
            "images": Home().home_pic(),
            "bhk":  random.randint(1,5),
            "room_code": Home().room_code(),
            "monthly_rent": random.randrange(1000,100000,500),
            "security_deposit": random.randrange(10000,1000000,5000),
            "amenities": Home().amenities(),
            "tenant_type": random.randint(0,1),
            "house_restrictions":random.sample(set([0,1,2,3]), (random.randint(0,3))),
            "location": {
                "type": "Point",
                "coordinates": Coordinates().room_coordinates()
            },
            "occupancy_status":  random.randint(0,1),
            "address": fake.address(),
            "furnishing":  random.randint(0,2),
            "conditions": fake.sentence(),
            "house_no": Home().houseno(),
            "landmark": Home().landmark(),
            "property_type":  random.randint(0,1),
            "owner": {
                "owner_id": {
                    "$oid": str(ObjectId())
                },
                "name": fake.name(),
                "phone_no": phone_no(),
                "request_date": {
                    "$date": Date().date()
                },
                "request_status":  random.randint(0,2)
            },
            "current_tenant": {
                "$oid": str(ObjectId())
            },
            "square_feet": random.randint(500,5000),
            "bathrooms": random.randint(1,5),
            "no_of_tenants": random.randint(1,5)
            }
    
    def order(self):
        return {
            "_id": {
                "$oid": str(ObjectId())
                }, 
            "user_id": str(ObjectId()),
            "home_id": str(ObjectId()),
            "order_type":random.randint(0,3) ,
            "created_at": {
                "$date": Date().date()
            },
            "amount":random.randrange(500,10000,500),
            "status":"success",
            "payment_received":{
                "transaction_id" :str(ObjectId()),
                },
             "payment_sent":{
                "transaction_id" :str(ObjectId()) }
        }

    def transactions(self):
        return {
        "_id": {"$oid": str(ObjectId())},
        "amount":random.randrange(500,10000,500) ,
        "order_id":str(ObjectId()),
        "product":"Bunky Homes",
        "user_id":str(ObjectId()) ,
        "gateway": "razorpay",
        "payment_mode":"NEFT",
        "purpose": "payout",
        "utr": str(ObjectId()),
        "transaction_id": str(ObjectId()) ,
        "transaction_status": "",
        "created_at": {
                    "$date": Date().date()
                },
        "fees": 0,
        "tax": 0}


    def user_doc(self):
        return {
        "_id": {
            "$oid": str(ObjectId())
        },
        "user_id": str(ObjectId()),
        "first_name": Faker().first_name(),
        "last_name": Faker().last_name(),
        "dob": {
            "$date": Date().date()
            },
        "gender": random.randint(0,2),
        "phone_no":phone_no() ,
        "occupation": random.randint(0,1),
        "notification_token": str(ObjectId()),
        "schedule_visit": [{
            "home_id":str(ObjectId()) ,
            "schedule_date": {
                    "$date": Date().date()
                },
            "schedule_status":"" ,
            "schedule_id":str(ObjectId()),
            "home_details": {
                "image": Home().home_pic(),
                "property_type":random.randint(0,1) ,
                "room_code": Home().room_code(),
                "address": Faker().address(),
            }
        }],
        "listed_properties": [{
                "home_id": str(ObjectId()),
                "request_status": random.randint(0,2),
                "date": {
                    "$date":  Date().date()
                }
            }],
            
            "has_profile": True,
            "has_bank": True,
            "is_host": True,
            "is_tenant": True,
            "tenant_home_id":str(ObjectId())

            }
