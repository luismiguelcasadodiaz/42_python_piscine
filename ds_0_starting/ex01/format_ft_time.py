import time
data = [x for x in dir(time) if not x.startswith('_')]

for e in data:
    print(e.__doc__)