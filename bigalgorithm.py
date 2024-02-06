#CURRENTLY DEFINING A SCALE FROM 1 - 10 WHERE 0=CALM, 5=NEUTRAL, 10=ANGRY

import serial
import time

mysp=__import__('my_voice_analysis')
f="AUDIO_FILE_NAME"
c=r"FILE_NAME"


##VOICE ANALYSIS WEIGHTING (sr = speech rate, fp = # of fillers/pauses)
sr_list = [];
sr_avg = 0;

def voice_calc(current_sr, current_fp):
    prev_sr_avg = sr_avg;
    sr_avg = sum(sr_list)/len(sr_list);
    delta_sr = current_sr - sr_list[-1];
    sr_list.append(current_sr);
    delta_sr_avg = sr_avg - prev_sr_avg;


    #calculate a metric based off rate of speech in comparison to previous rates
    #assuming that slower rate indicated calm and faster indicates anger
    if delta_sr == 0:
        sr_metric = 5;
    elif delta_sr < -5 and delta_sr_avg < -5:
        sr_metric = 0;
    elif delta_sr < -2 and delta_sr_avg < -2:
        sr_metric = 3;
    elif delta_sr > 5 and delta_sr_avg > 5:
        sr_metric = 10;
    elif delta_sr > 2 and delta_sr_avg > 2:
        sr_metric = 6;
    else:
        sr_metric = None;
        print("POTENTIAL ERROR IN delta_st sr calculations")


    #calculate a metric based off of the number of pauses/fillers used without comparing to previous numbers
    #assuming that less fillers indicate calm and more indicates anger
    fp_range = [1,20]
    fp_metric = current_fp/(fp_range[1]-fp_range[0])*10;

    
    return [sr_metric, fp_metric]
    

##HEARTRATE ANALYSIS WEIGHTING TBD
hr_list = [];
hr_avg = 0;

def hr_calc(current_hr):
    prev_hr_avg = hr_avg;
    hr_avg = sum(hr_list)/len(hr_list);
    delta_hr = current_hr - hr_list[-1];
    hr_list.append(current_hr);
    delta_hr_avg = hr_avg - prev_hr_avg;


    hr_metric = 6;
    
    return hr_metric



##BIG MAJOR ALGORITHM TBD
def algorithm():
    return 0



##HAPTIC OUTPUT STUFF TBD

ser = serial.Serial1('DEVICE NAME', 9600)

def control_boards('BOARD ID'):

    

##HELLA HELLA TBD :)
#weights indicate how heavily each metric affects the haptic output
sr_weight = 0.2;
fp_weight = 0.2;
hr_weight = 0.6;

is_active = True;
current_fp = 0;
current_sr = 0;
current_hr = 0;
voice_metric = [];


while is_active:
    current_sr = mysp.myspsr(f,c);
    current_fp = mysp.myspaus(f,c);

    voice_metric = voice_calc(current_sr, current_fp);
    hr_metric = hr_calc(current_hr);

    metrics = [voice_metric(0)*sr_weight, voice_metric(1)*fp_weight, hr_metric*hr_weight];
    
    final_output = sum(metrics)/10;

    is_active = False;
    break
    







