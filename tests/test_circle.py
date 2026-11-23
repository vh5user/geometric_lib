import math
import unittest
import circle


class CircleTestCase(unittest.TestCase):
    #area(r): positive & boundary values
    def test_area_positive_int(self):
        self.assertAlmostEqual(circle.area(3), math.pi * 9)

    def test_area_unit_radius(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_positive_float(self):
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25)

    def test_area_small_float(self):
        self.assertAlmostEqual(circle.area(1e-5), math.pi * 1e-10)

    def test_area_large_int(self):
        self.assertAlmostEqual(circle.area(10**6), math.pi * (10**6) ** 2)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_zero_float(self):
        self.assertEqual(circle.area(0.0), 0.0)

    def test_area_scaling_property(self):
        self.assertAlmostEqual(circle.area(2 * 3), 4 * circle.area(3))

    def test_area_return_type_float(self):
        self.assertIsInstance(circle.area(3), float)

    #area(r): negative & special values 

    def test_area_negative_int(self):
        with self.assertRaises(ValueError):
            circle.area(-3)

    def test_area_negative_float(self):
        with self.assertRaises(ValueError):
            circle.area(-0.5)

    def test_area_string_input(self):
        with self.assertRaises(TypeError):
            circle.area("3")

    def test_area_none_input(self):
        with self.assertRaises(TypeError):
            circle.area(None)

    def test_area_bool_true(self):
        with self.assertRaises(TypeError):
            circle.area(True)

    def test_area_list_input(self):
        with self.assertRaises(TypeError):
            circle.area([3])

    def test_area_inf_input(self):
        with self.assertRaises(ValueError):
            circle.area(float("inf"))

    def test_area_nan_input(self):
        with self.assertRaises(ValueError):
            circle.area(float("nan"))

    #perimeter(r): positive & boundary values

    def test_perimeter_positive_int(self):
        self.assertAlmostEqual(circle.perimeter(3), 2 * math.pi * 3)

    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5)

    def test_perimeter_small_float(self):
        self.assertAlmostEqual(circle.perimeter(1e-5), 2 * math.pi * 1e-5)

    def test_perimeter_large_int(self):
        self.assertAlmostEqual(circle.perimeter(10**6), 2 * math.pi * 10**6)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_scaling_property(self):
        self.assertAlmostEqual(circle.perimeter(2 * 3), 2 * circle.perimeter(3))

    def test_perimeter_return_type_float(self):
        self.assertIsInstance(circle.perimeter(3), float)

    # perimeter(r): negative, special values & arity 

    def test_perimeter_negative_int(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-3)

    def test_perimeter_negative_float(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-0.5)

    def test_perimeter_string_input(self):
        with self.assertRaises(TypeError):
            circle.perimeter("3")

    def test_perimeter_none_input(self):
        with self.assertRaises(TypeError):
            circle.perimeter(None)

    def test_perimeter_bool_false(self):
        with self.assertRaises(TypeError):
            circle.perimeter(False)

    def test_perimeter_inf_input(self):
        with self.assertRaises(ValueError):
            circle.perimeter(float("inf"))

    def test_perimeter_nan_input(self):
        with self.assertRaises(ValueError):
            circle.perimeter(float("nan"))

    def test_perimeter_no_arguments(self):
        with self.assertRaises(TypeError):
            circle.perimeter()


if __name__ == "__main__":
    unittest.main()
