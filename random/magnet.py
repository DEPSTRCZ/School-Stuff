#magneti = "+-+--++--"
#negative = magneti.split("+-")
#print(negative)
num = 0
for x in negative:
    if x == "-+":
        print("negr")
        num+=1

print(num*2)

#def calcmagnets(string):
 #   num = 0
 #   for x in string.split("+-"):
 #       if x == "-+":
 #           num+=1
 #   return num*2

#print(calcmagnets("+-+--++--+"))


#+-+--++--+