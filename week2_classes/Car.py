class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        
    def calc_value(self, current_year):
        return self.price * 0.9 ** (current_year - self.year)
        
        
class AntiqueCar(Car):
    def calc_value(self, current_year):
        return self.price * 1.04 ** (current_year - self.year)
    

andy_car = Car("toyota", "sequoia", 2001, 40000)
print(andy_car.calc_value(2022))

chelsea_car = Car("honda", "accord", 1993, 12000)
print(chelsea_car.calc_value(2022))

ryan_car = Car("Jeep", "Wrangler", 2011, 30000)
print(ryan_car.calc_value(2022))


kelly_car = AntiqueCar("Pierce", "Arrow", 1922, 1000)
print(kelly_car.calc_value(2022))

korrie_car = AntiqueCar("Ford", "Stepside", 1960, 3200)

kellys_cars = [andy_car, chelsea_car, ryan_car, kelly_car, korrie_car]

tot_value = sum([my_car.calc_value(2022) for my_car in kellys_cars])
print("total value of kelly's cars: ", tot_value)

for car in kellys_cars:
    print(type(car))
    
    


