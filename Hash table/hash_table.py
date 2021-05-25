class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        return

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        return

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


h = HashTable()
print(h.get_hash('banana'))
h.add("banana", '5')

print(h.get('banana'))
h['banana'] = 6
h['orange'] = 46
print(h.arr)
print(h['banana'])
print(h['orange'])

del h['orange']
print(h['orange'])
