with open("myfile.txt","a") as file:
    print(file.tell())
    file.write("\nWrite operation using file handling")
    print("file written successfuly!")