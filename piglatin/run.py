prompt=str(input("Zadejte větu\n"))
def topig(string):
    stringarr = string.split(" ")
    result = ""
    for element in stringarr:
        result += f"{element[1:]+element[0]}ay "
    return result
print(topig(prompt))