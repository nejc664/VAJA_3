import json 

person ={
    "name" : "Alice",
    "age" : 30,
    "addresses":{
        "street" : "Dunajska",
        "city" :  "Ljubljana"
    },
    "married" : True
}

with open('/home/nejc/VAJE/VAJE-3/DATA/POMOC/person.json','w') as f:
    json.dump(person, f, indent=4, sort_keys=False)