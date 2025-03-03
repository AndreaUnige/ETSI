import numpy as np
import matplotlib.pyplot as plt

class Plotter:

    def plotConvolution(self, seq1, seq2, result):
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

        fig.suptitle('Convolution')

        plotSingleSignal(ax1, "x1", seq1)
        plotSingleSignal(ax2, "x2", seq2)
        plotSingleSignal(ax3, "x1 * x2", result)

        plt.show()


def plotSingleSignal(axis, title, signalToBePlotted):
    axis.set_title(title)
    axis.stem(signalToBePlotted)
    axis.set_xticks(generateTicks(signalToBePlotted))

def generateTicks(signal):
    return np.linspace(start=0, stop=len(signal) - 1, num=len(signal))
