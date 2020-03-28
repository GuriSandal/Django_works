total = 120
marks = [110, 90, 22, 51, 10, 35, 20, 80]

def check(x):
    if x>33:
        return True
ls = list(filter(check, marks))

pas = list(filter(lambda y:y>=33, marks))
print(ls)
print(pas)

st = "Hel4lo 95this4 is!!"

# def c(x):
#     if x.isdigit() == False:
#         return x

print(list(filter(lambda x: not x.isdigit(), st )))

