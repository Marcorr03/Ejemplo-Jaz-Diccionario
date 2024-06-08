import json
import os

if os.path.exists("archivo.json") and os.path.getsize("archivo.json") > 0:
    with open ("archivo.json","r") as file:
        data=json.load(file)

for i in data["Personas"]:
    if(i["Nombre"]=="Jaz"):
        print(i["Nombre"])
        break
