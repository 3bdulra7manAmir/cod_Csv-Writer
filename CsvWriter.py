import os
import subprocess as sp


class FileHandler:
    def __init__(self, targeted_path, file_name, program_name):
        self.targetedPath = targeted_path
        self.fileName = file_name
        self.programName = program_name
        self.counter = 0
        self.com = os.listdir(targeted_path)

    def handle_file(self, x):
        match x.split('.')[-1]:  # Use file extension to match
            case "xse":
                self.write_to_file("xmodelsurfs", x)  # Xmodel_export Models
            case "xmodel_export":
                self.write_to_file("xmodel", x)  # Xmodel_export Models
            case "xsb":
                self.write_to_file("xmodelsurfs", x)  # XSB           modelsurfs
            case "xmb":
                self.write_to_file("xmodel", x)  # XMB           Models
            case "xab":
                self.write_to_file("xanim", x)  # XAB           Anims
            # case "json":
            #     self.write_to_file("sound", x)       # Json          Materials
            case "json":
                self.write_to_file("weapon", x)  # Json          Materials
            case "iwi":
                self.write_to_file("image", x)  # IWI           Images
            case "h1Image":
                self.write_to_file("image", x)  # H1Image       Images
            case "flac":
                self.write_to_file("loaded_sound", x)  # FLAC          Sounds
            case "flac":  # ERROR
                self.write_to_file("xanim_export", x)  # Xanim_Export   Anims
            case _:  # Default case
                pass

    def write_to_file(self, prefix, x):
        with open(f"{self.fileName}.csv", "a") as f:
            f.write(f"{prefix},{x.split('.')[0]}\n")
        print(x.split('.')[0])
        self.counter += 1
        if self.counter == len(self.com):
            sp.Popen([self.programName, f"{self.fileName}.csv"])


def main():
    targeted_path = input("Go ahead Alpha!: ")
    print("Your Path is : " + targeted_path)
    file_name = "output"
    print("CSV file name is : " + file_name)
    program_name = "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"

    handler = FileHandler(targeted_path, file_name, program_name)

    for x in os.listdir(targeted_path):
        handler.handle_file(x)


if __name__ == "__main__":
    main()
