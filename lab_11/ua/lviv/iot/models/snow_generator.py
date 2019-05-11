from ua.lviv.iot.models.ski_resort_machinery import SkiResortMachinery


class SnowGenerator(SkiResortMachinery):

    def __init__(self,
                 name,
                 producer,
                 fuel_per_hour,
                 mileage,
                 type_of_fuel,
                 wheel_formula,
                 board_compressor_power,
                 nucleation,
                 rotation):
        super().__init__(name, producer, fuel_per_hour, mileage, type_of_fuel, wheel_formula)
        self.board_compressor_power = board_compressor_power 
        self.nucleation = nucleation 
        self.rotation = rotation 
        
    def __str__(self):
        return super().__str__() + \
        "\n Board compression power: " + str(self.board_compressor_power) + \
        ",\n Nucleation: " + self.nucleation + \
        ",\n Rotation: " + str(self.rotation)
