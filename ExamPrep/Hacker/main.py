import pandas as pd

## MAX DOWNLOAD SPEED = 20 MB/s
time_to_download = 300

with open("ExamPrep/Hacker/data.txt", "r") as f:
    line_data = f.read().splitlines()
    for line in line_data:
        try:
            target = line.split("|")
            name = target[0].strip()
            size = int(target[1].strip()[6:-2])
            credit_value = int(target[2].strip()[5:-8])

            ratio = credit_value / size
            print(ratio)
        except Exception as e:
            print(e)