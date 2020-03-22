def wav_read(address):
    """该函数输入wav文件的地址

    :param address: 输入变量为字符串格式变量
    :return: 返回wav文件的采样频率wav_fs、采样点数wav_n、波形的二进制文件wav_data
    """
    import wave
    import numpy as np
    read_wav = wave.open (address, "r")
    wav_fs = read_wav.getframerate ()
    wav_n = read_wav.getnframes ()
    wav_data = read_wav.readframes (wav_n)
    read_wav.close ()
    return wav_fs,wav_n,wav_data
