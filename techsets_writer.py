import os
import subprocess as sp


def write_to_csv(file_type, file_name, output_file):
    """Append the file name to the CSV file with the specified type."""
    try:
        with open(output_file, "a") as f:
            f.write(f"{file_type},{file_name.split('.')[0]}\n")
        print(file_name.split('.')[0])
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    targeted_path = input("Go ahead Alpha!: ").strip()
    file_name = "output"
    program_name = "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"

    if not os.path.exists(targeted_path):
        print("Error: The specified path does not exist.")
        return

    output_file = f"{file_name}.csv"
    counter = 0

    # List all files in the targeted directory
    try:
        com = os.listdir(targeted_path)

        # Process .techset files
        for x in com:
            if x.endswith(".techset"):
                write_to_csv("techset", x, output_file)
                counter += 1

        # Process .technique files
        for x in com:
            if x.endswith(".technique"):
                write_to_csv("technique", x, output_file)
                counter += 1

        # Open the CSV file with the specified program once processing is complete
        if counter > 0:
            sp.Popen([program_name, output_file])
        else:
            print("No .techset or .technique files found.")

    except Exception as e:
        print(f"Error processing files: {e}")


if __name__ == "__main__":
    main()
