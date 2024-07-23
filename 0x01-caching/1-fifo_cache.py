#!/usr/bin/env python3
''' caching system '''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFOCache that inherits from BaseCaching and is a caching system:

    You must use self.cache_data - dictionary from the parent
    You can overload def __init__(self)
    '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data the item  for key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is > BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded
        '''
        if not key or not item:
            return
        self.cache_data[key] = item
        if self.cache_data.__len__() > BaseCaching.MAX_ITEMS:
            n = next(iter(self.cache_data))  # get first item
            print(f'DISCARD: {n}')
            self.cache_data.pop(n)

        return self.cache_data

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist, return None.
        '''
        if not key or not self.cache_data.get(key):
            return None
        else:
            return self.cache_data.get(key)
