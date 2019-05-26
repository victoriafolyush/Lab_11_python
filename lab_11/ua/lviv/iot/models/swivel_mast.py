from lab_11.ua.lviv.iot.models.ski_resort_machinery import SkiResortMachinery


class SwivelMast(SkiResortMachinery):

    def __init__(self,
                 name,
                 producer,
                 fuel_per_hour,
                 mileage,
                 type_of_fuel,
                 wheel_formula,
                 length_of_flow,
                 height_of_flow,
                 oscillator):
        SkiResortMachinery.__init__(self, name, producer, fuel_per_hour, mileage, type_of_fuel, wheel_formula)
        self.length_of_flow = length_of_flow
        self.height_of_flow = height_of_flow
        self.oscillator = oscillator
        
    def __del__(self):
        print("Dracarys!" + self.name)
        
