def insertionsort(mylist):
    for i in range(1,len(mylist)):
        temp=mylist[i]
        m=i-1
        while m>=0:
            if mylist[m]<mylist[i]:
                mylist[i],mylist[m]=mylist[m],mylist[i]
    
    return mylist
                 
    