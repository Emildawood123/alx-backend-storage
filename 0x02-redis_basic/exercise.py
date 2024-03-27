#!/usr/bin/env python3
""" first use redis with python """
from functools import wraps
import redis
import uuid


def count_calls(method: callable) -> callable:
    @wraps(method)
    def nested(slef, *args, **kwargs):
        keygen = method.__qualname__
        self._redis.incr(keygen)
        return method(self, *args, **kwargs)
    return nested

class Cache:
    """cache class"""
    def __init__(self):
        """constrctor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: str | bytes | int | float) -> str:
        """store method"""
        keygen: str = str(uuid.uuid4())
        self._redis.set(keygen, data)
        return keygen

    def get(self, key: str, fn: callable | None = None):
        """get if we have fn"""
        value = self._redis.get(key)
        if fn is None:
            return value
        else:
            return fn(value)

    def get_str(self, key) -> str:
        """get_str method"""
        return self._redis.get(key, lambda x: x.decode('UTF-8'))

    def get_int(self, key):
        """get_int method"""
        return self._redis.get(key, int)
