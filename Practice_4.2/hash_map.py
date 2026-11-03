class HashMap:
    def __init__(self, size=10):
        self._size = size
        self._buckets = [[] for _ in range(size)]
        self._count = 0

    def _get_bucket(self, key):
        return self._buckets[hash(key) % self._size]

    def put(self, key, value):
        bucket = self._get_bucket(key)
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])
        self._count += 1

    def get(self, key):
        bucket = self._get_bucket(key)
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        raise KeyError("Ключ не найден")

    def remove(self, key):
        bucket = self._get_bucket(key)
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                self._count -= 1
                return
        raise KeyError("Ключ не найден")

    def contains(self, key):
        bucket = self._get_bucket(key)
        for pair in bucket:
            if pair[0] == key:
                return True
        return False

    def __len__(self):
        return self._count
