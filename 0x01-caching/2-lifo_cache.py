#!/usr/bin/env python3
''' caching system '''
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    '''
    caching system

    You must use self.cache_data - dictionary from the parent class BaseCaching
    You can overload def __init__(self):
    '''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data the item  for key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is > BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist, return None.
        '''
        return self.cache_data.get(key)
