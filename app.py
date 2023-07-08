"""
    Ejemplo del manejo de hilos
"""

import requests
import time
import csv
import threading
# librería de python que permite ejecutar comandos
import subprocess
import requests
#para verificar si el archivo existe
import os

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for row in lineas:
            fila = row[0].split("|")[0] #obtener el numero
            url = row[0].split("|")[1] #obtener la url
            lista.append([fila, url])
    # se retorna la lista con la información que se necesita
    return lista

def worker(numero, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    #obtener el html de la pagina
    pagina = requests.get(url)
    #guardar en varible el texto del html
    texto_file = pagina.text
    #armar el nombre del archivo a crear
    nombrearchivo = "salida/" + str(numero) + ".txt"
    #verificar si exsite el archivo, para eliminarlo
    if os.path.exists(nombrearchivo):
        os.remove(nombrearchivo)

    #guardar el html como texto (se necesito agregar explicitamente la codificacion de caracteres)
    with open(nombrearchivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto_file)


    time.sleep(10)

    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    # Se crea los hilos
    # en la función
    numero = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='navegando...',
                            target=worker,
                            args=(numero, url))
    hilo1.start()
