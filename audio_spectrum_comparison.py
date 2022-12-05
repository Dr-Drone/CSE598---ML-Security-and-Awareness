# ----------------------------
# Creating an attack Dataset
# ----------------------------
import pandas as pd
from pathlib import Path
from pydub import AudioSegment
import uuid
import numpy

from tqdm import tqdm

#pydub used to convolve sound data
 

#Instructions
''''
You need to have a filder in the subdirectry of UrbanSound8K/audio/ named Attack_Data_Set for this script to work
You also need to have a the attack noise stored in a folder called /attack_noise/ in root

The script used metadata file to read original file location, it then uses that to add noise to the data
# Attcack noise taken from: https://github.com/rub-ksv/adversarialattacks/tree/316b1f026cc55ee5c712240be656c68da940d743/docs/audio

'''

download_path = Path.cwd()/'UrbanSound8Kcopy.csv'

# Read metadata file
metadata_file = '/Users/pawanvijayanagar/Documents/ASU Masters/CSE598 - Machine Learning Security and Fairness/Midterm_Check/UrbanSound8K/metadata/UrbanSound8K.csv'
df = pd.read_csv(metadata_file)
df.head()

# Construct file path by concatenating fold and file name
df['relative_path'] = '/fold' + df['fold'].astype(str) + '/' + df['slice_file_name'].astype(str)

# Take relevant columns
df = df[['relative_path', 'classID']]
df.head()


print(len(df))
print(df.loc[1,'relative_path'])
length = len(df)

sound_1 = AudioSegment.from_file("UrbanSound8K/audio" + df.loc[15,'relative_path'])
sound_2 = AudioSegment.from_file("attack_noise/attack_noise.mp3")
combined = sound_1.overlay(sound_2)
filename = str(uuid.uuid4())
combined.export("haha.wav", format='wav')






import wave
wav_obj = wave.open("UrbanSound8K/audio" + df.loc[15,'relative_path'], 'rb')
sample_freq = wav_obj.getframerate()

n_samples = wav_obj.getnframes()
t_audio = n_samples/sample_freq

n_channels = wav_obj.getnchannels()
signal_wave = wav_obj.readframes(n_samples)

import numpy as np
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

times = np.linspace(0, n_samples/sample_freq, num=n_samples)

import matplotlib.pyplot as plt
plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Dog Barking Sterile Audio')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()
