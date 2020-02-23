num1 = int(input("Enter First Number= "))
num2 = int(input("Enter Second Number= "))
small = min([num1,num2])
large = max([num1,num2])

x = large
y = small
while(y):
    x,y = y,x%y
print("H.C.F. or G.C.D.=",x)


x=large
y=small
while(True):
    if((large % x == 0) and (large % y == 0)):
        print("L.C.M.= ",large)
        break
    large += 1
