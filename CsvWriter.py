#  reads directory files names and store it without extension then write the result into a file called temp.txt
import os
from datetime import datetime
import time
import subprocess as sp

targetedPath = input("Go ahead Alpha!: ")
print("Your Path is : " + targetedPath)
fileName = input("CSV file name: ")
print("CSV file name is : " + fileName)

programName = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"

com = os.listdir(targetedPath)
counter = 0

for x in os.listdir(targetedPath):
    if x.endswith(".xmodel_export"):
        f = open(""f"{fileName}.csv", "a")
        f.write("xmodel," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".xanim_export"):
        f = open(""f"{fileName}.csv", "a")
        f.write("xanim," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".json"):
        f = open(""f"{fileName}.csv", "a")
        f.write("weapon," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.startswith("hud_icon"):
        f = open(""f"{fileName}.csv", "a")
        f.write("material," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".techset"):  # .techset
        f = open(""f"{fileName}.csv", "a")
        f.write("techset," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".technique"):  # .technique
        f = open(""f"{fileName}.csv", "a")
        f.write("technique," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".vertexshader"):  # .vertexshader
        f = open(""f"{fileName}.csv", "a")
        f.write("vertexshader," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".pixelshader"):  # pixelshade
        f = open(""f"{fileName}.csv", "a")
        f.write("pixelshader," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])


current_dateTime = datetime.now()
print("Finished!...")
time.sleep(3)
