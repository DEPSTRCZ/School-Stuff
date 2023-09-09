with open("bulldozer\KSP\i\\02.in") as f:
    lines = f.readlines()
    f.close()
bul = list(map(int,lines[0].strip().split(" ")))
box = list(map(int,lines[1].strip().split(" ")))
movment = list(lines[2].strip())

def calc(axis,op):
    if op == "+":
        bul[axis] += 1
        if bul == box:
            box[axis] += 1
    elif op == "-":
        bul[axis] -= 1
        if bul == box:
            box[axis] -= 1

for step in movment:
    match(step):
        case "P": calc(0,"+")
        case "L": calc(0,"-")
        case "D": calc(1,"-")
        case "N": calc(1,"+")

with open("bulldozer\KSP\o\\02.out","w") as f:
    f.write(f"{' '.join(map(str,bul))}\n{' '.join(map(str,box))}")
    f.close()