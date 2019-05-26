class SkiResortMachinery:

    def __init__(self,
                 name,
                 producer,
                 fuel_per_hour,
                 mileage,
                 type_of_fuel,
                 wheel_formula):
        self.name = name
        self.producer = producer
        self.fuel_per_hour = fuel_per_hour
        self.mileage = mileage
        self.type_of_fuel = type_of_fuel
        self.wheel_formula = wheel_formula

    def __del__(self):
        print("This object was destroyed: " + self.name)

    def __str__(self):
        return "\n\nName: " + self.name + \
               ",\n Producer: " + self.producer + \
               ",\n Fuel per hour: " + str(self.fuel_per_hour) + \
               ",\n Mileage: " + str(self.mileage) + \
               ",\n Type: " + str(self.type_of_fuel) + \
               ",\n Wheel formula: " + str(self.wheel_formula)
