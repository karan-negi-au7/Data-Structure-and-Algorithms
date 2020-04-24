
def partition(arr,l,h):
    i = l
    j = h
    while(i<j):
        while arr[i]<=arr[l]:
            i+=1
        while arr[j]>arr[l]:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[l],arr[j] = arr[j],arr[l]
    return j                


def quick_sort(arr,l,h):
    if (l<h):
        loc = partition(arr,l,h)
        quick_sort(arr,l,loc-1)
        quick_sort(arr,loc+1,h)


arr = [6,4,2,9,7,8,9,3,5,3,4]    
quick_sort(arr,0,len(arr)-1)
print(arr)