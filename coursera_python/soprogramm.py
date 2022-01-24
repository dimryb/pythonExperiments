def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


g = grep("python")
next(g) # g.send(None)
# start grep
g.send("golang is better?")
g.send("python is simple!")
# python is simple!
