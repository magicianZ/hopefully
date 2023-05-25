a = 100
b = 115

run = True
def swap(a,b):
    while run == True:
        input("swap")
        if a > b:
            new = a-b
            print(a-new)
            print(b+new)
            return
        elif b > a:
            new1 = b-a
            print(a+new1)
            print(b-new1)
            return
swap(a,b)