from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

from multiprocessing import Process


def f1(name):
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f1, args=('bob',))
    p.start()
    p.join()


from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f2(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f2, args=('bob',))
    p.start()
    p.join()


from multiprocessing import Process, Queue


def f3(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f3, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()


from multiprocessing import Process, Lock


def f4(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()



if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f4, args=(lock, num)).start()
