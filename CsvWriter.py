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

for x in os.listdir(targetedPath): # Xmodel
    if x.endswith(".xmodel_export"):
        f = open(""f"{fileName}.csv", "a")
        f.write("xmodel," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".xmb"): # Xmodel
        f = open(""f"{fileName}.csv", "a")
        f.write("xmodel," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".xab"): # Xanim
        f = open(""f"{fileName}.csv", "a")
        f.write("xanim," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".json"): # sound
        f = open(""f"{fileName}.csv", "a")
        f.write("sound," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".xanim_export"): # Xanim
        f = open(""f"{fileName}.csv", "a")
        f.write("xanim," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".json"): # mostly WEAPONS files depends on The dir
        f = open(""f"{fileName}.csv", "a")
        f.write("weapon," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.startswith("hud_icon"): # WEAPONS_icons Materials
        f = open(""f"{fileName}.csv", "a")
        f.write("material," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".json"): #  mostly Materials depends on The dir
        f = open(""f"{fileName}.csv", "a")
        f.write("material," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".iwi"):  # iwi
        f = open(""f"{fileName}.csv", "a")
        f.write("image," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])
    
    # elif x.endswith(".dds"):  # dds
    #     f = open(""f"{fileName}.csv", "a")
    #     f.write("image,," + x.split('.')[0] + "\n")
    #     f.close()
    #     print(x.split('.')[0])
    #     counter = counter + 1
    #     if counter == len(com):
    #         sp.Popen([programName, f"{fileName}.csv"])

    elif x.endswith(".h1Image"):  # h1Image
        f = open(""f"{fileName}.csv", "a")
        f.write("image," + x.split('.')[0] + "\n")
        f.close()
        print("image," + x)
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])


current_dateTime = datetime.now()
print("Finished!...")
time.sleep(3)
