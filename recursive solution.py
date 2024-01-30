# recursive function to print first n natural numbers

def naturalnumbers(n):
    if n>0:
        naturalnumbers(n-1)
        print(n)
#naturalnumbers(5)

def naturalnumbersrev(n):
    if n>0:
        print(n)
        naturalnumbersrev(n-1)
naturalnumbersrev(5)