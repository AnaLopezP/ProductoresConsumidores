#PRUEBA??

from queue import Queue
from threading import Thread
import time

#Creo una cola
cola = Queue(10) #El 10 representa el tamaño máximo

#Creo una función para el productor
def productor(nombre):
    contador = 1
    while True:
        cola.join() #Con esto paramos hasta que todos los bollos se hayan comido
        cola.put(contador) #añadimos el bollo numero contador a la cola
        print(f"{nombre} está horneando el bollo {contador}")
        contador += 1

#Creo una funcion para el consumidor
def consumidor(nombre):
    contador = 1
    while True:
        comer = cola.get() #el cliente coge el bollo de la cola para comérserlo
        print(f"El consumidor {nombre} está comiendo el bollo {contador}")
        contador += 1
        cola.task_done() #Envía una señal de que ha terminado, así el productor puede hornear otro bollo
        time.sleep(3)

#CÓDIGO PRINCIPAL
if __name__ == "__main__":
    #Separamos las tareas en hilos diferentes. En un hilo se hornea y en otro se come
    hilo1 = Thread(target= productor, args=("Din Djarin",))
    hilo2 = Thread(target = consumidor, args=("Grogu",))
    hilo1.start()
    hilo2.start()
