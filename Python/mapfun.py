total = 120
marks = [110, 90, 22, 51, 10, 35, 20, 80]

print(list(map(lambda x:round((x/total)*100,2),marks)))

st = "Hel4lo 95this4 is!!"

print(list(map(lambda x: "" if x.isdigit() else x, st )))

