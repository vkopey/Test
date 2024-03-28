import matplotlib.pyplot as plt

def f(a,b):
    Y=[]
    for x in [0,1,2,3,4,5,6,7,8,9,10]:
        Y.append(a*x+b)
    return Y

def MNK(X,Y,a,b):
    S=0
    for x,y in zip(X,Y):
        f=a*x+b
        S+=(f-y)**2
    return S

X=[0,1,2,3,4,5,6,7,8,9,10]
Y=[0,4,6,5,8,6,9,8,9,9,9.0]

plt.plot(X,Y, 'o')

R=[]
for a in [x/10.0 for x in range(30)]:
    for b in [x/10.0 for x in range(30)]:
        R.append((MNK(X,Y,a,b), a, b))

R.sort()
a=R[0][1]
b=R[0][2]
plt.plot(X, [a*x+b for x in X])
plt.show()