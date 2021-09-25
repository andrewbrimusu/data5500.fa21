class House():
    def __init__(self, area_code, sq_ft, num_bedrms, num_bathrms, age_home):
        self.area_code = area_code
        self.sq_ft = sq_ft
        self.num_bathrms = num_bathrms
        self.num_bedrms = num_bedrms
        
    def get_area_code(self):
        return self.area_code
        
    def get_sq_ft(self):
        return self.sq_ft
        
    def get_num_bathrms(self):
        return self.num_bathrms
        
    def get_num_bedrms(self):
        return self.num_bedrms
    
    def get_age_home(self):
        return self.age_home
        
    def set_area_code(sel, area_code):
        self.area_code = area_code
        
    def set_sq_ft(self, sq_ft):
        self.sq_ft = sq_ft
        
    def set_num_bathrms(self, num_bathrms):
        self.num_bathrms = num_bathrms
        
    def set_num_bedrms(self, num_bedrms):
        self.num_bedrms = num_bedrms
        
    def set_age_home(self, age_home):
        self.age_home = age_home
        
    
andys_house = House(630, 1500, 4, 2, 80)
andys_house.set_age_home(90)
print(andys_house.get_age_home())

