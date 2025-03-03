import numpy as np


class Convolution:

    x = None
    xPrePadded = None

    h = None
    h_flipped = None
    hFlippedPostPadded = None

    convolutionLength = 0

    nZerosPadding__prefix = 0
    nZerosPadding__suffix = 0

    convolutionResult = np.array([])

    def __init__(self, x1, x2):
        self.x = x1
        self.h = x2

        self.convolutionLength = len(self.x) + len(self.h) - 1

        self.nZerosPadding__prefix = self.convolutionLength - len(self.x)
        self.nZerosPadding__suffix = self.convolutionLength - len(self.h)



    def convolve(self):
        self.flip()
        self.padOriginalSequence()
        self.padFlippedSequence()

        self.multiplyAndSum()

        return self.convolutionResult





    def flip(self):
        self.h_flipped = np.flip(self.h)

    def padOriginalSequence(self):
        self.xPrePadded = self.padSequence(self.x, leftSidePad=self.nZerosPadding__prefix, rightSidePad=0)

    def padFlippedSequence(self):
        self.hFlippedPostPadded = self.padSequence(self.h_flipped, leftSidePad=0,
                                                   rightSidePad=self.nZerosPadding__suffix)

    def padSequence(self, sequence, leftSidePad, rightSidePad):
        return np.pad(sequence, (leftSidePad, rightSidePad), 'constant')

    def multiplyAndSum(self):
        for i in range(0, self.convolutionLength):
            shifted = np.roll(self.hFlippedPostPadded, i)
            res = np.dot(self.xPrePadded, shifted)
            self.convolutionResult = np.append(self.convolutionResult, res)