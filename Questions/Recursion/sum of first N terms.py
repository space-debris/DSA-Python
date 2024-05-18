
def sumOfSeries(n):
        if (n==0):
            return 0
        else:
            return n+sumOfSeries(n-1)

    
m=sumOfSeries(7)
print(m)