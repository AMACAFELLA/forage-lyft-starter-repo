from datetime import date
from engine.capulet_engine import CapuletEngine 
from engine.default_battery import DefaultBattery
from car import Car

class CarFactory:

    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = DefaultBattery(last_service_date, current_date)
        return Car(engine, battery)