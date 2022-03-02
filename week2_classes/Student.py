class Student:
    def __init__(self, anum, name):
        self.__anum = anum
        self.name = name
        
    def get_anum(self):
        return self.__anum
        
    def set_anum(self, anum):
        self.__anum = anum
        
    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name
        
        
andy = Student("a000001", "andy")
print(andy.get_name())

# print(andy.__anum)

andy.set_anum("a00000001")

print(andy.get_anum())



