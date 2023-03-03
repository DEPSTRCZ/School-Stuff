arr = [1,5,10,24,15,30,80,100,-5]
for pos in range(len(arr)-1):
    for val in arr:
        #print(arr[pos]==val)
        #print(pos,arr[pos],val)
            #-print(min(val,arr[pos+1]))
        print(arr[pos],arr[pos+1],val)
        if arr[pos] > arr[pos+1]:
            arr[pos] = arr[pos+1]
            arr[pos+1] = arr[pos]
print(arr)
