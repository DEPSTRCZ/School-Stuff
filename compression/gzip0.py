import gzip
import os
import csv

path = "compression\\files"
csv_header = ["Soubor","Typ","Velikost","Gzip Vel","Bz2 Vel"]

for file in os.listdir(path):
    with open(f"{path}\\{file}", "rb") as f:
        print(f)
        with gzip.open(f"{path}\\{file}.gz", "wb") as f_out:
            f_out.writelines(f)
            with gzip.open(f"{path}\\{file}.gz", 'rb') as fc:
                file_content = fc.read()
                print(len(file_content))
                uncompressed_size = os.path.getsize(f"{path}\\{file}")
                extension = os.path.splitext(file)[1]
                print(file, extension, uncompressed_size)
                with open(f"{path}\\{file}", "rb") as test:
                    print(f)
                    compressed_data = f.read()

compressed_size = len(compressed_data)
print(f"Compressed file size: {compressed_size} bytes")