class PriorityQueue:
    def __init__(self):
        self._items = []
        self._keys = []
        self._counter = 0
    
    def is_empty(self):
        return len(self._items) == 0
    
    def push(self, item, priority):
        self._items.append(item)
        self._keys.append((priority, self._counter))
        self._counter += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        # Ищем индекс минимального ключа
        best_idx = 0
        for i in range(1, len(self._keys)):
            if self._keys[i] < self._keys[best_idx]:
                best_idx = i
        
        # Удаляем и ключ, и сам элемент
        self._keys.pop(best_idx)
        return self._items.pop(best_idx)

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        best_idx = 0
        for i in range(1, len(self._keys)):
            if self._keys[i] < self._keys[best_idx]:
                best_idx = i
        
        return self._items[best_idx]

    def size(self):
        return len(self._items)

    def __len__(self):
        return len(self._items)
