import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_need_service_true(self):
        tire_wear = [0.1,0.1,0.9,0.1]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.need_service())

    def test_need_service_false(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.need_service())