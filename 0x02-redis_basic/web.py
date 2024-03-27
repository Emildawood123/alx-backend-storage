#!/usr/bin/env python
"""get_page method"""
import requests
import redis
from functools import wraps
from typing import Callable


def helper_method(fn: Callable) -> Callable:
    """helper_method"""
    @wraps(fn)
    def wrapper(url: str) -> str:
        """wrapper function"""
        r = redis.Redis()
        r.incr(f"count:{url}")
        cached_page = r.get(f"{url}")
        if cached_page:
            return cached_page.decode("utf-8")
        response = fn(url)
        r.set(f"{url}", response, ex=10)
        return response

    return wrapper


@helper_method
def get_page(url: str) -> str:
    """get_page method"""
    response = requests.get(url)
