#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd
from scipy.misc import lena

img = lena()
t = np.arrange(100)
time = np.sin(0.1*t)
real = time[:,np.newaxis, np.newaxis] * img[np.newaxis,...]

# add noise
noisy = real + np.random.randn(*real.shape) * 255




