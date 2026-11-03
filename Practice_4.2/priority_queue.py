class PriorityQueue:
    def __init__(self):
        self._items = []
        self._counter = 0

    def __len__(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item, priority):
        self._items.append({
            'item': item,
            'priority': priority,
            'order': self._counter
        })
        self._counter += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        best_idx = 0
        best_priority = self._items[0]['priority']
        best_order = self._items[0]['order']
        
        for i in range(1, len(self._items)):
            p = self._items[i]['priority']
            o = self._items[i]['order']
            if p < best_priority or (p == best_priority and o < best_order):
                best_idx = i
                best_priority = p
                best_order = o
        
        best_item = self._items[best_idx]['item']
        self._items.pop(best_idx)
        return best_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        best_idx = 0
        best_priority = self._items[0]['priority']
        best_order = self._items[0]['order']
        
        for i in range(1, len(self._items)):
            p = self._items[i]['priority']
            o = self._items[i]['order']
            if p < best_priority or (p == best_priority and o < best_order):
                best_idx = i
                best_priority = p
                best_order = o
        
        return self._items[best_idx]['item']
