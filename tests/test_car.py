import unittest
from car import Car


# ⚠️ Using only 1️⃣ class for all the tests like this is not scalable.
# For larger projects, we need test isolation with different `setUp` methods for each test.
class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car()

    def test_initial_speed(self) -> None:
        self.assertEqual(self.car.speed, 0)

    def test_initial_odometer(self) -> None:
        self.assertEqual(self.car.odometer, 0)

    def test_initial_time(self) -> None:
        self.assertEqual(self.car.time, 0)

    def test_accelerate_from_zero(self) -> None:
        self.assertEqual(self.car.accelerate(), 5)
        self.assertEqual(self.car.speed, 5)

    def test_multiple_accelerations(self) -> None:
        for _ in range(3):
            self.car.accelerate()
        self.assertEqual(self.car.speed, 15)

    def test_brake_once(self) -> None:
        self.car.accelerate()
        self.assertEqual(self.car.brake(), 0)
        self.assertEqual(self.car.speed, 0)

    def test_multiple_brakes(self) -> None:
        for _ in range(5):
            self.car.accelerate()
        for _ in range(3):
            self.car.brake()
        self.assertEqual(self.car.speed, 10)

    def test_should_not_allow_negative_speed(self) -> None:
        self.car.brake()
        self.assertEqual(self.car.speed, 0)
