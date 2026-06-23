from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(4):
    f()
    g()


decor = callLimit(4)

@decor
def p():
    print("p()")

@decor
def s():
    print("s()")

p()
p()
p()
p()
p()
s()
s()
s()
s()
s()
