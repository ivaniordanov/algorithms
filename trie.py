import collections

class _Node(object):
    def __init__(self):
        self._children = collections.defaultdict(_Node)
        self._value = None

    def get_or_create(self, child):
        return self._children[child]

    def get_value(self):
        return self._value

    def has_value(self):
        return self._value is not None

    def set_value(self, value):
        self._value = value

    def children(self):
        for name, value in self._children.items():
            yield name, value

class Trie(object):
    def __init__(self):
        self._root = _Node()

    def _find_node(self, key):
        node = self._root
        for char in key:
            node = node.get_or_create(char)
        return node

    def set(self, key, value):
        node = self._find_node(key)
        if node.has_value(): raise ValueError(key + " already exists")
        node.set_value(value)

    def remove(self, key):
        return self._find_node(key).set_value(None)

    def exists(self, key):
        return self._find_node(key).has_value()

    def get(self, key):
        node = self._find_node(key)
        if not node.has_value(): raise KeyError(key)
        return node.get_value()

    def clear(self):
        self._root = _Node()

    def values(self):
        for _, child in self._walk(self._root, '', []):
            yield child.get_value()

    def keys(self):
        for key, _ in self._walk(self._root, '', []):
            yield key

    def all(self):
        for key, child in self._walk(self._root, '', []):
            yield {'key': key, 'value': child.get_value()}

    def _walk(self, node, key='', results=[]):
        if node.has_value(): results.append((key, node))
        for name, child in node.children():
            self._walk(child, key + name, results)
        return results
