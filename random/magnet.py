# magneti = ["+-",
#            "+-",
#            "-+",
#            "+-",
#            "+-",
#            "-+"]
magneti = ["-+",
           "-+",
           "+-",
           "-+",
           "-+",
           "+-",
           "-+",
           "-+",
           "+-",
           "-+"]
indexes = 0

for x in range(len(magneti)-1):
    if magneti[x] == magneti[x+1]:
        continue
    else:
        indexes+=1
    

print(indexes)
