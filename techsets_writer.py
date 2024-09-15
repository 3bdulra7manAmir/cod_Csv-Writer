import os
import csv
import subprocess as sp


targetedPath = input("Go ahead Alpha!: ")
fileName = "output"

programName = "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"

com = os.listdir(targetedPath)
counter = 0

for x in os.listdir(targetedPath):
    if x.endswith(".techset"):
        f = open(""f"{fileName}.csv", "a")
        f.write("techset," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])

for x in os.listdir(targetedPath):
    if x.endswith(".technique"):
        f = open(""f"{fileName}.csv", "a")
        f.write("technique," + x.split('.')[0] + "\n")
        f.close()
        print(x.split('.')[0])
        counter = counter + 1
        if counter == len(com):
            sp.Popen([programName, f"{fileName}.csv"])