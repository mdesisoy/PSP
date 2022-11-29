import os
import multiprocessing
from multiprocessing import Pool

# Exercise 1: Using the multiprocessing module, write a simple python program as follows:
# Create a pool of workers to run parallel tasks.
# The pool size should be the number of CPU cores available on your node minus 1 (8cores > pool of 7 workers).
# Write a function to be running in parallel, call it my_id. The function should receive as input the task id.
# When called, the function will print to the screen a message in the form: 
# “Hi, I’m worker ID (with PID)” 
# Where ID should be replaced with the task number assigned to the worker and PID with the process ID of the running worker.
# Run tasks in parallel using the map function, for a total of tasks equal to twice the number of CPU cores in your node.

def my_id(ID):
    print('Hi, I\'m worker ID ' + str(ID) + ' (with PID ' + multiprocessing.current_process().name[-1] + ')')

def exercise1():
    pool_size = os.cpu_count() - 1
    if __name__ == '__main__':
        with Pool(pool_size) as p:
            p.map(my_id, range(1,os.cpu_count()*2+1))

# Exercise 2: Using the multiprocessing module, write a simple python program as follows:
# Create a pool of workers to run parallel tasks.
# The pool size should be 2.
# Write a function to be running in parallel, call it print_cube. 
# The function should receive as input a number [num]. When called, 
# the function will print to the screen a message in the form: “The cube of number [num] is [cube]”. 
# Where [cube] should be replaced with the cube of the number received as input.
# Write a function to be running in parallel, call it print_square. 
# The function should receive as input a number [num]. 
# When called, the function will print to the screen a message in the form: “The square of number [num] is [square]”. 
# Where [square] should be replaced with the square of the number received as input.

def print_cube(num):
    print('The cube of number %d is %d' % (num, num**3))

def print_square(num):
    print('The square of number %d is %d' % (num, num**2))

def exercise2():
    if __name__ == '__main__':
        with Pool(2) as p:
            p.map(print_cube, range(3, 6))
            p.map(print_square, range(3, 6))

exercise1()
exercise2()