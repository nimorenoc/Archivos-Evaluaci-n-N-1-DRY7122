import json
try:
    with open("myfile.json", "r") as file:
        json_file = json.load(file)
        print ("archivo myfile.json:")
        print (json_file)
except FileNotFoundError:
    print("El archivo no se encuentra")
