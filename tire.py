from abc import ABC, abstractmethod

class Tire(ABC):
  
  @abstractmethod
  def needs_service(self):
    pass

class CarriganTire(Tire):

  def __init__(self, wear_array):
    self.wear_array = wear_array

  def needs_service(self):
    return any(value >= 0.9 for value in self.wear_array) 

class OctoprimeTire(Tire):

  def __init__(self, wear_array):
    self.wear_array = wear_array

  def needs_service(self):
    return sum(self.wear_array) >= 3