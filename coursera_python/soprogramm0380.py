# Вызовы сопрограмм, PEP 380

def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep_python_coroutine():
    g = grep("python")
    next(g)
    g.send("python is the best!")
    g.close()


g = grep_python_coroutine()  # is g coroutine?
print(g)

def grep_python_coroutine2():
    g = grep("python")
    yield from g

g = grep_python_coroutine2()  # is g coroutine?
print(g)

g.send(None) # next(g)
g.send("python wow!")
