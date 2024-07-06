from functools import wraps
from log import task_logger as log
import yaml

def _format_args(args: dict):
    if args:
        return ', '.join([f"{k} = {repr(v)}" for k, v in args.items()])
    else:
        return "(no args)"

class Runner:
    def __init__(self, parallel: bool = False, from_config: bool = False):
        self._tasks = []
        self._from_config = from_config

    def from_yaml(file: str):
        with open(file) as stream:
            config = yaml.safe_load(stream)['tasks']

        runner = Runner(from_config=True)
        runner._config = config
        return runner

    def task(self, args=None, runs=None):
        if self._from_config:
            def decorator(func):
                @wraps(func)
                def inner(*args, **kwargs):
                    return func(*args, **kwargs)
                
                if runs:
                    log.warn("Runs supplied in decorator will be ignored.")

                name = func.__name__
                cfg_runs = [task[name]['args'] for task in self._config if name in task.keys()]
                for argset in cfg_runs:
                    self._tasks.append((inner, argset))
                return inner

        else:
            def decorator(func):
                @wraps(func)
                def inner(*args, **kwargs):
                    return func(*args, **kwargs)
                if args:
                    self._tasks.append((inner, args))
                elif isinstance(runs, list):
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

