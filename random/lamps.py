#input = "OOOXOXOOOOXOOO-"
input = "OOXOXOOOOOOO"
def calc(string):
    arr = [x for x in string]
    for x in range(len(arr)-2):
        if arr[x] == "O" and arr[x+1] == "O" and arr[x+2] == "O":
            arr[x+1] = "-"
    return "".join(arr)
print(calc(input))