# recursive function to print first n natural numbers

def naturalnumbers(n):
    if n>0:
        naturalnumbers(n-1)
        print(n,end=" ")
#naturalnumbers(5)

def naturalnumbersrev(n):
    if n>0:
        print(n,end=" " )
        naturalnumbersrev(n-1)
#naturalnumbersrev(5)

def oddnatunum(n):
    if n>0:
        oddnatunum(n-1)
        print(2*n-1,end=" ")
oddnatunum(10)