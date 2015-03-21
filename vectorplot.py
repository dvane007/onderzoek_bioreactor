import matplotlib.pyplot as plt
import numpy as np

time = 100
h = .01
steps = int(time/h)
a = 2.4
b = max(0, 1/(a-1))
xStart = 1
sStart = max(0, 1/(a-1))
xSize = 5
sSize = 5

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

plt.plot([0, xSize], [max(0, 1/float(a-1)), max(0, 1/float(a-1))])
plt.plot([(b-s)*(1+s)/float(s) for s in A], A)
plt.plot(max(0, a*(b-1/float(a-1))), max(0, 1/float(a-1)), '*')

#Solution
def diff(a, b):
    x = [xStart]
    s = [sStart]

    for i in range(0, steps):
        x.append(x[i]+h*f(x[i], s[i]))
        s.append(s[i]+h*g(x[i], s[i]))

    return x, s

x, s = diff(a, b)
plt.plot(x, s)

#Graph
plt.xlabel('X (bacterieconcentratie)')
plt.ylabel('S (voedselconcentratie)')
plt.show()
