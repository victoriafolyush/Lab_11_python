from ua.lviv.iot.models.ski_resort_machinery import SkiResortMachinery


class SnowTower(SkiResortMachinery): 
    
    def __init__ (self,
                 name,
                 producer,
                 fuel_per_hour,
                 mileage,
                 type_of_fuel,
                 wheel_formula,
                 height,
                 has_board_copressor,
                 water_jets):
        super().__init__(name, producer, fuel_per_hour, mileage, type_of_fuel, wheel_formula)
        self.height = height
        self.has_board_copressor = has_board_copressor
        self.water_jets = water_jets

    def __str__(self):
            return super().__str__() + \
            "\n Height: " + str(self.height) + \
            ",\n Has board compressor: " + str(self.has_board_copressor) + \
            ",\n Water jets: " + str(self.water_jets)
