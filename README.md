# Convolution
Simple python code that shows how to implement the convolution between 2 sequences.

<h3>The convolution formula</h3>

$y(n) = x(n) * h(n) = \displaystyle\sum_{k=-\infty}^{\infty} x(k) h(n-k)$

<h3>Working principle:</h3>

The convolution is implemented in the simplest way, without the employment of any libraries.
The followed algorithm comes straight from the definition:
 - Flip one signal
 - Shift it 
 - Multiply and Sum
<br><br>


At the end of the computation, the code shows the result both on the python console and as a simple stem plot.

<h3>Useful Links:</h3>

- https://numpy.org/devdocs/reference/generated/numpy.convolve.html
- https://matplotlib.org/
