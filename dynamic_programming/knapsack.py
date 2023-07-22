import random
import collections
from memoize import memoize

random.seed(42)

class Item(collections.namedtuple('Item', ['name', 'value', 'cost'])):
    def __repr__(self):
        return self.name

    @property
    def result(self):
        return Result(self.value, [self.name])

def generate_key(items, weight):
    return "{}-{}".format(len(items), weight)

class Result(object):
    def __init__(self, value, items):
        self._value = value
        self._items = items

    def add(self, other):
        return Result(self._value + other._value, self._items + other._items)

    def __repr__(self):
        return "{}, {}".format(self._value, self._items.__repr__())

    def __gt__(self, other): #used by max
        return self._value > other._value

    @classmethod
    def empty(cls):
        return cls(0, [])

@memoize(generate_key)
def knapsack(items, limit):
    return Result.empty() if len(items) == 0 or limit == 0 else max([pick_first(items, limit), skip_first(items, limit)])

def pick_first(items, limit):
    return Result.empty() if limit < items[0].cost else items[0].result.add(knapsack(items[1:], limit - items[0].cost))

def skip_first(items, limit):
    return knapsack(items[1:], limit)

def random_items(items_count, max_value, max_cost):
    return [Item(str(i), random.randint(1, max_value), random.randint(1, max_cost)) for i in range(items_count)]

import time
s = time.time()
items = random_items(100, 100, 100)
print(knapsack(items, 750))
print (time.time() - s)