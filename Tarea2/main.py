print("")
print("--------------------------------Formato Json---------------------------------")
import json
def readJson():
    file=open('primero.json',)
    data = json.load(file)
    file.close()
    return  data
dict=readJson()
for primero in dict:
    print(primero)

print("--------------------------------Formato XML----------------------------------")
import xml.etree.ElementTree as ET
archivo= ET.parse('registro2.xml')
raiz=archivo.getroot()
for hijo in raiz:
    for hijo2 in hijo:
        print(hijo2.text)
    print("")
print("")

print("--------------------------------Formato CSV---------------------------------")
import csv
with open('registro3.csv') as f:
    reader = csv.reader(f, delimiter=";")
    for col in reader:
        print("Lugar: {0}, Restaurante: {1}, Comida: {2}, Precio: {3}".format(col[0],col[1],col[2],col[3]))