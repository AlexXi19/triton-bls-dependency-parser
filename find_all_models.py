import os
import subprocess

if __name__ == "__main__":
    # Get the directory path
    directory = './models'

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Print the names of all files in the directory
    files.sort()
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            print(file)
            subprocess.run(['python3 model_parser.py models/'+ file], shell=True)

