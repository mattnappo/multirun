import subprocess

from multirun import Runner

runner = Runner()

@runner.task()
def simple_task():
    print("hello world")

@runner.task(args={'x': 1, 'y': 2})
def arg_task(x, y):
    print(f"added {x + y}")

@runner.task(runs=[{'x': 1, 'y': 2}, {'x': 5, 'y': 17}])
def echo_task(x, y):
    print(f"hello {x + y}")

@runner.task(runs=[{'cmd': cmd} for cmd in ["uname -a", "df -h /", "whoami"]])
def run_cmd(cmd):
    out = subprocess.run(cmd.split(), shell=True, stdout=subprocess.PIPE)
    output = out.stdout.decode('utf-8')
    print(output)
    return (out.returncode, output)

def test_run():
    print()
    runner.run()
