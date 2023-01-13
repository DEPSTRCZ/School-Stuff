lines = int(input("Enter number of lines\n"))
line = 0 
output = ""
for line in range(lines):
    for i in range(lines - line):
        output += " "
    for x in range(line2-1):
        output += "" 
    output += "\n"
print(output)
