from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from xml.etree import ElementTree as data


def Menu():
    while True:
        print("-----MENÚ-----")
        print(" 1. Cargar XML ")
        print(" 2. Elegir Patrón ")
        print(" 3. Mostrar Gráfica del Patrón ")
        print(" 4. Seleccionar Código de Patrón ")
        print(" 5. Salir ")
        opción = input("Elija una opción para continuar: ")
        
        if opción == "1":
            print("XML")
            load_file("archivoprueba.xml")
        elif opción == "2":
            print("Patrón")
        elif opción == "3":
            print ("Gráfica")
        elif opción == "4":
            print("Código")
        elif opción == "5":
            print("Vuelve Pronto :) ")
            break
        else:
            print("Ingrese una opción válida.... ")

def load_file(ruta):
    #Tk().withdraw()
    tree = data.parse(ruta)
    xml_root = tree.getroot()
    print(xml_root)

    print("Atributos")
    for element in xml_root:
        for subelement in element:
            print(subelement.attrib)
    print("Valores")
    for element in xml_root:
        for subelement in element:
            print(subelement.tag)
            print(subelement.text)


Menu()
