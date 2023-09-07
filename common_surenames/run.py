dict = {}
with open("C:\\Users\\jirie\\Desktop\\GIT\\ŠKOLA\\School-Things\\common_surenames\\KSP\\05.in") as f:
    input = f.readlines()
input.pop(0)
for elem in input:
    if elem.strip() in dict:
        dict[elem.strip()] += 1
    else: dict[elem.strip()] = 0
maxindex = list(dict.values()).index(max(dict.values()))
with open("C:\\Users\\jirie\\Desktop\\GIT\\ŠKOLA\\School-Things\\common_surenames\\KSP\\Out\\05.out","w") as f:
    f.write(f"{list(dict.keys())[maxindex]} {max(dict.values())+1}")