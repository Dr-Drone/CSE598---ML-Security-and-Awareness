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

for i in tqdm(range(6245)):
    sound_1 = AudioSegment.from_file("UrbanSound8K/audio" + df.loc[i,'relative_path'])
    sound_2 = AudioSegment.from_file("attack_noise/attack_noise.mp3")
    combined = sound_1.overlay(sound_2)
    filename = str(uuid.uuid4())
    combined.export("./UrbanSound8K/audio/Attack_Data_Set/"+filename+".wav", format='wav')
    df.loc[i + length,'relative_path'] = "/Attack_Data_Set/" +filename+ ".wav"
    df.loc[i + length,'classID'] = 10
df.to_csv("dataset_location.csv")
#17463

