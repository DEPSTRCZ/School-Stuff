height = int(input("Zadejte výšku(cm)\n")) / 100
height = height*height
weight = int(input("Zadejte hmotnost(Kg)\n"))
bmi = weight/height
if bmi < 16:
    level = "Těžká hubenost"
if bmi > 16 and bmi < 17:
    level = "Střední hubenost"
if bmi > 17 and bmi < 18.5:
    level = "Mírná hubenost"
if bmi > 18.5 and bmi < 25:
    level = "Normální"
if bmi > 25 and bmi < 30:
    level = "Nadváha"
if bmi > 30 and bmi < 35:
    level = "Obezita třídy 1"
if bmi > 35 and bmi < 40:
    level = "Obezita třídy 2"
if bmi > 40:
    level = "Obezita třídy 3"
        
print(f"Vaše bmi je:",bmi)
print(f"Váš index bmi je:", level)