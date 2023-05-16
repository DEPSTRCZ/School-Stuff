arr = [["👾","👾","👾","👾","👾"],
        ["👾","👾","👾","👾","👾"],
          ["👾","👾","👾","👾","👾"],
            ["👾","👾","👾","👾","👾"],
              ["👾","👾","👾","👾","👾"]]
quit = False
x = 0
y = 0

while quit == False:
    for element in arr:
        arr[y][x] = "🪦 "
        print("".join(element))

    move = str(input("Enter\n"))

    match move:
        case "":
            break
        case "q":
            quit = True
            print("\033c")
            exit()
        case "a":
            if x != 0:
                arr[y][x] = "👾"
                x-=1
        case "d":
            if x != 4:
                arr[y][x] = "👾"
                x+=1
        case "w":
            if y != 0:
                arr[y][x] = "👾"
                y-=1
        case "s":
            if y != 4:
                arr[y][x] = "👾"
                y+=1
    print("\033c")

