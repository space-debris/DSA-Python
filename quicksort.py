def quicksort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot=list1[0]
        lesser=[x for x in list1[1:] if x<=pivot]
        greater=[x for x in list1[1:] if x>pivot]
        return quicksort(lesser)+[pivot]+quicksort(greater)
 
mylist=[42,58,74,96,54,21,3,45,85]       
print(quicksort(mylist))