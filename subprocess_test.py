# print("Subprocess test!")

import subprocess

while True:
    user_input = input("Enter 1 to switch to file2.py: ")
    if user_input == "1":
        # Stop the execution of file1.py and start running file2.py
        print("Switching to file2.py...")
        subprocess.run(['python', 'file2.py'])
        print("Switching back to file1.py...")
    else:
        break
