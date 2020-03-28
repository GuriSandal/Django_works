import random
options = """
    Press1: Register as User
    Press2: Resgister as Admin
    Press3: Add Movie (Admin)
    Press0: To Exit
"""
print(options)
user = []
admin = []

movies = []

def create_user_account():
    name=input("Please Enter Your name: ")
    if len(user) == 0:
        pin = random.randint(1000,9999)
        print("!!****Please Check your Pin Number****!!")
        a = {"Name":name,"PIN":pin}
        user.append(a)
        print("Dear {} Your acc. created! PIN No.{}".format(name,pin))
    else:
        pin = random.randint(1000,9999)
        for i in range(len(user)+1):
            if i == len(user):
                print("!!****Please Check your Pin Number****!!")
                a = {"Name":name,"PIN":pin}
                user.append(a)
                print("Dear {}, You reg. successfully! PIN No.{}".format(name,pin))
            elif user[i]["PIN"]==pin:
                pin = random.randint(1000,9999)
                

def create_admin_account():
    name=input("Please Enter Your name: ")
    if len(admin) == 0:
        pin = random.randint(1000,9999)
        print("!!****Please Check your Pin Number****!!")
        a = {"Name":name,"PIN":pin}
        admin.append(a)
        print("Dear {} Your acc. created! PIN No.{}".format(name,pin))
    else:
        pin = random.randint(1000,9999)
        for i in range(len(admin)+1):
            if i == len(admin):
                print("!!****Please Check your Pin Number****!!")
                a = {"Name":name,"PIN":pin}
                admin.append(a)
                print("Dear {}, You reg. successfully ! PIN No.{}".format(name,pin))
            elif admin[i]["PIN"]==pin:
                pin = random.randint(1000,9999)
 
 
def addMovie():
    pin = int(input("Enter Your PIN: "))
    for i in range(len(admin)):
        if admin[i]['PIN'] == pin:    
            print("!!Welcom  ",admin[i]['Name'])
            print()
            movie = input("Enter Movie Name: ")
            if len(movies) == 0:
                lang = input("Enter Language: ")
                t_seats = int(input("Enter Total no. of seats: "))            
                a_seats = int(input("Enter Total no of avialabe seats: ")) 
                m = {"Name":movie, "Language":lang, "Total Seats":t_seats, "Available Seats":a_seats}
                movies.append(m) 
                print("Movie added Successfully!!")
                print("Name     Languages     Total Seats      Avialabe Seats")
                for k in movies:
                    print(f"{k['Name']}     {k['Language']}     {k['Total Seats']}     {k['Available Seats']}")
            else:
                for j in range(len(movies)+1):
                    if j == len(movies):
                        lang = input("Enter Language: ")
                        t_seats = int(input("Enter Total no. of seats: "))            
                        a_seats = int(input("Enter Total no of avialabe seats: ")) 
                        m = {"Name":movie, "Language":lang, "Total Seats":t_seats, "Available Seats":a_seats}
                        movies.append(m) 
                        print("Movie added Successfully!!")
                        print("Name     Languages     Total Seats      Avialabe Seats")
                        for k in movies:
                            print(f"{k['Name']}       {k['Language']}       {k['Total Seats']}        {k['Available Seats']}")
                    elif movies[j]["Name"]==movie:
                        print("!!Movie is already There beacause at one time only one movie will be show of same name!!!")
                        break
        else:
            print("Your are not Admin")
                
            
                  
            
                
                
while True:
    op = input("\nChoose an action: ")
    if op=="1":
        create_user_account()
    elif op=="2":
        create_admin_account()
    elif op=="3":
        addMovie()
    elif op=="0":
        break
    else:
        print("Invalid Choice\n")