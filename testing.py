import threading

def f1():
    print('f1')
def f2():
    print('f2')
def f3():
    print('f3')
def f4():
    print('f4')
def f5():
    print('f5')

t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
t1 = threading.Thread(target=f3)
t2 = threading.Thread(target=f4)
t1.start()
t2.start()
t1.join()
t2.join()
f5()