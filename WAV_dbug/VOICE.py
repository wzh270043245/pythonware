def voice(wav_numpy,wav_fs):
    """该函数输入wav文件的波形（一维数组）、采样频率产生语谱图

    :param wav_numpy: 输入wav文件的波形（一维数组）
    :param wav_fs: 输入wav文件的采样频率
    :return: 产生图片，无返回值
    """
    import numpy as np
    import pylab as plt
    plt.figure (3)
    plt.specgram (wav_numpy, Fs=wav_fs, scale_by_freq=True, sides='default')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.ylabel ('Frequency/Hz')
    plt.xlabel ('Time/s')
    axes = plt.gca ()
    axes.set_ylim ([0, 10000])
    # plt.savefig ('voice', dpi=300)
    plt.show()
    return 0