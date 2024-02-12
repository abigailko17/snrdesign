# voice profile
import wave
mysp = __import__('my-voice-analysis')
import librosa
import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
import wave

# audio needs to be fed in in small segments
file_name_in = r'C:\Users\M\Documents\Voice Analysis\hiddenFigures.wav'
file_name_out = r'C:\Users\M\Documents\Voice Analysis'
in_name = '\\hiddenFigures'

start = 0
end = 5
segment_length = 5 # length of output segments
data = []
file_out = []
time_stamp = []

with wave.open(file_name_in, "rb") as infile:
    # get file data
    n_channels = infile.getnchannels()
    sample_width = infile.getsampwidth()
    frame_rate = infile.getframerate()
    n_frames = infile.getnframes()
    clip_length = n_frames/frame_rate
    print(infile.getparams())

    while start < math.floor(clip_length):
        # set position in wave to start of segment
        infile.setpos(int(start * frame_rate))
        # extract data
        
        data.append(infile.readframes(int((end-start)*frame_rate)))
        
        time_stamp.append(str(start) + '-'+str(end))
        file_out.append(file_name_out + in_name + str(start) + '-'+str(end) + '.wav')

        start = end
        end = end + segment_length
        
for i in range(len(data)):
    with wave.open(file_out[i], 'w') as outfile:
        outfile.setnchannels(n_channels)
        outfile.setsampwidth(sample_width)
        outfile.setframerate(frame_rate)
        outfile.setnframes(int(len(data[i]) / sample_width))
        outfile.writeframes(data[i])



f0_mean = []
f0_sd = []
f0_max = []
f0_min = []
articulation_rate = []
f0_all = []

for i in range(len(file_out)):
    wav_data, sr = librosa.load(file_out[i],sr=frame_rate,mono=True)
    f0 = librosa.yin(wav_data, fmin = librosa.note_to_hz('C1'), fmax = librosa.note_to_hz('C5'))
    f0_mean.append(np.average(f0))
    f0_sd.append(np.std(f0))
    f0_max.append(np.max(f0))
    f0_min.append(np.min(f0))
    f0_all.append(f0)
    print(time_stamp[i], np.average(f0))

    
plt.plot(time_stamp,f0_mean)
plt.plot(time_stamp,f0_sd)
plt.legend(['Mean', 'Standard Deviation'])
plt.xlabel('Time Interval')
plt.ylabel('Fundamental Frequency')
plt.title('Fundamental Frequency Over Time')
plt.show()
