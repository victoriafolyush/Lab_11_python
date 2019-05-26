from lab_11.ua.lviv.iot.managers.ski_resort_machinery_manager import SkiResortMachineryManager
from lab_11.ua.lviv.iot.models.fuel import Fuel
from lab_11.ua.lviv.iot.models.ski_resort_machinery import SkiResortMachinery
from lab_11.ua.lviv.iot.models.snow_generator import SnowGenerator
from lab_11.ua.lviv.iot.models.snow_tower import SnowTower
from lab_11.ua.lviv.iot.models.swivel_mast import SwivelMast
from lab_11.ua.lviv.iot.models.wheel_formula import WheelFormula


def main():
    manager = SkiResortMachineryManager()
    father = SkiResortMachinery("Machinery", "SMI", 45.6, 34.5,
                                Fuel.GAZOLINE, WheelFormula.FOUR_TWO)
    generator = SnowGenerator("Snow Generator F43 ", "SMI", 12.5, 452.5, Fuel.GAZOLINE,
                              WheelFormula.FOUR_FOUR, 64.5, "Nucleation", 60.0) 
    tower = SnowTower("Carriage Lift Tower", "SMI", 5.6, 521.54,
                      Fuel.KEROSENE, WheelFormula.TWO_TWO, 45.6, True, 9)
    mast = SwivelMast("Swivel Mast Swing Arm ", "SMI", 3.5, 762.5, Fuel.DIESEL,
                      WheelFormula.FOUR_TWO, 46.4, 67.2,
                      359.0)
   
    machinery_list = [father, generator, tower, mast]
         
    print(*manager.sort_by_mileage(machinery_list, True))
    print(*manager.sort_by_fuel_loss_per_hour(machinery_list, False))
    print(*manager.find_by_fuel(machinery_list, Fuel.DIESEL))
    print(*manager.find_by_wheel_formula(machinery_list, WheelFormula.FOUR_FOUR))
    
    print("\nDestructors: ")
   
  
if __name__ == '__main__':  
    main()
