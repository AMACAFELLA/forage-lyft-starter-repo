from abc import ABC, abstractmethod 

class Engine(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class DefaultEngine(Engine):

    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 5000