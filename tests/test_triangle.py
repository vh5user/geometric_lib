import unittest
import triangle


class TriangleTestCase(unittest.TestCase):

    # area(a, h): positive & boundary values

    def test_area_positive_int(self):
        self.assertEqual(triangle.area(6, 4), 12.0)

    def test_area_odd_product(self):
        self.assertEqual(triangle.area(3, 5), 7.5)

    def test_area_unit_dimensions(self):
        self.assertEqual(triangle.area(1, 1), 0.5)

    def test_area_positive_float(self):
        self.assertAlmostEqual(triangle.area(2.5, 4.2), 5.25)

    def test_area_small_float(self):
        self.assertAlmostEqual(triangle.area(1e-4, 2e-4), 1e-8)

    def test_area_large_int(self):
        self.assertEqual(triangle.area(10**6, 10**6), 5 * 10**11)

    def test_area_zero_base(self):
        self.assertEqual(triangle.area(0, 5), 0.0)

    def test_area_zero_height(self):
        self.assertEqual(triangle.area(5, 0), 0.0)

    def test_area_scaling_property(self):
        self.assertEqual(triangle.area(2 * 6, 2 * 4), 4 * triangle.area(6, 4))

    # area(a, h): negative & special values

    def test_area_negative_base(self):
        with self.assertRaises(ValueError):
            triangle.area(-6, 4)

    def test_area_negative_height(self):
        with self.assertRaises(ValueError):
            triangle.area(6, -4)

    def test_area_both_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-6, -4)

    def test_area_string_input(self):
        with self.assertRaises(TypeError):
            triangle.area("6", 4)

    def test_area_none_input(self):
        with self.assertRaises(TypeError):
            triangle.area(None, 4)

    def test_area_bool_input(self):
        with self.assertRaises(TypeError):
            triangle.area(True, 4)

    def test_area_inf_input(self):
        with self.assertRaises(ValueError):
            triangle.area(float("inf"), 4)

    # perimeter(a, b, c): positive & boundary values

    def test_perimeter_right_triangle(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)

    def test_perimeter_isosceles(self):
        self.assertEqual(triangle.perimeter(5, 5, 8), 18)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(triangle.perimeter(2.5, 3.5, 4.0), 10.0)

    def test_perimeter_small_float(self):
        self.assertAlmostEqual(triangle.perimeter(0.003, 0.004, 0.005), 0.012)

    def test_perimeter_large_int(self):
        self.assertEqual(triangle.perimeter(3 * 10**8, 4 * 10**8, 5 * 10**8), 12 * 10**8)

    def test_perimeter_permutation_invariance(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), triangle.perimeter(5, 3, 4))

    def test_perimeter_all_zeros(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    # perimeter(a, b, c): negative, inequality, special values & arity

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_perimeter_all_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, -4, -5)

    def test_perimeter_inequality_violation(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 2, 10)

    def test_perimeter_degenerate_triangle(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 2, 3)

    def test_perimeter_all_strings(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("3", "4", "5")

    def test_perimeter_none_input(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(None, 4, 5)

    def test_perimeter_bool_input(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(True, True, True)

    def test_perimeter_nan_input(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(float("nan"), 4, 5)

    def test_perimeter_missing_argument(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, 4)


if __name__ == "__main__":
    unittest.main()
