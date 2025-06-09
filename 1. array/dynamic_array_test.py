from array_dataStructure import DynamicArray
import unittest

class TestDynamicArray(unittest.TestCase):

    def test_initial_length_and_capacity(self):
        arr = DynamicArray()
        self.assertEqual(len(arr), 0)
        self.assertEqual(arr.capacity, 1)

    def test_append_and_resize(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        self.assertEqual(len(arr), 3)
        self.assertTrue(arr.capacity >= 3)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)

    def test_get_set_item(self):
        arr = DynamicArray()
        arr.append('a')
        arr.append('b')
        arr[0] = 'x'
        arr[1] = 'y'
        self.assertEqual(arr[0], 'x')
        self.assertEqual(arr[1], 'y')

    def test_out_of_bounds_access(self):
        arr = DynamicArray()
        arr.append(5)
        with self.assertRaises(IndexError):
            _ = arr[2]
        with self.assertRaises(IndexError):
            arr[3] = 10

    def test_list_conversion(self):
        arr = DynamicArray()
        values = [10, 20, 30]
        for v in values:
            arr.append(v)
        self.assertEqual(arr.list(), values)

    def test_str_method(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        self.assertEqual(str(arr), "[1, 2]")

if __name__ == '__main__':
    unittest.main()
