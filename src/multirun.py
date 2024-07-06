import yaml

from functools import wraps
from log import task_logger as log

def _format_args(args: dict):
    if args:
        return ', '.join([f"{k} = {repr(v)}" for k, v in args.items()])
    else:
        return "(no args)"

class Runner:
    def __init__(self, parallel: bool = False):
        self._tasks = []

    def from_yaml(file: str):
        with open(file) as stream:
            config = yaml.safe_load(stream)['tasks']
            from pprint import pprint
            pprint(config)

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
            log.info(f"[{name}] {_format_args(args)}")
            if args:
                func(**args)
            else:
                func()
            print()

    def get_tasks(self):
        return self._tasks
    
    def __call__(self):
        print("cannot call function directly")

