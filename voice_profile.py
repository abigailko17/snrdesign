# voice profile
import wave
mysp = __import__('my-voice-analysis')
import librosa
import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
import pandas as pd
#from pydub import AudioSegment

# audio needs to be fed in in small segments
file_name_in = r'C:\Users\M\Documents\Voice Analysis\hiddenFigures.wav'
file_name_out = r'C:\Users\M\Documents\Voice Analysis'
in_name = '\\hiddenFigures'

import wave
start_i = 0
end_i = 5
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

    infile.setpos(0)
    signal_wave = infile.readframes(n_frames)
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    l_channel = signal_array[0::2]
    r_channel = signal_array[1::2]
    times = np.linspace(0,clip_length,num=n_frames)

    all_peaks, _ = scipy.signal.find_peaks(l_channel,height=1000)
    peak_idx = []
    # idk what the actual threshhold for a person speaking should be but lets say 1000 for now
    temp_amp = np.array(l_channel) # array of amplitudes
    threshold = np.mean(temp_amp)
    w = 1000
    for i in all_peaks:
        if i < w:
            if l_channel[i] >= max(l_channel[i:i+w]):
                peak_idx.append(i)
        elif i > len(l_channel) - w:
            if l_channel[i] >= max(l_channel[i-w:i]):
                peak_idx.append(i)
        else:
            if l_channel[i] >= max(l_channel[i-w:i+w]):
                peak_idx.append(i)

    amps = []
    t_peak = []
    tot_time = [] # time separated by time ranges
    tot_amp = [] # amplitudes separated by time ranges            
    temp_peak = np.array(peak_idx) # array of peak amplitude indices
    temp_t = np.array(times) # array of times

    while start_i < math.floor(clip_length):
        # set position in wave to start of segment
        infile.setpos(int(start_i * frame_rate))
        # extract data
        t1 = temp_t[temp_t >= start_i]
        t = t1[t1 < end_i] #find times that are between start and end time 
        tot_time.append(t) # add times between start and end to total time array
        a = l_channel[temp_t >= start_i]
        a1 = a[t1 < end_i]
        amp = l_channel
        tot_amp.append(a1)
        
        data.append(infile.readframes(int((end_i-start_i)*frame_rate))) # add frames to data for f0 measurement
        
        time_stamp.append(str(start_i) + '-'+str(end_i)) # name of time range
        file_out.append(file_name_out + in_name + str(start_i) + '-'+str(end_i) + '.wav')

        peak1 = temp_peak[times[temp_peak] < end_i] # indices peaks that are in time range
        peak = peak1[times[peak1] >= start_i]
        t_peak.append(times[peak])
        amps.append(l_channel[peak])
        
        start_i = end_i
        end_i = end_i + segment_length

    """
    figure, axis = plt.subplots(3,1)
    axis[0].plot(times,l_channel)
    axis[0].set_title('Left Channel')
    axis[0].set_ylabel('Signal Value')
    axis[0].set_xlabel('Time (s)')
    axis[0].set_xlim(0, clip_length)

    axis[1].specgram(l_channel, Fs = frame_rate, vmin = -20, vmax = 50)
    #axis[1].plot(times,frame_rate)
    axis[1].set_title('Left Channel')
    axis[1].set_ylabel('Frequency (Hz)')
    axis[1].set_xlabel('Time (s)')
    axis[1].set_xlim(0, clip_length)
    #plt.colorbar()
    """
    
    """          
    for i in range(1,len(l_channel)):
        if l_channel[i] > w:
            if i < w:
                if l_channel[i] >= max(l_channel[i:i+w]):
                    peak_idx.append(i)
            elif i > len(l_channel) - w:
                if l_channel[i] >= max(l_channel[i-w:i]):
                    peak_idx.append(i)
            else:
                if l_channel[i] >= max(l_channel[i-w:i+w]):
                    peak_idx.append(i)
    """
    
    #for i in range(all_peaks):
    #peak_idx = all_peaks
    """  
    axis[0].plot(times[peak_idx],l_channel[peak_idx],'r.')

    wav_data, sr = librosa.load(file_name_in,sr=frame_rate,mono=True)
    f0 = librosa.yin(wav_data, fmin = librosa.note_to_hz('C1'), fmax = librosa.note_to_hz('C5'))
    axis[2].plot(f0)
    axis[2].set_xlim(0, clip_length*100)
    plt.show()

    #audio = AudioSegment.from_file(file_name_in)
    #audio.play()
    print(times[peak_idx])
    plt.plot(times,l_channel)
    plt.title('Left Channel')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
    plt.xlim(0, clip_length)
    plt.plot(times[peak_idx],l_channel[peak_idx],'r.')
    plt.axvline(x=0, color='r', linestyle='--')
    plt.axvline(x=len(l_channel),color='r',linestyle='--')
    plt.show()
    """
        
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

    plt.plot(tot_time[i],tot_amp[i])
    plt.title('Left Channel')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
    plt.xlim(tot_time[i][0],tot_time[i][len(tot_time[i])-1])
    plt.plot(t_peak[i],amps[i],'r.')
    plt.show()
    
    print(time_stamp[i], np.average(f0), " syllables: ", len(amps[i]))

    
plt.plot(time_stamp,f0_mean)
plt.plot(time_stamp,f0_sd)
plt.legend(['Mean', 'Standard Deviation'])
plt.xlabel('Time Interval (s)')
plt.ylabel('Fundamental Frequency (Hz)')
plt.title('Fundamental Frequency Over Time')
plt.show()

