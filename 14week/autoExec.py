import os
import time

while True:
    file_list = os.listdir()
    print("Current files in the folder:")
    for file in file_list:
        print(file)
    print("---------------------------")
    time.sleep(15)
