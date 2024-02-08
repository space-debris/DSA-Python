def mergesort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        leftlist = mylist[:mid]
        rightlist = mylist[mid:]

        leftlist = mergesort(leftlist)
        rightlist = mergesort(rightlist)

        i = j = k = 0
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                mylist[k] = leftlist[i]
                i += 1
            else:
                mylist[k] = rightlist[j]
                j += 1
            k += 1

        while i < len(leftlist):
            mylist[k] = leftlist[i]
            k += 1
            i += 1

        while j < len(rightlist):
            mylist[k] = rightlist[j]
            k += 1
            j += 1

    return mylist

listy = [45, 85, 41, 65, 78, 98, 54, 12, 58]
sorted_listy = mergesort(listy)
print(sorted_listy)