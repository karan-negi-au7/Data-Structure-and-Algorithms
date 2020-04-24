def insertion_sort(list):
    n = len(list)
    for i in range(1,n):
        temp = list[i]
        j = i-1
        while j>=0 and list[j]>temp:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = temp
    return list    



print(insertion_sort([5,8,4,2,1,0,6,7,3]))     
           
