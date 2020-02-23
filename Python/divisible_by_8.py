a = int(input("Enter Starting Range= "))
b = int(input("Enter Ending Range= "))
lis = []
for i in range(a,b+1):
    if i % 8 == 0:
        lis.append(i)
print(lis)

l = [i for i in range(a,b+1) if i%8==0]
print(l)