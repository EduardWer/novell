import json

with open("gerois.json") as file:
    data = json.load(file)
    for i in data["info"]:

        print(data["info"])

