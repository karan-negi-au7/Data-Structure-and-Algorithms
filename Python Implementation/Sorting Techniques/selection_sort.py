def selection_sort(arr):
  n = len(arr)
  for i in range(n-1):
    minIndex = i
    for j in range(i+1,n):
      if arr[minIndex]>arr[j]:
        minIndex = j
    arr[i],arr[minIndex] = arr[minIndex],arr[i]


arr = [5,8,7,9,6,2,14,6,5]
selection_sort(arr)
print(arr)
