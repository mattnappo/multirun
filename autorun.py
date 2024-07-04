from functools import wraps
from log import task_logger as log

class Runner:
    def __init__(self, parallel: bool = False):
        self._tasks = []

    def task(self, runs=None):
        def decorator(func):
            @wraps(func)
            def inner(*args, **kwargs): # remove arg
                return func(*args, **kwargs)
            if isinstance(runs, list):
                for argset in runs:
                    self._tasks.append((inner, argset))
            else:
                self._tasks.append((inner, runs))
            return inner
        return decorator

    def run(self):
        for func, args in self._tasks:
            name = func.__name__
            log.info(f"[RUN {name}]: args = {args}")
            if args:
                func(**args)
            else:
                func()
            print()

    def get_tasks(self):
        return self._tasks
    
    def __call__(self):
        print("cannot call function directly")

