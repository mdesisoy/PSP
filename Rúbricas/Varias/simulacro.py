# Implementa en python un codigo de Productor Consumidor mediante cola sincronizada tal que:
# 1 El productor produce años de nacimiento que los almacena en la cola 
#       y el tiempo de espera entre la generacion de un numero y otro es de 1 segundos
# 2 El consumidor lee los años e indica si el año correspondonte es bisiesto o no 

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

def productor(q):
    while True:
        time.sleep(1)
        year = random.randint(1, 9999)
        q.put(year)
        # print('Hay ' + str(q.qsize()) + ' año/s en la cola')
    
def consumidor(q):
    while True:
        time.sleep(4)
        try:
            year = q.get(timeout=1)
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

# 1:1
def exercise(num_productores, num_consumidores):
    if __name__ == '__main__':
        q = multiprocessing.Queue()
        for _ in range(num_productores):
            p = multiprocessing.Process(target=productor, args=(q,))
            p.start()
        for _ in range(num_consumidores):
            c = multiprocessing.Process(target=consumidor, args=(q,))
            c.start()
        for _ in range(num_productores):
            p.join()
        for _ in range(num_consumidores):
            c.join()

if __name__ == '__main__':
    exercise(2, 10)