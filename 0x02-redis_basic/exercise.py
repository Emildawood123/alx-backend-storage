#!/usr/bin/env python3
""" first use redis with python """
import redis
import uuid


class Cache:
    """cache class"""
    def __init__(self):
        """constrctor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """store method"""
        keygen: str = str(uuid.uuid4())
        self._redis.set(keygen, data)
        return keygen
