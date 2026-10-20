#여기다가 dB 넘파이 배열 만드는 함수 다 해놓고, 그 함수들을 gen_vowel에서 쓰자!

import numpy as np
import wave
import os

def dBfilterA():
    lin1 = np.linspace(-100, -30, 260) #-0
    lin2 = np.linspace(-30, -15, 260) #0-1
    lin3 = np.linspace(-15, -13, 260) #1-2
    lin4 = np.linspace(-13, -1, 260) #2-3
    lin5 = np.linspace(-1, -2, 260)  #3-4
    lin6 = np.linspace(-2, -3, 260) #4-5
    lin7 = np.linspace(-3, -500, 1300) #5-
    lin8 = np.linspace(-500, -500, 24000)

    output = np.append(lin1, lin2)
    output = np.append(output, lin3)
    output = np.append(output, lin4)
    output = np.append(output, lin5)
    output = np.append(output, lin6)
    output = np.append(output, lin7)
    output = np.append(output, lin8)

    return output
