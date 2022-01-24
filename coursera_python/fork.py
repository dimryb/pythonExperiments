import time
import os

pid = os.fork()

if pid == 0:
    # дочерний процесс
    while True:
        print("Child: ", os.getpid())
        time.sleep(5)
else:
    # родительский процесс
    print("Parent: ", os.getpid())
    os.wait()

