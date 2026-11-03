class PriorityQueue:
    def __init__(self):
        self._storage = []
        self._counter = 0
    def is_empty(self):
        return len(self._storage) == 0
    
    def push(self, item, priority):
        self._storage.append((priority, self._counter, item))
        self._counter += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")

        best_idx = 0
        for i in range(1, len(self._storage)):
            if (self._storage[i][0] > self._storage[best_idx][0] or
                (self._storage[i][0] == self._storage[best_idx][0] and 
                 self._storage[i][1] < self._storage[best_idx][1])):
                best_idx = i

        best_item = self._storage[best_idx][2]
        self._storage.pop(best_idx)
        return best_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        best_idx = 0
        for i in range(1, len(self._storage)):
            if (self._storage[i][0] > self._storage[best_idx][0] or
                (self._storage[i][0] == self._storage[best_idx][0] and 
                 self._storage[i][1] < self._storage[best_idx][1])):
                best_idx = i
        
        return self._storage[best_idx][2]

    def size(self):
        return len(self._storage)
