from array_dataStructure import StaticArray
import unittest

class TestArray(unittest.TestCase):

    def test_initialization(self):
        arr = StaticArray(5)
        # self.assertEqual(len(arr), 0)
        self.assertEqual(arr.size, 5)

    def test_get_set_item(self):
        arr = StaticArray(3)
        arr.__setitem__(0, 10)
        arr.__setitem__(1, 20)
        arr.__setitem__(2, 30)
        self.assertEqual(arr.__getitem__(0), 10)
        self.assertEqual(arr.__getitem__(1), 20)
        self.assertEqual(arr.__getitem__(2), 30)

    def test_out_of_bounds(self):
        arr = StaticArray(2)
        with self.assertRaises(IndexError):
            arr.__getitem__(2)
        with self.assertRaises(IndexError):
            arr.__setitem__(3, 100)

    def test_list_method(self):
        arr = StaticArray(3)
        arr.__setitem__(0, "a")
        arr.__setitem__(1, "b")
        arr.__setitem__(2, "c")
        self.assertEqual(arr.list(), ["a", "b", "c"])

    def test_str_method(self):
        arr = StaticArray(2)
        arr.__setitem__(0, 1)
        arr.__setitem__(1, 2)
        self.assertIn("py_object", str(arr))

if __name__ == "__main__":
    unittest.main()
