import json
from template_doc import GenerateJson
"""
#extend works like mergeDict
"""
home_json = []
order_json = []
transactions_json = []
user_json = []

for i in range (10):

    home_temp = GenerateJson().home_doc()
    home_json.extend([home_temp]) 

    order_temp = GenerateJson().home_doc()
    order_json.extend([home_temp])

    transactions_temp = GenerateJson().home_doc()
    transactions_json.extend([home_temp])

    user_temp = GenerateJson().home_doc()
    user_json.extend([home_temp])
    

json_object = json.dumps(home_json, indent=4)
with open("./mongojsondocuments/home_xx_yy_zz.json", "a") as outfile:
    outfile.write(json_object)
    outfile.write(",\n\n\n")

json_object = json.dumps(order_json, indent=4)
with open("./mongojsondocuments/order_xx_yy_zz.json", "a") as outfile:
    outfile.write(json_object)
    outfile.write(",\n\n\n")

json_object = json.dumps(transactions_json, indent=4)
with open("./mongojsondocuments/transactions_xx_yy_zz.json", "a") as outfile:
    outfile.write(json_object)
    outfile.write(",\n\n\n")

json_object = json.dumps(user_json, indent=4)
with open("./mongojsondocuments/user_xx_yy_zz.json", "a") as outfile:
    outfile.write(json_object)
    outfile.write(",\n\n\n")

