from VowelSynthesizer import generator, dBFilter
import numpy as np
import wave
import os

def make_sound(vowel, f0, duration1, sample_rate = 48000): #vowel은 char, f0은 튜플, duration은 float
    if vowel == 'ㅏ' or vowel == '아':
        f0 = list(f0)
        f0[0] = int(f0[0])
        f0[1] = int(f0[1])

        #배음 몇개 만들어야 할지 계산
        min = f0[0] if f0[0] < f0[1] else f0[1]
        #count = round(1560/min)
        count = 6


        #배음 생성
        output = generator.generate_sin(duration = duration1, freqL=0, freqR=0, dB=-100)
        for i in range(1, count + 1):  #원래 range 퍼스트 1임. 잠깐 디버깅중
            curfreq = i * f0[0]
            nextfreq = i * f0[1]

            #dBFilter에서 주파수 dB 필터 가져와서
            if f0[0] <= f0[1]: #음 상승할때 or 일정할때
                filternp = dBFilter.dBfilterA()[curfreq-1 : nextfreq]
            else: #음 내려갈때
                filternp = dBFilter.dBfilterA()[nextfreq-1 : curfreq]
                filternp = np.flip(filternp)

            #맞게 보간한 다음에
            x = np.linspace(0, 1, abs(curfreq - nextfreq) + 1)
            y = filternp
            new_filter = np.interp(np.linspace(0, 1, int(sample_rate*duration1)), x, y)

            #씌우기
            audio = generator.generate_sin(duration = duration1, freqL=curfreq, freqR=nextfreq, dB=new_filter)
            output = output + audio
        return output



    elif vowel == 'ㅣ' or vowel == '이':
        print("hello, world!")
        return np.array([])
