import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_need_service_true(self):
        tire_wear = [0.9, 0.9, 0.9, 0.4]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.need_service())

    def test_need_service_false(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.need_service())