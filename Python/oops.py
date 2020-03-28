class Student:
    college = "ACDB Engg. College"
    branch = "CSE"
    
    def intro(self):
        print("it is a member function")
        
s = Student()
print(s.college)
print(s.branch)
s.intro()