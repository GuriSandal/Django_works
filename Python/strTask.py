a = input("Enter a number: ")
if a.isdigit():
    if len(a) >= 10:
        print((len(a)-3)*"*"+a[-3:])
    else:
        print("Number should contain at least 10 digit!!")
else:
    print("Number should contain digit only!!")
