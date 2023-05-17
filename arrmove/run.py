import keyboard
import time
import random
arr = [["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
        ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
          ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
            ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
              ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
              ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
              ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
              ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
              ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
              ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"],
              ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]]
quit = False
x = 0
y = 0
allienspos = []
allienskilled = 0
def check(y,x):
    global allienskilled
    if arr[y][x] == "👾":
        allienspos.remove([x,y])
        allienskilled+=1

while quit == False:
    if len(allienspos) < random.randint(0,3):
        for loop in range(random.randint(1,6)):
            rpos = [random.randint(0, len(arr[0])-1),random.randint(0, len(arr)-1)]
            if rpos not in allienspos:
                allienspos.append(rpos)
                arr[rpos[1]][rpos[0]] = "👾"
                

    for element in arr:
        arr[y][x] = "🤖"
        print("".join(element))

    match keyboard.read_key():
        case "q":
            quit = True
            print("\033c")
            keyboard.press('ctrl')
            keyboard.press('c')
            keyboard.release('c')
            keyboard.release('ctrl')
            print(f"🟢 Your final score: {allienskilled}")
            exit()
        case "a":
            if x != 0:
                arr[y][x] = "⬛"
                x-=1
                check(y,x)
                time.sleep(0.1)
        case "d":
            if x != len(arr[0])-1:
                arr[y][x] = "⬛"
                x+=1
                check(y,x)
                time.sleep(0.1)
        case "w":
            if y != 0:
                arr[y][x] = "⬛"
                y-=1
                check(y,x)
                time.sleep(0.1)
        case "s":
            if y != len(arr)-1:
                arr[y][x] = "⬛"
                y+=1
                check(y,x)
                time.sleep(0.1)
    print("\033c")
    print(f"🟡 Score: {allienskilled}")