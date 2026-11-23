import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):

    # area(a, b): positive & boundary values

    def test_area_positive_int(self):
        self.assertEqual(rectangle.area(4, 5), 20)

    def test_area_square_case(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_zero_side(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_both_zero(self):
        self.assertEqual(rectangle.area(0, 0), 0)

    def test_area_positive_float(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0)

    def test_area_small_float(self):
        self.assertAlmostEqual(rectangle.area(1e-4, 2e-4), 2e-8)

    def test_area_large_int(self):
        self.assertEqual(rectangle.area(10**6, 10**6), 10**12)

    def test_area_commutativity(self):
        self.assertEqual(rectangle.area(3, 7), rectangle.area(7, 3))

    def test_area_scaling_property(self):
        self.assertEqual(rectangle.area(2 * 3, 2 * 5), 4 * rectangle.area(3, 5))

    # area(a, b): negative & special values

    def test_area_negative_first(self):
        with self.assertRaises(ValueError):
            rectangle.area(-4, 5)

    def test_area_negative_second(self):
        with self.assertRaises(ValueError):
            rectangle.area(4, -5)

    def test_area_both_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-4, -5)

    def test_area_string_and_int(self):
        with self.assertRaises(TypeError):
            rectangle.area("a", 3)

    def test_area_both_strings(self):
        with self.assertRaises(TypeError):
            rectangle.area("4", "5")

    def test_area_none_input(self):
        with self.assertRaises(TypeError):
            rectangle.area(None, 5)

    def test_area_bool_input(self):
        with self.assertRaises(TypeError):
            rectangle.area(True, 5)

    def test_area_inf_input(self):
        with self.assertRaises(ValueError):
            rectangle.area(float("inf"), 5)

    # perimeter(a, b): positive & boundary values

    def test_perimeter_positive_int(self):
        self.assertEqual(rectangle.perimeter(4, 5), 18)

    def test_perimeter_square_case(self):
        self.assertEqual(rectangle.perimeter(10, 10), 40)

    def test_perimeter_zero_side(self):
        self.assertEqual(rectangle.perimeter(10, 0), 20)

    def test_perimeter_both_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(rectangle.perimeter(2.5, 3.5), 12.0)

    def test_perimeter_small_float(self):
        self.assertAlmostEqual(rectangle.perimeter(0.001, 0.002), 0.006)

    def test_perimeter_large_int(self):
        self.assertEqual(rectangle.perimeter(10**9, 2 * 10**9), 6 * 10**9)

    def test_perimeter_commutativity(self):
        self.assertEqual(rectangle.perimeter(3, 7), rectangle.perimeter(7, 3))

    # perimeter(a, b): negative, special values & arity

    def test_perimeter_negative_first(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-4, 5)

    def test_perimeter_negative_second(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(4, -5)

    def test_perimeter_both_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-4, -5)

    def test_perimeter_both_strings(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("4", "5")

    def test_perimeter_none_input(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(None, 5)

    def test_perimeter_bool_input(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(True, False)

    def test_perimeter_nan_input(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(float("nan"), 5)

    def test_perimeter_missing_argument(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(4)


if __name__ == "__main__":
    unittest.main()
