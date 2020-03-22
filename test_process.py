import WAV_read
import TIME_domain
import FFT_domain
import VOICE

from time import process_time
begin_time = process_time()

# address=input('请输入WAV文件格式地址：')
address="C:\\Users\\wzh\\Desktop\\000001.Wav"
(wav_fs, wav_n, wav_data)=WAV_read.wav_read(address)
wav_numpy=TIME_domain.time_domain(wav_fs, wav_n, wav_data)
FFT_domain.fft_domain(wav_numpy, wav_fs, wav_n)
VOICE.voice(wav_numpy, wav_fs)

end_time = process_time()
run_time = end_time-begin_time
print ('程序运行时间：',run_time)