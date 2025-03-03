import numpy as np


class Convolution:

    x = None
    xPrePadded = None

    h = None
    hFlippedPostPadded = None

    h_flipped = None

    convLength = 0

    nZerosPrefixPadding = 0
    nZerosSuffixPadding = 0

    result = np.array([])

    def __init__(self, x1, x2):
        self.x = x1
        self.h = x2

        self.convLength = len(self.x) + len(self.h) - 1

        self.nZerosPrefixPadding = self.convLength - len(self.x)
        self.nZerosSuffixPadding = self.convLength - len(self.h)



    def convolve(self):
        self.flip()
        self.padOrignalSequence()
        self.padFlippedSequence()

        self.multiplyAndSum()

        return self.result





    def flip(self):
        self.h_flipped = np.flip(self.h)

    def padOrignalSequence(self):
        self.xPrePadded = self.padSequence(self.x, leftSidePad=self.nZerosPrefixPadding, rightSidePad=0)

    def padFlippedSequence(self):
        self.hFlippedPostPadded = self.padSequence(self.h_flipped, leftSidePad=0,
                                                   rightSidePad=self.nZerosSuffixPadding)

    def padSequence(self, sequence, leftSidePad, rightSidePad):
        return np.pad(sequence, (leftSidePad, rightSidePad), 'constant')

    def multiplyAndSum(self):
        for i in range(0, self.convLength):
            shifted = np.roll(self.hFlippedPostPadded, i)
            res = np.dot(self.xPrePadded, shifted)
            self.result = np.append(self.result, res)