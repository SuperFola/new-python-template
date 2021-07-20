#!/usr/bin/env python3

import time


def reporter(name: str):
    """reporter decorator
    Args:
        name (str): step name
    """
    def inner(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            out = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"|____{name} took {(end - start) * 1000:0.3f} ms")
            return out
        return wrapper
    return inner