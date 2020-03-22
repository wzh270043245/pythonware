def fft_domain (wav_numpy, wav_fs, wav_n):
    """该函数输入wav文件的波形（一维数组）、采样频率、采样点数产生wav文件的PSD谱图

    :param wav_numpy: wav文件的波形（一维数组）
    :param wav_fs: 
    :param wav_n: 
    :return: 产生图片，无返回值
    """
    import numpy as np
    import pylab as plt
    from scipy.fftpack import fft
    cor_wav = np.correlate (wav_numpy, wav_numpy, mode='full')
    abs_fft_wav= (abs(fft(cor_wav, wav_n)))**2
    idx = np.arange (0, round (wav_n / 2))
    x = idx * wav_fs / wav_n
    y = abs_fft_wav[0:8192]
    plt.figure (2)
    plt.plot (x, y/max(y[1000:10000]))
    plt.ylabel ('归一化幅值/A')
    plt.xlabel ('Frequency/Hz')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    axes = plt.gca ()
    axes.set_xlim ([1000, 10000])
    axes.set_ylim ([0, 1.1])
    plt.grid (1)
    # plt.savefig ('fft', dpi=300)
    return 0