from lxml import etree as t
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from xml.etree import ElementTree as ET



def load_file(ruta):
    #Tk().withdraw()
    tree = t.parse(ruta)
    elements = tree.load_file()
    filename = askopenfilename()
    xml_tree = ET.parse(filename)
    xml_root = xml_tree.getroot()
    print(xml_tree)

load_file()