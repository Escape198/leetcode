class DynamicArray:
    def __init__(self):
        self._array = []
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]

    def append(self, value):
        self._array.append(value)
        self._size += 1
        # При необходимости увеличиваем ёмкость массива
        if len(self._array) == self._size:
            self._resize(2 * self._size)

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty list")
        item = self._array.pop()
        self._size -= 1
        if self._size > 0 and self._size == len(self._array) // 4:
            self._resize(len(self._array) // 2)
        return item

    def _resize(self, new_capacity):
        new_array = [0] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def is_empty(self):
        return self._size == 0


arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
print(f"Длина массива: {len(arr)}")
print(f"Элемент с индексом 1: {arr[1]}")
print(f"Удаленный элемент: {arr.pop()}")
print(f"Длина массива после удаления: {len(arr)}")
