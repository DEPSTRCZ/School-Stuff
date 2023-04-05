import gzip
import os
import csv
import bz2

path = str(input("Enter desired path:\n"))
csv_header = ["Soubor","Typ","Velikost (B)","Gzip Vel (B)","Bz2 Vel (B)"]

def writerows(file,content):
    if not os.path.isfile(file):
        with open(file, "a",newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_header)
            csvfile.close()
    with open(file,"a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(content)
        csvfile.close()

def CheckIfFileExtenstion(extension):
    if extension == ".gz" or extension == ".bz2": 
        quit()

for file in os.listdir(path):
    with open(f"{path}\\{file}", "rb") as f:
        uncompressed_size = os.path.getsize(f"{path}\\{file}")
        extension = os.path.splitext(file)[1]
        CheckIfFileExtenstion(extension)

        with gzip.open(f"{path}\\{file}.gz", "wb") as fileCompressed:
            fileCompressed.writelines(f)
            fileCompressed.close()

            with gzip.open(f"{path}\\{file}.gz", 'rb') as FCRead:
                FCRead.close()
                f.close()

                with open(f"{path}\\{file}", "rb") as f:
                    CheckIfFileExtenstion(extension)

                    with bz2.open(f"{path}\\{file}.bz2", "wb") as fileCompressed:
                        fileCompressed.writelines(f)
                        fileCompressed.close()

                        with bz2.open(f"{path}\\{file}.bz2", 'rb') as FCRead:
                            data = [file, extension, uncompressed_size,os.stat(f"{path}\\{file}.gz").st_size,os.stat(f"{path}\\{file}.bz2").st_size]
                            writerows(f"{path}/../table.csv",data)
                            FCRead.close()
                            f.close()
                            print(f"{file} -Done\n")
print("\nTask Finished!")