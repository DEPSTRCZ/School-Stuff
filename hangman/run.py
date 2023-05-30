used = []
tries = 7
display = []
correct = []

guess = str(input("Middle Man: Enter the word or sentance: "))
print("word/sentance has been entered")
print('\033c')

for char in guess:
    if char == " ":
        display.append("-")
        correct.append(char)
    else:
        display.append("*")
        correct.append(char)
        
print("".join(display),"\nTries left:",tries)
def correctguess(ch):
    if ch in correct:
        for char in correct:
            if char == ch:
                indx = correct.index(char)
                display[indx] = ch
                correct[indx] = "+"
        print('\033c')
        print("".join(display),"\nTries left:",tries)
def wrongguess(ch):
    global tries
    if ch not in correct:
        tries-=1
        used.append(ch)
        fused = "".join(used)
        print('\033c')
        print("".join(display),f"\nTries left: {tries} \nUsed letters: {fused}")

def Player():
    char = str(input("Player: Enter a letter: "))
    if len(char) > 1:
        print("Please enter only one letter")
        Player()
    elif char in correct:
        correctguess(char)
    else:
        wrongguess(char)


while tries > 0:
    try:
        if "*" not in display:
            print('\033c')
            print("You won!")
            exit()
        Player()
    except KeyboardInterrupt:
        print('\033c')
        print("Game has been stopped")
        exit()

print('\033c')
print("You lost!")