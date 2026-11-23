import unittest
import square


class SquareTestCase(unittest.TestCase):

    #area(a): positive & boundary values

    def test_area_positive_int(self):
        self.assertEqual(square.area(4), 16)

    def test_area_unit_side(self):
        self.assertEqual(square.area(1), 1)

    def test_area_positive_float(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_area_small_float(self):
        self.assertAlmostEqual(square.area(0.01), 0.0001)

    def test_area_large_int(self):
        self.assertEqual(square.area(10**6), 10**12)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_zero_float(self):
        self.assertEqual(square.area(0.0), 0.0)

    def test_area_scaling_property(self):
        self.assertEqual(square.area(3 * 2), 9 * square.area(2))

    def test_area_fractional_precision(self):
        self.assertAlmostEqual(square.area(0.1), 0.01)

    #area(a): negative & special values 

    def test_area_negative_int(self):
        with self.assertRaises(ValueError):
            square.area(-4)

    def test_area_negative_float(self):
        with self.assertRaises(ValueError):
            square.area(-2.5)

    def test_area_string_input(self):
        with self.assertRaises(TypeError):
            square.area("4")

    def test_area_none_input(self):
        with self.assertRaises(TypeError):
            square.area(None)

    def test_area_bool_true(self):
        with self.assertRaises(TypeError):
            square.area(True)

    def test_area_list_input(self):
        with self.assertRaises(TypeError):
            square.area([4])

    def test_area_inf_input(self):
        with self.assertRaises(ValueError):
            square.area(float("inf"))

    def test_area_nan_input(self):
        with self.assertRaises(ValueError):
            square.area(float("nan"))

    #perimeter(a): positive & boundary values

    def test_perimeter_positive_int(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_perimeter_unit_side(self):
        self.assertEqual(square.perimeter(1), 4)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_small_float(self):
        self.assertAlmostEqual(square.perimeter(0.001), 0.004)

    def test_perimeter_large_int(self):
        self.assertEqual(square.perimeter(10**9), 4 * 10**9)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_scaling_property(self):
        self.assertEqual(square.perimeter(5 * 2), 5 * square.perimeter(2))

    def test_perimeter_area_equality_at_4(self):
        self.assertEqual(square.perimeter(4), square.area(4))

    # perimeter(a): negative, special values & arity 

    def test_perimeter_negative_int(self):
        with self.assertRaises(ValueError):
            square.perimeter(-4)

    def test_perimeter_negative_float(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1.5)

    def test_perimeter_string_input(self):
        with self.assertRaises(TypeError):
            square.perimeter("4")

    def test_perimeter_none_input(self):
        with self.assertRaises(TypeError):
            square.perimeter(None)

    def test_perimeter_bool_true(self):
        with self.assertRaises(TypeError):
            square.perimeter(True)

    def test_perimeter_list_input(self):
        with self.assertRaises(TypeError):
            square.perimeter([4])

    def test_perimeter_inf_input(self):
        with self.assertRaises(ValueError):
            square.perimeter(float("inf"))

    def test_perimeter_no_arguments(self):
        with self.assertRaises(TypeError):
            square.perimeter()


if __name__ == "__main__":
    unittest.main()
