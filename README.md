# multirun

Simple zero-dependence Python tool to configure multiple runs of a set of functions.

## Example

### Setup

In a Python file, create a `Runner` which manages task configuration and state.

```
from multirun import Runner
runner = Runner()
```

### Add a static task

This will add the `hello` function to the `Runner`.

```
@runner.task()
def hello():
    print("Hello multirun")
```

To run the `Runner`,

```
runner.run()
```

This will output

```
[hello] (no args)
Hello multirun
```

### Single-run task

Now, let's make a function that requires two arguments.

```
@runner.task(args={'x': 4, 'y': 7})
def sum(x: int, y: int):
    print(x + y)

runner.run()
```

This will output:

```
[sum] x = 4, y = 7
11
```

### Multi-run task

You can also specify a list of argument `dict`s with `runs=`. This will will run
the function once per each argument set.

```
@runner.task(runs=[{'x': 8, 'y': 1}, {'x': 1, 'y': 2})
def sum(x: int, y: int):
    print(x + y)

runner.run()
```

This will output:
```
[sum] x = 8, y = 1
9

[sum] x = 1, y = 2
3
```

## Parsing from YAML

You can also specify your task runs in a yaml file. Here is an example:

```
# config.yaml

tasks:
  - echo:
      args:
        x: 'world'
  - echo:
      args:
        x: 'matt'
  - add:
      args:
        a: 4
        b: 3
```

Then, create a `Runner` from the configuration:

```
from multirun import Runner
runner = Runner.from_yaml("config.yaml")

@runner.task()
def echo(x):
    print(f"Hello {x}")

@runner.task()
def add(a, b):
    print(a + b)

runner.run()
```

Output:
```
[echo] x = 'world'
Hello world

[echo] x = 'matt'
Hello matt

[add] a = 4, b = 3
7
```

You can see more examples in `tests/`.

