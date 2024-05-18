def factorialNumbers(N):
        factorials = []
        fact = 1
        for i in range(1, N+1):
            fact *= i
            if fact <= N:
                factorials.append(fact)
            else:
                break
        return factorials
 
print(factorialNumbers(6))
