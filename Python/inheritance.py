class Account:
    clz = "ABCD"
    branch = "CSE"
    def fee_detail(self,total,pending):
        print(self.clz)
        print("Total:Rs.{}".format(total))
        print("Pending:Rs.{}".format(pending))
        
class Student(Account):
    tech = "python"
    def register(self, name, email):
        print("Name:",name)
        print("Email:",email)
        
ob = Student()
ob.fee_detail(100,10)
ob.register("Guri","guri@gmail.com")
print(ob.branch)