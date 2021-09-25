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
    def __init__(self, name, age, favorite_colors, hw_scores):
        self.name = name
        self.age = age
        self.favorite_colors = favorite_colors
        self.hw_scores = hw_scores
        
    def calc_avg_grades(self):
        return np.mean(self.hw_scores)


andy_person = Person("andy", 39, ["aggie blue", "fighting white"], [95, 80, 99])
print(andy_person.calc_avg_grades())