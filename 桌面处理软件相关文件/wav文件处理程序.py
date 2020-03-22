import wave
import numpy as np
from scipy.fftpack import fft   # 只能从scipy中的fftback模块导入fft，这样fft才可用，若直接导入scipy或scipy.fftback则不能使用fft
import pylab as plt
# from time import process_time
# begin_time = process_time()

read_wav = wave.open(r"C:\Users\wzh\Desktop\000001.Wav","rb")

# 1.返回声道数量 int
wav_nchannels = read_wav.getnchannels()
# 2.返回字节长度 int
wav_sampwidth = read_wav.getsampwidth()
# 3.返回采样频率 int
wav_framerate = read_wav.getframerate()
# 4.返回音频总帧数（采样点） int
wav_nframerate = read_wav.getnframes()
# 读取wav文件的波形
wav_data = read_wav.readframes(wav_nframerate)
read_wav.close()

# 时域图像
# wav_numpy = np.fromstring(wav_data,dtype=np.short)
wav_numpy = np.frombuffer(wav_data,dtype=np.short)
wav_numpy.shape=(-1,1)

wav_numpy=wav_numpy.T

wav_numpy = wav_numpy/max(wav_numpy[0])

time = np.arange(0,wav_nframerate)/wav_framerate

plt.figure(1)
plt.plot(time,wav_numpy[0]*1.0/max(abs(wav_numpy[0])))
plt.rcParams['font.sans-serif']=['SimHei']# 显示中文
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
plt.xlabel("时间")
plt.ylabel("幅值")
plt.grid(1)


# 功率谱密度图
# TODO 函数自相关的计算
cor_wav = np.correlate(wav_numpy[0],wav_numpy[0],mode='full')
# # TODO FFT
fft_wav = fft(cor_wav,wav_nframerate)
# # 取绝对值
abs_fft_wav = np.abs(fft_wav)

idx=np.arange(0,round(wav_nframerate/2))
k=idx * wav_framerate/wav_nframerate
y=abs_fft_wav[0:8192]

plt.figure(2)
plt.plot(k,y)
axes=plt.gca()
axes.set_xlim([1000,10000])
# axes.set_ylim([0,10000])
plt.grid(1)

# 语谱图
plt.figure(3)
plt.specgram(wav_numpy[0],Fs = wav_framerate, scale_by_freq = True, sides = 'default')
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')
axes=plt.gca()
axes.set_ylim([0,10000])

# end_time = process_time()
# run_time = end_time-begin_time
# print ('程序运行时间：',run_time)

plt.show()
