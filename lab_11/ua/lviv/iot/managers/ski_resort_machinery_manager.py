

class SkiResortMachineryManager:
    
    def __init__(self, machinery_list=[]):
        self.machinery_list = machinery_list
    
    def sort_by_fuel_loss_per_hour(self, machinery_list, is_reversed):
        return sorted(machinery_list, key=lambda machinery:machinery.fuel_per_hour, reverse=is_reversed)
    
    def sort_by_mileage(self, machinery_list, is_reversed):
        return sorted(machinery_list, key=lambda machinery:machinery.mileage, reverse=is_reversed)
    
    def find_by_fuel (self, machinery_list, type_of_fuel):
        return list(filter(lambda machinery:machinery.type_of_fuel == type_of_fuel, machinery_list))
    
    def find_by_wheel_formula(self, machinery_list, wheel_formula):
        return list(filter(lambda machinery:machinery.wheel_formula == wheel_formula, machinery_list))
