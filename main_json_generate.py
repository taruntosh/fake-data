import json
import klass.common as klass
import helper as rg
from faker import Faker

# Gives fake ---> Email, Company, Address, Sentences(for ABOUT/BIO)
fake = Faker()

mate_json = []
room_json = []

for i in range(1000):    
    rg._oid = klass.oid()
    rg._profile_pic = klass.Users().profile_pic() 
    rg._name = fake.name()   
    #
    sample1 = rg.GenerateJson(is_mate=True, is_host=True, value="mate").do_it()
    sample11 = rg.GenerateJson(is_mate=True, is_host=True, value="host").do_it1()
    
    mate_json.extend([sample1])
    room_json.extend([sample11])

    rg._oid = klass.oid()
    rg._profile_pic = klass.Users().profile_pic() 
    rg._name = fake.name()
    #
    sample2 = rg.GenerateJson(is_mate=True, is_host=False, value="mate").do_it()

    mate_json.extend([sample2])
   

    rg._oid = klass.oid()
    rg._profile_pic = klass.Users().profile_pic() 
    rg._name = fake.name()
    #
    sample3 = rg.GenerateJson(is_mate=False, is_host=True, value="mate").do_it()
    sample33 = rg.GenerateJson(is_mate=False, is_host=True, value="host").do_it1()

    mate_json.extend([sample3])
    room_json.extend([sample33])

    rg._oid = klass.oid()
    rg._profile_pic = klass.Users().profile_pic() 
    rg._name = fake.name()    #
    sample4 = rg.GenerateJson(is_mate=False, is_host=False, value="mate").do_it() 

    mate_json.extend([sample4])





    

    
##########  is_mate     USER/MATE-USER/MATE-USER/MATE-USER/MATE-USER/MATE
json_object = json.dumps(mate_json, indent=4)
with open("./json-ready/users_xx_yy_zz.json", "a") as outfile:
    outfile.write(json_object)
    outfile.write(",\n\n\n")     

##########  is_host     ROOM/HOST-ROOM/HOST-ROOM/HOST-ROOM/HOST-ROOM/HOST
json_object = json.dumps(room_json, indent=4)
with open("./json-ready/rooms_xx_yy_zz.json", "a") as outfile:
    outfile.write(json_object)
    outfile.write(",\n\n\n")
 

  