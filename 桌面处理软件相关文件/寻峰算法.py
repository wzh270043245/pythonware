import WAV_read
import TIME_domain
import numpy as np
import pylab as plt
from scipy.fftpack import fft
from time import process_time
from scipy.signal import find_peaks
begin_time = process_time()

# address=input('请输入WAV文件格式地址：')
address="C:\\Users\\wzh\\Desktop\\220kV西衙门\\000352.Wav"
(wav_fs, wav_n, wav_data)=WAV_read.wav_read(address)
wav_numpy=TIME_domain.time_domain(wav_fs, wav_n, wav_data)
cor_wav = np.correlate (wav_numpy, wav_numpy, mode='full')
abs_fft_wav= (abs(fft(cor_wav, wav_n)))**2
idx = np.arange (0, round (wav_n / 2))
x = idx * wav_fs / wav_n
y = abs_fft_wav[0:8192]
plt.figure (2)
print(len(x))
print(len(y))
print(max (y[1000:8192]))
print(max (y[100:8192]))
plt.plot (x,y)
y=y/ max (y[1000:8192])
y_max = max(y[10:8192])
x_index = np.where(y == y_max)
print(y_max,type(x_index))
print(x_index[0][0])
print(x[x_index[0][0]])
# y_max,x_index = max(y[1000:10000])
# print(y_max,x_index)
# indices = find_peaks(y, height=None, threshold=None, distance=10000,
#                prominence=None, width=None, wlen=None, rel_height=None,
#                plateau_size=None)
# print(indices)
# plt.plot(indices[0], y[indices[0]], 'o')
plt.ylabel ('归一化幅值/A')
plt.xlabel ('Frequency/Hz')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
axes = plt.gca ()
# axes.set_xlim ([1000, 10000])
# axes.set_ylim ([0, 1.1])
plt.grid (1)
plt.show()