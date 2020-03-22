import WAV_dbug
from time import process_time
begin_time = process_time()

# address=input('请输入WAV文件格式地址：')
address="C:\\Users\\wzh\\Desktop\\000001.Wav"
(wav_fs, wav_n, wav_data)=WAV_dbug.WAV_read.wav_read(address)
wav_numpy=WAV_dbug.TIME_domain.time_domain(wav_fs, wav_n, wav_data)
WAV_dbug.FFT_domain.fft_domain(wav_numpy, wav_fs, wav_n)
WAV_dbug.VOICE.voice(wav_numpy, wav_fs)

end_time = process_time()
run_time = end_time-begin_time
print ('程序运行时间：',run_time)