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
        return self.price * 1.05 ** (current_year - self.year)

andy_car = Car("toyota", "sequoia", 2002, 35000)
print(andy_car.calc_value(2021))

heber_car = Car("nissan", "murano", 2006, 25000)
print(heber_car.calc_value(2021))

emily_car = Car("toyota", "camry", 2004, 30000)
print(emily_car.calc_value(2021))

kegan_car = AntiqueCar("chevrolet", "corvette", 1969, 12000)
print(kegan_car.calc_value(2021))

emily_car2 = AntiqueCar("ford", "model-T", 1910, 300)
print(emily_car2.calc_value(2021))

cars_lot = [andy_car, heber_car, emily_car, kegan_car, emily_car2]

total_value = 0
for car in cars_lot:
    total_value += car.calc_value(2021)
    
print("The value of the entire car lot is: ", total_value)


