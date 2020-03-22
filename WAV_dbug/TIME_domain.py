def time_domain(wav_fs, wav_n, wav_data):
    """该函数输入wav文件的采样频率、采样点数、波形的二进制文件产生wav文件的时域图像

    :param wav_fs: 输入由wav_read函数产生的采样频率
    :param wav_n: 输入由wav_read函数产生的采样点数
    :param wav_data: 输入由wav_read函数产生的采样波形（数组）
    :return: 产生图片，返回处理过后的波形wav_numpy[0]
    """
    import numpy as np
    import pylab as plt
    wav_numpy = np.frombuffer(wav_data, dtype=np.short)
    wav_numpy.shape = -1, 1
    wav_numpy = wav_numpy.T / max(wav_numpy[0])
    time = np.arange (0, wav_n) / wav_fs
    plt.figure (1)
    plt.plot (time, wav_numpy[0] * 1.0 / max (abs (wav_numpy[0])))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.xlabel ("time/s")
    plt.ylabel ("振幅/A")
    axes = plt.gca ()
    axes.set_xlim ([0,max(time)])
    axes.set_ylim ([-1, 1])
    plt.grid (1)
    # plt.savefig ('time', dpi=300)
    return wav_numpy[0]