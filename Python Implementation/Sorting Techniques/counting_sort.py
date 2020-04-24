def countintSort(givenArray):
    countArray = [0]*(max(givenArray)+1)
    for i in givenArray:
        countArray[i] += 1
    countArrayLength =  len(countArray)
    newArray = []
    for j in range(countArrayLength):
        for k in range(countArray[j]):
            newArray.append(j)
    return (newArray)        

givenArray = [5,6,4,3,2,8]
print(countintSort(givenArray))