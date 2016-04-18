# -*- coding: utf-8 -*-

class Cache(object):
    __cache = {}
    __slots__ = '__cache',


    @classmethod
    def get(cls, key):
        print 'get', key
        return cls.__cache[key]

    
    @classmethod
    def set(cls, key, value):
        print 'set', key, value
        cls.__cache[key] = value


    @classmethod
    def has(cls, key):
        print 'has', key
        return key in cls.__cache


CACHE = Cache()

def cache_decorator(func):
    def wrapper(x):
        if CACHE.has(x):
            print 'CACHE already has key %s' % x
            return CACHE.get(x)
        else:
            print 'CACHE hasn\'t key %s' % x
            value = func(x)
            CACHE.set(x, value)
            return value

    return wrapper

@cache_decorator
def get_long_response(user_id):
    return user_id * 1000

print get_long_response(12)
print
print get_long_response(15)
print
print get_long_response(12)
print
