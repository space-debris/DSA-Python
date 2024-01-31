#sum of first n natural numbers
def sumofnat(n):
     if n==1:
         return 1
     return n+sumofnat(n-1)
print(sumofnat(10))

#sum of first n odd natural numbers
def sumofoddnat(n):
    if n==1:
        return 1
    return 2*n-1 +sumofoddnat(n-1)
print(sumofoddnat(10))

def sumofevennat(n):
    if n==1: #first even number
        return 2
    return 2*n +sumofevennat(n-1)
print(sumofevennat(10))

# factorial
def factorial(n):
    if n==1 or n==0:
        return 1 
    else:
        return n*factorial(n-1)
print(factorial(5))

def sumofsq(n):
    if n==1:
        return 1
    else:
        return n*n + sumofsq(n-1)
print(sumofsq(5))