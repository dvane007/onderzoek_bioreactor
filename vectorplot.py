import matplotlib.pyplot as plt
import numpy as np

a = 1.01
b = 1.1
xStart = 2
sStart = 1
xSize = 10
sSize = 3

def f(x, s):
    return a*x*s/(1 + s) - x

def g(x, s):
    return -x*s/(1 + s) - s + b

X = np.linspace(0, xSize, 25)
S = np.linspace(0, sSize, 25)

X, S = np.meshgrid(X, S)

u, v = np.zeros(X.shape), np.zeros(S.shape)

NI, NJ = X.shape

for i in range(NI):
    for j in range(NJ):
        x = X[i, j]
        s = S[i, j]
        u[i, j] = f(x, s)
        v[i, j] = g(x, s)
     
#Vector field
plt.quiver(X, S, u, v, color='r')
plt.axis([0, xSize, 0, sSize])

#Nullclines
A = [(x/100.0)*xSize for x in range(1, 101)]

plt.plot(A, [1/float(a-1) for x in A])
plt.plot([(b-s)*(1+s)/float(s) for s in A], A)
plt.plot(a*(b-1/float(a-1)), 1/float(a-1), '*')

#Solution
def diff(a, b):
    h = .01

    x = [xStart]
    s = [sStart]

    for i in range(0, 10000):
        x.append(x[i]+h*f(x[i], s[i]))
        s.append(s[i]+h*g(x[i], s[i]))

    return x, s

x, s = diff(a, b)
plt.plot(x, s)

#Graph
plt.xlabel('X')
plt.ylabel('S')
plt.show()
