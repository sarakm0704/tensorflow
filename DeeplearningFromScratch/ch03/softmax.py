import numpy as np
#probability
def softmax(a):
    c = np.exp(a)
    exp_a = np.exp(a - c) #overflow
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
