# Implementa en python un codigo de Productor Consumidor mediante cola sincronizada tal que:
# 1 El productor produce años de nacimiento que los almacena en la cola 
#       y el tiempo de espera entre la generacion de un numero y otro es de 1 segundos
# 2 El consumidor lee los años e indica si el año correspondonte es bisiesto o no 

# el productor y el consumidor tienen que ser clases que no hereden de ninguna clase

# el tiempo de espera entre la lectura de completa una cola y la siguiente lectura completa es de es de 4 segundos
# Prueba el algoritmo con una relacion de productor:consumidor de     
# 
# 1:1   
# 3:2
# 2:10

import multiprocessing
import time
import random
import queue

class Productor(multiprocessing.Process):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            time.sleep(1)
            year = random.randint(1, 9999)
            self.q.put(year)
            # print('Hay ' + str(q.qsize()) + ' año/s en la cola')

class Consumidor(multiprocessing.Process):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            time.sleep(4)
            try:
                year = self.q.get(timeout=1)
                comprobar_bisiesto(year)
            except queue.Empty:
                print('La cola está vacía')
                break

def comprobar_bisiesto(year):
    if year % 4 != 0: #no divisible entre 4
        print('El año %d no es bisiesto' % year)
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
        print("El año %d es bisiesto" % year)
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
        print("El año %d no es bisiesto" % year)
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
        print("El año %d es bisiesto" % year)

def exercise(num_productores, num_consumidores):
    q = multiprocessing.Queue()
    productores     = [Productor(q) for _ in range(num_productores)]
    consumidores    = [Consumidor(q) for _ in range(num_consumidores)]

    for p in productores:
        p.start()
    for c in consumidores:
        c.start()

    for p in productores:
        p.join()
    for c in consumidores:
        c.join()

# ahora vamos a realizar las pruebas usando el from queue import Queue y el import threading

from queue import Queue
import threading

class Productor(threading.Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            time.sleep(1)
            year = random.randint(1, 9999)
            self.q.put(year)
            # print('Hay ' + str(q.qsize()) + ' año/s en la cola')

class Consumidor(threading.Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            time.sleep(4)
            try:
                year = self.q.get(timeout=1)
                comprobar_bisiesto(year)
            except queue.Empty:
                print('La cola está vacía')
                break

def exercise2(num_productores, num_consumidores):
    q = Queue()
    productores     = [Productor(q) for _ in range(num_productores)]
    consumidores    = [Consumidor(q) for _ in range(num_consumidores)]

    for p in productores:
        p.start()
    for c in consumidores:
        c.start()

    for p in productores:
        p.join()
    for c in consumidores:
        c.join()

if __name__ == '__main__':
    # exercise(1, 1)
    # exercise(3, 2)
    # exercise(2, 10)
    # exercise2(1, 1)
    # exercise2(3, 2)
    exercise2(2, 10)