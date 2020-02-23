num = int(input("Enter A Number= "))
for i in range(2,(num//2)+1):
    if num%i == 0:
        print("The give is not Prime")
        break
else:
    print("The given number is Prime")        
