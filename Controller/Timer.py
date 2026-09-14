import time
from functools import wraps
from Model.HandleJSON import HandleJSON



def timer(func=None):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            handle_json = HandleJSON()
            interval = handle_json.deserialize_json_config().get("interval", 15)
            while True:
                fn(*args, **kwargs)
                time.sleep(interval)

        return wrapper

    if callable(func):
        return decorator(func)
    return decorator
