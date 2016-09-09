import numpy as np
import matplotlib.pyplot as plt
import treePlotter as tp

def sincosin():
    x=np.linspace(0,10,1000)
    y=np.sin(x)+1
    z=np.cos(x**2) +1

    plt.figure(figsize=(8,4))
    plt.plot(x,y,label= '$\sin x+1 $',color='red',linewidth=2)
    plt.plot(x,z,'b--',label= '$\cos x^2+1$')
    plt.xlabel('TIme(s) ')
    plt.ylabel('Volt ')
    plt.title('A Simple Example')
    plt.ylim(0,2,2)
    plt.legend()
    plt.show()

def tree():
    mytree={'root':{0:'left node',1:{'level2':{3:'left node',4:'right node'}},5:'right node'}}
    tp.createPlot(mytree)

if __name__ == '__main__':
    tree()
