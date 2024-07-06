from multirun import Runner

runner = Runner.from_yaml("config.yaml")

@runner.task()
def echo(x: str):
    print(f"hello {x}")

@runner.task()
def add(a: int, b: int):
    print(a + b)

runner.run()
