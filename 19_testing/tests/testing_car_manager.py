from CarManager.car_manager import Car

import unittest

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Corolla", 5, 50)

    def test_initialization(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Corolla")
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 50)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_setter_with_empty_string(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""
        self.assertTrue("Make cannot be null or empty!" in str(context.exception))

    def test_model_setter_with_empty_string(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""
        self.assertTrue("Model cannot be null or empty!" in str(context.exception))

    def test_fuel_consumption_setter_with_negative_value(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1
        self.assertTrue("Fuel consumption cannot be zero or negative!" in str(context.exception))

    def test_fuel_capacity_setter_with_negative_value(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1
        self.assertTrue("Fuel capacity cannot be zero or negative!" in str(context.exception))

    def test_fuel_amount_setter_with_negative_value(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertTrue("Fuel amount cannot be negative!" in str(context.exception))

    def test_refuel_with_negative_value(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-1)
        self.assertTrue("Fuel amount cannot be zero or negative!" in str(context.exception))

    def test_refuel_with_zero_value(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertTrue("Fuel amount cannot be zero or negative!" in str(context.exception))

    def test_refuel_with_valid_value(self):
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_amount, 20)

    def test_refuel_with_value_exceeding_capacity(self):
        self.car.refuel(60)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_drive_with_sufficient_fuel(self):
        self.car.refuel(50)
        self.car.drive(500)  # Should consume 25 liters (5 liters per 100 km for 500 km)
        self.assertEqual(self.car.fuel_amount, 25)

    def test_drive_with_insufficient_fuel(self):
        self.car.refuel(10)
        with self.assertRaises(Exception) as context:
            self.car.drive(500)  # Should consume 25 liters, but we only have 10 liters
        self.assertTrue("You don't have enough fuel to drive!" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
