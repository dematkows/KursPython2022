import unittest
from fields import square_area, rectangle_area, triangle_area, trapezoid_area


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 5
        self.b = 6
        self.h = 10

    def test_square_area_with_correct_values(self):
        # result = square_area(5)
        # self.assertEqual(result, 25)
        self.assertEqual(square_area(self.a), 25)

    def test_square_area_with_incorrect_values(self):
        # with self.assertRaises(TypeError):
        #     square_area("5")
        self.assertRaises(TypeError, square_area, "5")

    def test_rectangle_area_with_correct_values(self):
        result = rectangle_area(self.a, self.b)
        self.assertEqual(result, 30)

    def test_rectangle_area_with_incorrect_values(self):
        self.assertRaises(TypeError, rectangle_area, self.a, "self.b")

    def test_triangle_area_with_correct_values(self):
        result = triangle_area(self.a, "self.b")
        self.assertEqual(result, 15)

    def test_triangle_area_with_incorrect_values(self):
        self.assertRaises(TypeError, triangle_area, self.a, "self.b")

    def test_trapezoid_area_with_correct_values(self):
        result = trapezoid_area(self.a, self.b, self.h)
        self.assertEqual(result, 55)

    def test_trapezoid_area_with_incorrect_values(self):
        self.assertRaises(TypeError, trapezoid_area, self.a, self.b, "self.h")

    def tearDown(self):
        del self.a
        del self.b
        del self.h


if __name__ == '__main__':
    unittest.main()
