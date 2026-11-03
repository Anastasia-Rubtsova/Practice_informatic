class Deque:
    def __init__(self):
        self._capacity = 4
        self._data = [None] * self._capacity
        self._head = 0
        self._size = 0

    @property
    def capacity(self):
        return self._capacity

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _grow(self):
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._capacity]
        self._data = new_data
        self._head = 0
        self._capacity = new_capacity

    def push_back(self, item):
        if self._size == self._capacity:
            self._grow()
        index = (self._head + self._size) % self._capacity
        self._data[index] = item
        self._size += 1

    def push_front(self, item):
        if self._size == self._capacity:
            self._grow()
        self._head = (self._head - 1) % self._capacity
        self._data[self._head] = item
        self._size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        item = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        back_index = (self._head + self._size - 1) % self._capacity
        item = self._data[back_index]
        self._data[back_index] = None
        self._size -= 1
        return item

    def front(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        return self._data[self._head]

    def back(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        back_index = (self._head + self._size - 1) % self._capacity
        return self._data[back_index]
