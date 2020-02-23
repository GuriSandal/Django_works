start = int(input("Enter Starting Number= "))
end = int(input("Enter Ending Number= "))
print("Even Digit Sum= ",sum([i for i in range(start,end+1) if i%2==0 ]))
print("Odd Digit Sum= ",sum([i for i in range(start,end+1) if i%2!=0 ]))
