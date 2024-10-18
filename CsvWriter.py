import os
import subprocess as sp


class FileHandler:
    def __init__(self, targeted_path, file_name, program_name):
        self.targeted_path = targeted_path
        self.file_name = file_name
        self.program_name = program_name
        self.counter = 0
        self.com = os.listdir(targeted_path)

    def handle_file(self, file_name):
        file_extension = file_name.split('.')[-1]
        prefix_mapping = {
            "xse": "xmodelsurfs",
            "xmodel_export": "xmodel",
            "xsb": "xmodelsurfs",
            "xmb": "xmodel",
            "xab": "xanim",
            "json": "weapon",
            "iwi": "image",
            "h1Image": "image",
            "flac": "loaded_sound",
            # Add more mappings as needed
        }

        prefix = prefix_mapping.get(file_extension)
        if prefix:
            self.write_to_file(prefix, file_name)

    def write_to_file(self, prefix, file_name):
        try:
            with open(f"{self.file_name}.csv", "a") as f:
                f.write(f"{prefix},{file_name.split('.')[0]}\n")
            print(file_name.split('.')[0])
            self.counter += 1

            if self.counter == len(self.com):
                sp.Popen([self.program_name, f"{self.file_name}.csv"])
        except Exception as e:
            print(f"Error writing to file: {e}")


def main():
    targeted_path = input("Go ahead Alpha!: ").strip()
    if not os.path.exists(targeted_path):
        print("Error: The specified path does not exist.")
        return

    print("Your Path is : " + targeted_path)
    file_name = "output"
    print("CSV file name is : " + file_name)
    program_name = "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"

    handler = FileHandler(targeted_path, file_name, program_name)

    try:
        for file_name in os.listdir(targeted_path):
            handler.handle_file(file_name)
    except Exception as e:
        print(f"Error processing files: {e}")


if __name__ == "__main__":
    main()
