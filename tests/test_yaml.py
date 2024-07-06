from multirun import Runner

runner = Runner.from_yaml("tests/config.yaml")

@runner.task()
def echo(x: str):
    print(f"hello {x}")

@runner.task()
def add(a: int, b: int):
    print(a + b)

def test_run():
    print()
    runner.run()
