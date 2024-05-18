def factorial(N):
    if (N==0):
        return 1
    return N*factorial(N-1)
        
def factorialNumbers(N):
    factorials=[]
    for i in range(1,N+1):
        fact= factorial(i)
        if (fact <=N):
            factorials.append(fact)
    return factorials
 
print(factorialNumbers(6))
