import unittest
from tire import CarriganTire, OctoprimeTire

class TestTires(unittest.TestCase):

  def test_carrigan_tire(self):
    tire = CarriganTire([0.1, 0.2, 0.8, 0.3])
    self.assertFalse(tire.needs_service())

    tire = CarriganTire([0.1, 0.9, 0.8, 0.3]) 
    self.assertTrue(tire.needs_service())

  def test_octoprime_tire(self):
    tire = OctoprimeTire([0.1, 0.2, 0.3, 0.4])
    self.assertFalse(tire.needs_service())

    tire = OctoprimeTire([0.9, 0.9, 1.0, 0.5])
    self.assertTrue(tire.needs_service())