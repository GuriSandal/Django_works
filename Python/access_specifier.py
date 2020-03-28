class Student:
    def __init__(self):
        self.name = "Gurjant" #Public
        self._rno = 100       #Protected 
        self.__acc = 89767    #Private
        print("Student Initialize")

class Drive:
    def __init__(self):
        Student.__init__(self)
        print("Drive Initialize")
        print(self.name)
        print(self._rno)
       
o = Drive()