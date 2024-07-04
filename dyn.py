import subprocess

from autorun import Runner

def _run(cmd):
    out = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    ret = out.returncode
    output = out.stdout.decode('utf-8')
    return (ret, output)

runner = Runner()

@runner.task()
def simple_task():
    print("hello world")

@runner.task(runs=[{'x': 1, 'y': 2}, {'x': 5, 'y': 17}])
def echo_task(x, y):
    print(f"hello {x + y}")

runner.run() # this line will cause echo_task to run with the args x=1 and y=2


@runner.task()
def run_task():
    print(_run("uname -a")[1].strip())



#print(runner.get_tasks())

runner.run()


#runner.config()
