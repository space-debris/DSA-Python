def selection_sort(list1):
    n=len(list1)
    for i in range(n):
        smallest=i
        for j in range(i+1,n):
            if list1[j]<list1[smallest]:
                smallest=j
        list1[i], list1[smallest] = list1[smallest], list1[i]        
        
                
    return list1
  
list1=[84,75,9,21,56,73,31,56,94]
print(selection_sort(list1))