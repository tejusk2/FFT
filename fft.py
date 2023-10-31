import math
import numpy as np

dimensions = [] #columns, rows

def fast_fourier_transform(data):
    n = len(data)
    if n == 1:
        return data

    #root of unity
    omega = np.exp((2*math.pi*1j)/n)

    #slice lists into even and odd
    even_coefficients = data[::2]
    odd_coefficients = data[1::2]

    #recursive function call
    even_outputs = fast_fourier_transform(even_coefficients)
    odd_outputs = fast_fourier_transform(odd_coefficients)

    #output algorithm into list of size n
    output = np.zeros(n, 'complex_')

    for k in range(int(n/2)):
        output[k] = even_outputs[k] + np.power(omega, k)*odd_outputs[k]
        output[k+int(n/2)] = even_outputs[k] - np.power(omega, k)*odd_outputs[k]

    return output


def normalization(data):
    #find nearest whole integer length that is a power of 2
    x = math.log(len(data),2)
    length = math.pow(2, math.ceil(x))
    #zero pad array to make this length
    diff = int(length - len(data))

    zero_pad = [0]*diff
    return np.append(data, zero_pad)
