import matplotlib.pyplot as plt

def diff(a, b):
    def f(x, s):
        return a*x*s/(1 + s) - x

    def g(x, s):
        return -x*s/(1 + s) - s + b

    h = .01

    x = [4]
    s = [.1]

    for i in range(0, 1000):
        x.append(x[i]+h*f(x[i], s[i]))
        s.append(s[i]+h*g(x[i], s[i]))

    return x, s

a = 1
b = 4

x, s = diff(a, b)
t = range(0, 1001)
plt.plot(t, x)
plt.plot(t, s)

plt.xlabel('t')
plt.ylabel('x (blue), s (green)')
plt.show()
