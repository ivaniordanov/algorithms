import operator

class Heap(object):
    def __init__(self, data, compare=operator.gt):
        self._compare = compare
        self._data = data
        self._create()

    def push(self, item):
        self._data.append(item)
        self._up_heap(len(self._data)-1)

    def pop(self):
        item = self._data[0]
        self._data[0] = self._data.pop()
        self._down_heap(0)
        return item

    def _create(self):
        for i in reversed(range(len(self._data) // 2)): self._down_heap(i)

    def _parent(self, index):
        return max(0, (index-1)//2)

    def _children(self, index):
        return [x for x in [index*2+1, index*2+2] if x < len(self._data)]

    def _pick_child(self, children, default):
        if len(children) == 2: return children[0] if self._compare(self._data[children[0]], self._data[children[1]]) else children[1]
        return children[0] if children else default

    def _swap(self, first, second):
        self._data[first], self._data[second] = self._data[second], self._data[first]
        return second

    def _up_heap(self, i):
        parent = self._parent(i)
        while self._compare(self._data[i], self._data[parent]):
            i = self._swap(i, parent)
            parent = self._parent(i)

    def _down_heap(self, index):
        child = self._pick_child(self._children(index), index)
        while self._compare(self._data[child], self._data[index]):
            index = self._swap(index, child)
            child = self._pick_child(self._children(index), index)
