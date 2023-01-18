import unittest
from datetime import datetime

from Engines.SternmanEngine import SternmanEngine
from Engines.CapuletEngine import CapuletEngine
from Engines.WilloughbyEngine import WilloughbyEngine
from Batteries.SpindlerBattery import SpindlerBattery
from Batteries.NubbinBattery import NubbinBattery

class CarComponentTests(unittest.TestCase):
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
        today = datetime.today()
        lsd, cd = today.replace(year=today.year-2), today
        battery = SpindlerBattery(lsd, cd)
        self.assertTrue(battery.needs_service())
    
    def test_spindler_should_not_be_serviced(self):
        today = datetime.today()
        lsd = today.replace(year=today.year-3)
        cd = datetime.today()
        battery = SpindlerBattery(lsd, cd)
        self.assertFalse(battery.needs_service())

    def test_nubbin_should_be_serviced(self):
        today = datetime.today()
        lsd, cd = today.replace(year=today.year-4), today
        battery = NubbinBattery(lsd, cd)
        self.assertTrue(battery.needs_service())

    def test_nubbin_should_not_be_serviced(self):
        today = datetime.today()
        lsd, cd = today.replace(year=today.year-5), today
        battery = NubbinBattery(lsd, cd)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()

