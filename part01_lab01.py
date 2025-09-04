class SimpleHashMap:

    def __init__(self, normalizer=lambda x: x, capacity=32):
        self._norm = normalizer
        self._cap = max(4, int(capacity))
        self._buckets = [[] for _ in range(self._cap)]
        self._size = 0

    def _index(self, key):
        return hash(self._norm(key)) % self._cap
    
    def put(self, key, value):
        nk = self._norm(key)
        idx = hash(nk) % self._cap
        chain = self._buckets[idx]
        for i, (xnk, _) in enumerate(chain):
            if xnk == nk:
                chain[i] = (nk, value)
                return
        chain.append((nk, value))
        self._size += 1

    def get(self, key, default=None):
        nk = self._norm(key)
        chain = self._buckets[hash(nk) % self._cap]
        for xnk, xv in chain:
            if xnk == nk:
                return xv
        return default
    
    def pop(self, key):
        nk = self._norm(key)
        idx = hash(nk) % self._cap
        chain = self._buckets[idx]

        for i, (xnk, xv) in enumerate(chain):
            if xnk == nk:
                del chain[i]
                self._size -= 1
                return xv
        raise KeyError(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        sentinel = object()
        v = self.get(key, sentinel)
        if v is sentinel:
            raise KeyError(key)
        return v
    
    def __contains__(self, key):
        nk = self._norm(key)
        chain = self._buckets[hash(nk) % self._cap]
        return any(xnk == nk for xnk, _ in chain)
    
    def __len__(self):
        return self._size
    


m = SimpleHashMap(normalizer=str.casefold)
m["SeOuL"] = 1
print(m["seoul"])
m["sEOUl"] = 3
print(m["seoul"])
print("SEOUL" in m)

def unordered_pair(p):
    a, b = p
    return (a, b) if a <= b else (b, a)

# 예제 2. 무방향 간선 키(순서 무시)
edges = SimpleHashMap(normalizer=unordered_pair)
edges[("A", "B")] = 5
print(edges[("B", "A")])
print(("B", "A") in edges)
