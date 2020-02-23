users = []
while True:
    print()
    print("Press 1: To Add User")
    print("Press 2: To View Users")
    print("Press 3: To Delete User")
    print("Press 4: To Exit")
    print()
    a = input("Enter Choice: ")
    if a == '1':
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        users.append([name,email])
        print(f"{name} added successfully!!!")
    elif a == '2':
        for i in users:
            print(f"Name: {i[0]},  Email: {i[1]}")
        print(f"**** Total Users: {len(users)} ****")
    elif a == '3':
        d = input("Enter Name to Delete: ")
        if len(users) == 0:
            print(f"{d} is not in our database")
        else:
            for i in range(len(users)):
                if d.lower() == users[i][0].lower():
                    users.pop(i)  
                    print(f"{d.capitalize()} remover successfully!!!")
                    break
                elif i == (len(users) - 1):
                    print(f"{d} is not in our database")
    elif a == '4':
        break
    