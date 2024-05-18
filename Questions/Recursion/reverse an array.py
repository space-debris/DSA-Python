array=[1,2,3,4,5,6,7,8,9]

def reverse(arr,i):
    n=len(arr)
    if i>=n/2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    reverse(arr,i+1)
    return arr
    
print(reverse(array,0))