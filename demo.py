import functools

class Runner:
    def __init__(self):
        self.tasks = []

    def task(self, *args, **kwargs):
        if len(args) == 1 and callable(args[0]):  # Check if decorator is used without parentheses
            func = args[0]
            args = {}
        else:
            args = args[0] if args else {}  # Extract args if passed as positional argument
            func = None

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            # Always add to tasks even if args or kwargs are empty
            self.tasks.append((wrapper, args))

            return wrapper

        if func:
            return decorator(func)
        else:
            return decorator

    def run(self):
        for task_func, task_args in self.tasks:
            task_func(**task_args)

# Example usage:
runner = Runner()

@runner.task(args={'x': 1, 'y': 2})
def echo_task(x, y):
    print(f"hello {x + y}")

@runner.task
def simple_task():
    print("This is a simple task")

runner.run()
