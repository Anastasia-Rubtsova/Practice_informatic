class Stack:
    def __init__(self):
        self._storage = []
    
    def is_empty(self):
        return len(self._storage) == 0
    
    def push(self, item):
        self._storage.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError ("Стек пуст")
        return self._storage.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._storage[-1]
    
    def size(self):
        return len(self._storage) 
