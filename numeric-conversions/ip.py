
def dectobin(number):
    num = int(number)
    print(num)
    list = []
    while num > 0:
        n = num%2
        num = num//2
        list.append(n)
    list.reverse()
    result = int("".join(str(x) for x in list))
    return result
def bintodec(num):
    arr = [int(x)for x in str(num)]
    counted = 0
    length = len(arr)
    for x in arr:
        length -= 1
        counted += (2**length*x)
    return counted
    
def decconvert(ip):
    if(ip.find(".") < 3): exit("Not valid ip!")
    elements = ip.split(".")
    result = ""
    for x in elements:
        result += str(dectobin(x))+"."
    return result[:-1]
def binconvert(ip):
    if(ip.find(".") < 3): exit("Not valid ip!")
    elements = ip.split(".")
    result = ""
    for x in elements:
        result += str(bintodec(x))+"."
    return result[:-1]
method = str(input("Enter from what you want to convert:(dec,bin)\n"))
ip = str(input("Enter ip adress to convert:\n"))
if(method == "bin"):
    print(binconvert(ip))
elif(method == "dec"):
    print(decconvert(ip))
else:
    print("Wrong argument - Valid are <dec> or <bin>")
