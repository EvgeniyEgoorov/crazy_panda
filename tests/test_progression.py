import unittest
from progression import get_progression_details


class TestProgression(unittest.TestCase):
    def test_step_two(self):
        self.assertEqual(get_progression_details([1, 3, 5, 7, 1]), (1, 7, 2, 1))

    def test_step_four(self):
        self.assertEqual(get_progression_details([1, 5, 9, 13, 17, 17]), (1, 17, 4, 17))

    def test_no_added_val(self):
        self.assertEqual(get_progression_details([1, 5, 9, 13, 17]), (1, 17, 4, None))


if __name__ == "__main__":
    unittest.main()
