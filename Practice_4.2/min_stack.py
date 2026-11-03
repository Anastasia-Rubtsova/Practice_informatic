class MinStack:
    def __init__(self):
        self._storage = []
        self._mins = []
    def is_empty(self):
        return len(self._storage) == 0
    
    def push(self, item):
        self._storage.append(item)
        if len(self._mins) == 0:
            self._mins.append(item)
        else:
            if item < self._mins[-1]:
                self._mins.append(item)
            else:
                self._mins.append(self._mins[-1])
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        self._mins.pop()
        return self._storage.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._storage[-1]
    
    def get_min(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._mins[-1]
    
    def __len__(self):
        return len(self._storage)
