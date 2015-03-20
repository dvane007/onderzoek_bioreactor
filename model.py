import matplotlib.pyplot as plt

steps = 10000

def diff(a, b):
    def f(x, s):
        return a*x*s/(1 + s) - x

    def g(x, s):
        return -x*s/(1 + s) - s + b

    h = .01

    x = [0.1]
    s = [1/(a-1)]

    for i in range(0, steps):
        x.append(x[i]+h*f(x[i], s[i]))
        s.append(s[i]+h*g(x[i], s[i]))

    return x, s

a = 2.4
b = 1/(a-1)+1

x, s = diff(a, b)
t = range(0, steps + 1)
plt.plot(t, x)
plt.plot(t, s)

plt.xlabel('t')
plt.ylabel('x (blue), s (green)')
plt.show()
