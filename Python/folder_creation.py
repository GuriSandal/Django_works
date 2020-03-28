import os

if "abcd" not in os.listdir():
    os.mkdir("abcd")
    print("Directory created")
else:
    os.rmdir("abcd")
    print("Directory Deleted")