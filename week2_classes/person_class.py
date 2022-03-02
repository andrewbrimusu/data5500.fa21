import numpy as np

person = {}
person["name"] = "andy"
person["age"] = 39
person["favorite_colors"] = ["aggie blue", "fighting white"]

person["hw_scores"] = [95, 80, 99]



print("person: ", person)
print(person["name"], person["age"], person["favorite_colors"])


def calc_avg_grades(grades):
    return np.mean(grades)
    
    
    
print(calc_avg_grades(person["hw_scores"]))




class Person():
    def __init__(self, name, age, favorite_colors, hw_scores=[100, 100, 100]):
        self.name = name
        self.age = age
        self.favorite_colors = favorite_colors
        self.hw_scores = hw_scores
        
    def calc_avg_grades(self):
        return np.mean(self.hw_scores)
    
    def set_name(self, name):
        self.name = name
        
        


andy_person = Person("andy", 40, ["aggie blue", "fighting white"], [95, 80, 99])

ryan = Person("ryan", 21, ["blue"], [100, 99, 100])

kelley = Person("kelley", 30, ["kelly green"])


print(andy_person.calc_avg_grades())

print(ryan.calc_avg_grades())

print(ryan.name)

ryan.set_name("ryan sofoul")

print(ryan.name)

