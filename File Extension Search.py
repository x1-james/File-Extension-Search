# File extension search
#
# This program will search a directory for files with a specific extension
# and print the number of files found and the extension. It will also ask
# the user if they want to see the files and if they want to search again.

import os

def main():

    # Ask user what file extension they want to search for
    ext = input("What file extension are you looking for? ")

    # Ask user what directory they want to search
    dir = input("What directory do you want to search? ")

    found_files = []

    # Search file structure for files with that extension
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                found_files.append(os.path.join(root, file))

    # Print the number of files found and the extension
    print("Found", len(found_files), "files with the", ext, "extension.")

    # Ask if the user wants to see the files
    show = input("Do you want to see the files? (y/n) ")

    # If yes, print the files
    if show == "y":
        for file in found_files:
            print(file)

    # Ask user if they want to search again
    again = input("Do you want to search again? (y/n) ")

    # If yes, repeat
    if again == "y":
        main()

main()
