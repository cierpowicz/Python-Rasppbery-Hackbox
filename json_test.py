import json


data = {
    'kanapka':{
        "name":"hoddog-bułka",
        "type":"kurczak"
    }
}


siemanko = json.dumps(data)

print (siemanko)

