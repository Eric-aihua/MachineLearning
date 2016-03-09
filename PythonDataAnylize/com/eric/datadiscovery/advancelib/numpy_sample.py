__author__ = 'Eric'
import numpy as np

def numpy_sample():
        #define array
        a = np.array([1, 2, 3, 4])
        b = np.array((5, 6, 7, 8))
        c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])

        #print array length
        print(a.shape)
        print(b.shape)
        print(c.shape)
        print(c*c)

        #np function test
        range_items=np.arange(0,3,0.1)
        print(range_items)

        linspace_items=np.linspace(1,5,30)
        print(linspace_items)



numpy_sample()