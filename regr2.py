import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class RM:
    x=np.array([0,1,2,3,4,5,6,7,8,9,10.])
    y=np.array([0,4,6,5,8,6,9,8,9,9,9.0])
    xt=np.array([11,12,13,14,15,16,17,18,19,20])
    yt=np.array([9,9,11,10,12,13,12,14,13,15])

    def f(self, x, a,b,c,d,e):
        return a*x+b
        #return a*x**3+b*x**2+c*x+d
        #return a*x**4+b*x**3+c*x**2+d*x+e

    def plot_train(self):
        plt.plot(self.x, self.y, 'o')

    def fit(self):
        popt, pcov = curve_fit(self.f, self.x, self.y)
        self.popt=popt

    def plot_model(self):
        x=np.arange(0,10,0.1)
        plt.plot(x, self.f(x,*self.popt))

    def score(self):
        return np.corrcoef(self.yt, self.f(self.xt, *self.popt))[0,1]**2

model=RM()
model.fit()
model.plot_train()
model.plot_model()
print(model.score())
plt.show()