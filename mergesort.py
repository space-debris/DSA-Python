def mergesort(mylist):
    
    if len(mylist)<=1:
        return mylist
    
    else:
        temp=len(mylist)//2
        list1=[mylist[x] for x in mylist if x<temp and x>=0]
        list2=[mylist[x] for x in mylist if x>=temp and x<len(mylist)]
        mergesort(list1)
        mergesort(list2)

mylist=[45,85,41,65,78,98,54,12,58]
    