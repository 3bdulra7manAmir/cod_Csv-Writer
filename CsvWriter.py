#  reads directory files names and store it without extension then write the result into a file called temp.txt
import os
from datetime import datetime
import time

targetedPath = input("Go ahead Alpha!: ")
print("Your Path is : " + targetedPath)
fileName = input("CSV file name: ")
print("CSV file name is : " + fileName)


for x in os.listdir(targetedPath):
    if x.endswith(".xmodel_export"):
        f = open(""f"{fileName}.csv", "a")
        f.write("xmodel," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
    elif x.endswith(".xanim_export"):
        f = open(""f"{fileName}.csv", "a")
        f.write("xanim," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
    elif x.endswith(".json"):
        f = open(""f"{fileName}.csv", "a")
        f.write("material," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
    elif x.startswith("hud"):
        f = open(""f"{fileName}.csv", "a")
        f.write("material," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])

current_dateTime = datetime.now()
print("Finished!...")
time.sleep(3)
