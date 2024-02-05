def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                
def mod_bubble_sort(data_list):
    flag=False
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag: #when flag False
            break





l= [34,67,12,89,25,50]
bubble_sort(l)  
print(l)     
print(mod_bubble_sort(l))     
    