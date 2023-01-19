import unittest
from datetime import datetime

from Engines.SternmanEngine import SternmanEngine
from Engines.CapuletEngine import CapuletEngine
from Engines.WilloughbyEngine import WilloughbyEngine
from Batteries.SpindlerBattery import SpindlerBattery
from Batteries.NubbinBattery import NubbinBattery
from Tires.CarriganTire import CarriganTire
from Tires.OctoprimeTire import OctoprimeTire

class CarComponentTests(unittest.TestCase):
    """Unit tests for all car components"""
    def test_sternman_should_be_serviced(self):
        warning_light_state = True
        engine = SternmanEngine(warning_light_state)
        self.assertTrue(engine.needs_service())

    def test_sternman_should_not_be_serviced(self):
        warning_light_state = False
        engine = SternmanEngine(warning_light_state)
        self.assertFalse(engine.needs_service())

    def test_capulet_should_be_serivced(self):
        lsm, cm = 0, 30000
        engine = CapuletEngine(lsm, cm)
        self.assertTrue(engine.needs_service())

    def test_capulet_should_not_be_serivced(self):
        lsm, cm = 0, 29999
        engine = CapuletEngine(lsm, cm)
        self.assertFalse(engine.needs_service())

    def test_willoughby_should_be_serviced(self):
        lsm, cm = 0, 60000
        engine = WilloughbyEngine(lsm, cm)
        self.assertTrue(engine.needs_service())

    def test_willoughby_should_not_be_serviced(self):
        lsm, cm = 0, 59999
        engine = WilloughbyEngine(lsm, cm)
        self.assertFalse(engine.needs_service())

    def test_spindler_should_be_serviced(self):
        # should service after 3 years or more
        lsd = datetime(2020, 6, 15)
        cd = datetime(2023, 6, 15)
        battery = SpindlerBattery(lsd, cd)
        self.assertTrue(battery.needs_service())
    
    def test_spindler_should_not_be_serviced(self):
        #should not be serviced if less than 3 years
        lsd = datetime(2020, 6, 15)
        cd = datetime(2023, 6, 14)
        battery = SpindlerBattery(lsd, cd)
        self.assertFalse(battery.needs_service())

    def test_nubbin_should_be_serviced(self):
        #should be serviced after 4 years or more
        lsd = datetime(2020, 6, 15)
        cd = datetime(2024, 6, 15)
        battery = NubbinBattery(lsd, cd)
        self.assertTrue(battery.needs_service())

    def test_nubbin_should_not_be_serviced(self):
        #should not be serviced if less than 4 years
        lsd = datetime(2020, 6, 15)
        cd = datetime(2024, 6, 14)
        battery = NubbinBattery(lsd, cd)
        self.assertFalse(battery.needs_service())

    def test_carrigan_should_be_serviced(self):
        tires = [0, 0.9, 0, 0]
        tire = CarriganTire(tires)
        self.assertTrue(tire.needs_service())

    def test_carrigan_should_not_be_serviced(self):
        tires = [0, 0.89, 0, 0]
        tire = CarriganTire(tires)
        self.assertFalse(tire.needs_service())

    def test_octoprime_should_be_serviced(self):
        tires = [0.7, 0.8, 0.8, 0.7]
        tire = OctoprimeTire(tires)
        self.assertTrue(tire.needs_service())

    def test_octoprime_should_not_be_serviced(self):
        tires = [0.7, 0.7, 0.7, 0.7]
        tire = OctoprimeTire(tires)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()

