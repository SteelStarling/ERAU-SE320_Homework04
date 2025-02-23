#!/usr/bin/env python3

"""Implements a decorator function that implements exponential backoff on failed calls of the decorated function - Copied from CS399
Author:     Taylor Hancock
Class:      SE320
Date:       02/22/2025
Assignment: Back Off Decorator
"""

from random import randint
from time import sleep, asctime

def backoff(initial_delay: float = 0.01, back_off_factor: float = 2, max_delay: float = 5) -> callable:
    """ Convert a function to use an exponential backoff on failed calls

    Keyword Arguments:
    initial_delay - the first delay time following the first failure in seconds (default: 0.01)
    back_off_factor - the factor by which the initial delay is multiplied by after each failure (default: 2)
    max_delay - the maximum delay length in seconds (default: 2.5)
    """

    # Original backoff function
    def backoff_default(func: callable) -> callable:
        delay = 0

        def inner(*args, **kwargs):
            # specify nonlocal
            nonlocal delay, initial_delay, back_off_factor

            sleep(delay)  # sleep for the specified time

            print(f"{asctime()}: will be calling {func.__name__} after {delay} sec delay")
            ret_val = func(*args, **kwargs)
            print(ret_val)

            if ret_val:  # if ever succeeds, reset delay
                delay = 0
            else:
                if delay == 0:  # either set to initial or start incrementing
                    delay = initial_delay
                elif delay < max_delay:
                    delay *= back_off_factor

            # ensure never go over max delay value
            if delay > max_delay:
                delay = max_delay

        return inner
    return backoff_default

@backoff(initial_delay=0.1, back_off_factor=1.5, max_delay=2.5)
def call_shaky_service():
    return 6 == randint(1, 6)

while True:
    print(call_shaky_service())
