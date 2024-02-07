def insertionsort(mylist):
    for i in range(1,len(mylist)):
        m=i-1
        while m>=0:
            if mylist[m]<mylist[i]:
                mylist[i],mylist[m]=mylist[m],mylist[i]
            m-=1
    
    return mylist

mylist=[45,7,3,12,98,74,52,1,34,49]
print(insertionsort(mylist))    