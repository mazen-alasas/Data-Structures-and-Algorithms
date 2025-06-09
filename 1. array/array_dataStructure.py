import ctypes


class StaticArray:
    def __init__(self, size):
        self.size = size
        self._array = self._make_array(size)

    def _make_array(self, size):
        return (size * ctypes.py_object)()

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        return self._array[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        self._array[index] = value

    def __str__(self):
        return str(self._array)

    def list(self):
        return [self._array[i] for i in range(self.size)]

    def __len__(self):
        return self.size



class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self._array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        return self._array[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        self._array[index] = value

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self._array[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self._array[i]
        self._array = new_array
        self.capacity = new_capacity

    def __len__(self):
        return self.size

    def list(self):
        return [self._array[i] for i in range(self.size)]

    def __str__(self):
        return str(self.list())
