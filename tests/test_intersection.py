import unittest
from intersection import find_intersection_v1, find_intersection_v2


class TestIntersection(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(find_intersection_v1([], []), [])
        self.assertEqual(find_intersection_v2([], []), [])

    def test_no_intersection(self):
        self.assertEqual(find_intersection_v1([1, 2, 3], [5, 6, 7]), [])
        self.assertEqual(find_intersection_v2([1, 2, 3], [5, 6, 7]), [])

    def test_lists_with_unique_values(self):
        self.assertEqual(find_intersection_v1([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
        self.assertEqual(find_intersection_v2([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])

    def test_lists_with_duplicates(self):
        self.assertEqual(
            find_intersection_v1([1, 2, 3, 3, 4, 4], [3, 3, 4, 5, 6, 7]), [3, 3, 4]
        )
        self.assertEqual(
            find_intersection_v2([1, 2, 3, 3, 4, 4], [3, 3, 4, 5, 6, 7]), [3, 3, 4]
        )

    def test_lists_with_different_len(self):
        self.assertEqual(find_intersection_v1([1, 2, 3], [3, 4, 5, 6, 7, 8]), [3])
        self.assertEqual(find_intersection_v2([1, 2, 3], [3, 4, 5, 6, 7, 8]), [3])

    def test_lists_with_negative_vals(self):
        self.assertEqual(find_intersection_v1([-1, -2, -3], [-3, -4, -5]), [-3])
        self.assertEqual(find_intersection_v2([-1, -2, -3], [-3, -4, -5]), [-3])


if __name__ == "__main__":
    unittest.main()
