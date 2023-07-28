from datetime import timedelta, date
from abc import ABC, abstractmethod

class Battery(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class DefaultBattery(Battery):

    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date) >= timedelta(days=730)