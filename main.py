import os
import json
import matplotlib.pyplot as plt
from scipy import signal


def sub_plot_time(row, col, data, Fs, ylabel):
  axes[row, col].plot(data, "k", linewidth=0.1)
  axes[row, col].set_xlim([0, 10547])
  axes[row, col].set_ylabel(ylabel)
  axes[row, col].set_xlabel("Sampling point")
  axes[row, col].grid(color='b', linestyle='--', linewidth=0.1)


def psd(data):
  return signal.welch(data, fs=Fs, window="hamm", nperseg=NFFT, detrend="constant")


def sub_plot_psd(row, col, Pxx, F, Fs, ylabel):
  axes[row, col].semilogy(F, Pxx, "k", linewidth=0.1)
  axes[row, col].set_xlim([F[1], F[-1]])
  axes[row, col].set_ylabel(ylabel)
  axes[row, col].set_xlabel("Frequency (Hz)")
  axes[row, col].grid(color='b', linestyle='--', linewidth=0.1)


# JSON 데이터 폴더 지정
json_path = './test'

# PNG 출력 저장할 폴더 지정
output_path = './result'

# 출력 폴더가 없으면 생성
if not os.path.exists(output_path):
  os.makedirs(output_path)

files = []

for r, d, f in os.walk(json_path):
  for file in f:
    if '.json' in file:
      files.append(os.path.join(r, file))

NFFT = 2**15
Fs = 10547

for f in files:
  print(f)
  with open(f) as json_file:
    data = json.load(json_file)
    F1, Pxx_1 = psd(data["channel1"])
    F2, Pxx_2 = psd(data["channel2"])
    F3, Pxx_3 = psd(data["channel3"])
    F4, Pxx_4 = psd(data["channel4"])
    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(14, 9))
    fig.suptitle(f)
    sub_plot_time(0, 0, data["channel1"], Fs, "channel-1 (g)")
    sub_plot_time(1, 0, data["channel2"], Fs, "channel-2 (g)")
    sub_plot_time(2, 0, data["channel3"], Fs, "channel-3 (g)")
    sub_plot_time(3, 0, data["channel4"], Fs, "channel-4 (g)")
    sub_plot_psd(0, 1, Pxx_1, F1, Fs, "Power spectrum")
    sub_plot_psd(1, 1, Pxx_2, F2, Fs, "Power spectrum")
    sub_plot_psd(2, 1, Pxx_3, F3, Fs, "Power spectrum")
    sub_plot_psd(3, 1, Pxx_4, F4, Fs, "Power spectrum")
    filename = os.path.splitext(os.path.basename(f))
    plt.savefig(output_path+"/"+filename[0]+".png")
    # plt.show()
