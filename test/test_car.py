import unittest
from datetime import datetime, timedelta

from engine.engine import DefaultEngine
from engine.capulet_engine import CapuletEngine 
from engine.battery import DefaultBattery

class TestDefaultEngine(unittest.TestCase):

    def test_needs_service_true(self):
        engine = DefaultEngine(0, 5001)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = DefaultEngine(0, 5000)
        self.assertFalse(engine.needs_service())
        
class TestCapuletEngine(unittest.TestCase):

    def test_needs_service_true(self):
        engine = CapuletEngine(0, 30001)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine(0, 30000)
        self.assertFalse(engine.needs_service())

class TestDefaultBattery(unittest.TestCase):

    def test_needs_service_true(self):
        today = datetime.today().date()
        last_service_date = today - timedelta(days=731)
        battery = DefaultBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        today = datetime.today().date()
        last_service_date = today - timedelta(days=729) 
        battery = DefaultBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())
        
if __name__ == '__main__':
    unittest.main()