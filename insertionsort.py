def insertionsort(mylist):
    for i in range(1,len(mylist)):
        temp=mylist[i]
        m=i-1
        while m>=0 and temp<mylist[m]:
            mylist[m+1]=mylist[m]
            m-=1
        mylist[m+1]=temp
    
    return mylist

mylist=[45,7,3,12,98,74,52,1,34,49]
print(insertionsort(mylist))    