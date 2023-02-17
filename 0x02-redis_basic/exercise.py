#!/usr/bin/env python3
""" Writing string to linux """
import uuid
from typing import Union
import redis


class Cache:
    """"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """
        the <data> should be stored in _redis with a key generated using <UUID>
        :returns the string form of the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
