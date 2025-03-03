import numpy as np
from Convolution import Convolution
from Plotter import Plotter

x1 = np.array([3, 3, 3, 3, 3])
x2 = np.array([2, 2, 2])

myPlt = Plotter()

if __name__=="__main__":
    c = Convolution(x1, x2)
    result = c.convolve()

    myPlt.plotConvolution(x1, x2, result)
    print(result)

