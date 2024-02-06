def selection_sort(list1):
    n=len(list1)
    for i in range(n):
        smallest=list1[i]
        for j in range(i+1,n):
            if list1[j]<smallest:
                