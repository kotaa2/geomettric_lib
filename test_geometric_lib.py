import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_positive(self):
        self.assertAlmostEqual(circle.area(2), 4 * math.pi, places=6)

    def test_area_float(self):
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25, places=6)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle.perimeter(5), 10 * math.pi, places=6)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            circle.area(None)
        with self.assertRaises(TypeError):
            circle.perimeter(None)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_positive(self):
        self.assertEqual(square.area(5), 25)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(2.5), 6.25, places=6)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            square.area(None)
        with self.assertRaises(TypeError):
            square.perimeter(None)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_square_mul(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_normal(self):
        self.assertEqual(rectangle.area(3, 7), 21)

    def test_area_float(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0, places=6)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(rectangle.perimeter(3, 7), 20)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle.area(None, 5)
        with self.assertRaises(TypeError):
            rectangle.perimeter(None, 5)


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(triangle.area(10, 0), 0)

    def test_area_normal(self):
        self.assertEqual(triangle.area(6, 4), 12)

    def test_area_float(self):
        self.assertAlmostEqual(triangle.area(3.5, 2.0), 3.5, places=6)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            triangle.area(None, 4)
        with self.assertRaises(TypeError):
            triangle.perimeter(None, 4, 5)


if __name__ == "__main__":
    unittest.main()
