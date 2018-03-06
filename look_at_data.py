import matplotlib.pyplot as plt
import numpy as np
import json

levels = []
with open('vid-data.txt', 'r') as file:
    levels = json.loads(file.readline())


def f(range, li):
    return (range[1:-1], [(a+b+c)/3 for a, b, c in zip(li, li[1:], li[2:])])


def g(xs, ys, n):
    if(n > 0):
        a, b = f(xs, ys)
        return g(a, b, n-1)
    else:
        return (xs, ys)


def find(xs, ys):
    direction = 'inc'
    points = []
    for i, (a, b) in enumerate(zip(ys, ys[1:])):
        if(a < b):
            if(direction == 'dec'):
                points.append(i)
            direction = 'inc'
        elif(a > b):
            if(direction == 'inc'):
                points.append(i)
            direction = 'dec'
    return [xs[i] for i in points]
    # print('i ', i, ' a ', a, ' b ', b)


smoothing_factor = 10
xs, ys = g(range(len(levels)), levels, smoothing_factor)
print(ys[0:10])
changes = find(xs, ys)
changes_ys = [ys[c] for c in changes]
print(list(zip(map(int, changes), map(int, changes_ys))))
plt.plot(xs, ys, '-')
plt.plot(changes, changes_ys, '*')
plt.show()

with open('frames-i-care-about.txt', 'w') as file:
    file.write(json.dumps(changes))
