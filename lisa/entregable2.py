# -*- coding: utf-8 -*-
"""entregable1.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nick9vsI-eJB3eMmdeVzvFDFG0vi8qI0
"""



from cgitb import text
from distutils.file_util import copy_file, move_file
from genericpath import exists
from importlib.resources import path
from itertools import count
from pickle import APPEND
from re import X
from tkinter.filedialog import SaveAs
from zipapp import create_archive
import requests
import time
import csv
import os
import pandas
import numpy
import shutil
from pandas import DataFrame
from csv import writer
from csv import DictWriter

#frases=requests.get("https://thesimpsonsquoteapi.glitch.me/quotes"


#print(frases.status_code)

#print(frases.json())

#print(frases.json()[0]["quote"])

def tiempoPeticion():
  for i in range(20):
    frases=requests.get("https://thesimpsonsquoteapi.glitch.me/quotes"
)
    texto=frases.json()[0]["quote"]
    personaje=frases.json()[0]["character"]
    imagen=frases.json()[0]["image"]
    print(texto)
    print(personaje)
    print(imagen)
    time.sleep(10)
    data={"quote":texto,"character":personaje,"image":imagen}
    def repe():
        cuentaThe=texto.count(' the ')
        cuentaGreat=texto.count(' great ')
        theList=[cuentaThe]
        greatList=[cuentaGreat]
        dict1:dict={'The':theList, 'Great': greatList}
        print(f'La palabra "the" aparece {cuentaThe} veces')
        print(f'La palabra "great" aparece {cuentaGreat} veces')
        df = pandas.DataFrame(dict1)
        df.to_csv('file.csv')

    def crearCarpeta():
        carpeta=os.path.exists(personaje) 
        if carpeta == True:
            with open('file.csv','a', newline='') as g: 
                a=csv.DictWriter(g,data.keys())
                a.writerow(data)
    
        if carpeta == False:
            os.mkdir(personaje)
            ruta=os.path.basename(personaje)
            with open('file.csv','a', newline='') as h: 
                a=csv.DictWriter(h,data.keys())
                a.writerow(data)
            move_file('file.csv',ruta)   
        repe()
    crearCarpeta()

tiempoPeticion()
