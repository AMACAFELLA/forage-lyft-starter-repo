# test_battery.py

import unittest 
from datetime import timedelta
from battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):

  def test_needs_service_after_3_years(self):
    last_service_date = date(2020, 1, 1) 
    current_date = date(2023, 1, 1)

    battery = SpindlerBattery(last_service_date, current_date)  
    self.assertTrue(battery.needs_service())

  # Additional tests would go here

# battery.py

from abc import ABC, abstractmethod

class Battery(ABC):

  @abstractmethod
  def needs_service(self):
    pass

class SpindlerBattery(Battery):

  def __init__(self, last_service_date, current_date):
    self.last_service_date = last_service_date
    self.current_date = current_date

  def needs_service(self):
    return (self.current_date - self.last_service_date) >= timedelta(days=1095)