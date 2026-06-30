import time


def timer(func, interval):
    """
    A decorator that runs a function at a specified interval.

    :param func: The function to be executed.
    :param interval: The time interval (in seconds) between executions.
    """
    def wrapper(*args, **kwargs):
        while True:
            func(*args, **kwargs)
            time.sleep(interval)
    return wrapper