import matplotlib.pyplot as plt

time = 100
h = .01
steps = int(time/h)
a = 0.9
b = 5#max(0, 1/(a-1)+1)
xStart = 1
sStart = max(0, 1/(a-1))

def diff(a, b):
    def f(x, s):
        return a*x*s/(1 + s) - x

    def g(x, s):
        return -x*s/(1 + s) - s + b

    x = [xStart]
    s = [sStart]

    for i in range(0, steps):
        x.append(x[i]+h*f(x[i], s[i]))
        s.append(s[i]+h*g(x[i], s[i]))

    return x, s

x, s = diff(a, b)
t = [t*h for t in range(0, steps + 1)]
plt.plot(t, x)
plt.plot(t, s)

plt.xlabel('t')
plt.ylabel('X (blauw), S (groen)')
plt.show()
