num1 = int(input("Enter First Number= "))
num2 = int(input("Enter Second Number= "))
num3 = int(input("Enter Third Number= "))
small = min([num1,num2,num3])
count = 0
common = []
for i in range(1,small+1):
    if num1%i==0 and num2%i==0 and num3%i==0:
        common.append(i)
        count += 1
print("Total no. of common multiple= ", count)
print("Common Multiple:")
for i in common:
    print(i,end=" ")
