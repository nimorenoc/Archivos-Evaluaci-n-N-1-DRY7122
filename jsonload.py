import json
try:
    with open("myfile.json", "r") as file:
         ourjson = json.load(file)
         print ("Contenido archivo myfile:")
         print (ourjson)
except FileNotFoundError:
    print ("El archivo no se encuentra")
