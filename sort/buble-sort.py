arr = [1,5,-100,10,1001,24,15,30,80,100,-5]
def bublesort(array):
    for loop in array:
        for pos in range(len(arr)-1):
            if array[pos] > arr[pos+1]:
                array[pos],array[pos+1] = array[pos+1],array[pos]
    return array
print(bublesort(arr))


