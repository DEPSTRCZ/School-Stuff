def numinput():
    arr = []
    howmany = int(input("How many magnets you want to input?\n"))
    for num in range(howmany):
        arr.append(str(input("")))
    return arr
def calcmagnets(array):
    count = 0
    for x in range(len(array)-1):
        if array[x] == array[x+1]:
            continue
        else:
            count+=1
    return count
print(calcmagnets(numinput()))