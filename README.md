## generator.py
.generate_sin(sample_rate, duration, freq, bit_depth, dB)
- sample_rate: 샘플레이트... 기본값은 48000
- duration: 지속시간(실수, 단위는 초)... 기본값은 10.0
- freq: 주파수(Hz)... 기본값은 1000
- bit_depth: ㄹㅇ 말 그대로, 별로 중요한 요소 아님... 기본값은 0
- dB: 데시벨... 근데 10까지만 소리 안깨지고 조금이라도 커지면 깨짐... 기본값은 0

- numpy.ndarray형을 반환함

.write_wav(filename, stereo_data, sample_rate, bit_depth)
- filename: 스트링으로 받음. 파일 이름임. 뒤에 자동으로 .wav가 붙어서 저장됨
- stereo_data: numpy.ndarray형이 들어감. 위의 .generate_sin()로 만든애가 들어갈 수 있음
- sample_rate: 샘플레이트... 기본값은 48000
- bit_depth: ㄹㅇ 말 그대로, 별로 중요한 요소 아님... 기본값은 0



다음 계획은
피치 곡선까지 구현해서 --> 이 과정에서 각 모음별 주파수 볼륨 필터 필요
프리셋까지 만들어두는것