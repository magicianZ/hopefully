import random
import time


start_time = time.time()
something = input('Hi')
if time.time() - start_time > 3:
    print('er')
if time.time() - start_time < 3:
    something = time.time() - start_time
    print(something)
    print('works')