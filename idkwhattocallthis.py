#BIG ALGORITHM THAT CODES IN THAT MATRIX TABLE THING THAT WE MADE
#LAST UPDATED 3/5/24 BY ABBY


import time
import numpy
import my-voice-analysis
from scipy import stats


'''
HEART RATE INPUT FILE FORMAT:
    starting time stamp [integer : sec]
    heart rate data [integer : BPM]
    .
    ..
    ...
    ending time stamp [integer : sec]

VOCAL ANALYSIS INPUT FILE FORMAT:
    current speaker [integer : 1,2,3]
    starting time stamp [integer : sec]
    fundamental frequency data [integer : Hz] articulation rate data [integer]
    .
    ..
    ...
    ending time stamp [integer : sec]
'''


start_time = time.time();
system_status = True;
time_chunk = 10; #TIME TO WAIT BETWEEN ANALYSIS LOOPS


'''
METRICS REFLECT THE CHANGES IN THE ASSOCIATED INPUT DATA:
   * -1 indicates a negative change
   * 0 indicates no change
   * 1 indicates a positive change
'''
hr_metric = None;
ff_metric = None;
ar_metric = None;


hr_data_log = []; #ALL HEART RATE DATA
ff_data_log = []; #ALL FUNDAMENTAL FREQUENCY DATA
ar_data_log = []; #ALL ARTICULATION RATE DATA

current_speaker = None; #CURRENT ANALYSIS SUBJECT VIA DIARIZATION

hr_list = [];
hr_avg = 0;
ff_list = [];
ff_avg = 0;
ar_list[];
ar_avg = 0;
    

#MAIN LOOP THAT CALLS ALL OF THE FUNCTIONS AND DOES ALL OF THE STUFF
while system_status:
    current_time = time.time() - start_time;
    #calculate heart rate
    #calculate fundamental frequency and articulation rate

    try:
        with open('HEARTRATEFILENAME.TXT', 'r') as hr_file:
            hr_content = hr_file.read();
        except FileNotFoundError:
            print("ERROR: Heart-rate input file not found.")

    try:
        with open('VOICESTUFFFILENAME.TXT', 'r') as va_file:
            va_content = va_file.read()
        except FileNotFoundError:
            print("ERROR: Vocal analyis input file not found.")

    hr_content.split('\n');
    hr_content[0] = hr_start_time;
    hr_content.pop(0)
    hr_content[-1] = hr_end_time;
    hr_content.pop()
    hr_list = hr_content;

    
    va_content.split('\n');
    va_content[0] = current_speaker;
    va_content.pop(0)
    va_content[0] = va_start_time;
    va_content.pop(0)
    va_content[-1] = va_end_time;
    va_content.pop()

    va_content.split(' ');
    for i in range(len(va_content)):
        int(va_content[i]);
    
        if i % 2 == 0:
            ff_list.append(i);
        else:
            ar_list.append(i);

    
    time.sleep(time_chunk);
        

#WEIGHTS THE HEART RATE DATA
def hr_weight():
    print("Beginning heart rate analysis... ");
    
    prev_hr_avg = hr_avg;
    hr_avg = sum(hr_list)/len(hr_list);
    delta_hr_avg = hr_avg - prev_hr_avg; #difference between current average and average from previous run

    hr_index = list(range(0,len(hr_list)));

    hr_slope, hr_intercept, hr_r_value, hr_p_value, std_err = stats.linregress(hr_index,hr_list);

    #analyzes the slope of the current data segment
    if hr_slope < 10:
        hr_metric += -3;
    elif hr_slope > 10:
        hr_metric += 3;
    else:
        hr_metric += 0;

    #analyzes the difference between the current and previous averages
        if delta_hr_avg < 0:
            hr_metric += -1;
        elif delta_hr_avg > 0:
            hr_metric += 1;
        else:
            hr_metric += 0;


    print("Heart rate analysis complete!");
    
    return hr_metric

    
#WEIGHTS THE FUNDAMENTAL FREQUENCY DATA
def fr_weight():
    print("Beginning fundamental frequency analysis...");
    prev_fr_avg = fr_avg;
    fr_avg = sum(fr_list)/len(fr_list);
    delta_fr_avg = fr_avg - prev_fr_avg; #difference between current average and average from previous run

    print("Fundamental frequency analysis complete!");
    
    return fr_metric

#WEIGHTS THE ARTICULATION RATE DATA
def ar_weight():
    print("Beginning articulation rate analysis...");
    print("Articulation rate analysis complete!");
    return ar_weight

#CALCULATES THE OUTPUT OF THE MATRIX TO BE SENT TO THE HAPTIC SYSTEM DEPENDING ON THE INPUT DATA
#FOR THE HEART RATE, FUNDAMENTAL FREQUENCY, AND ARTICULATION RATE
def matrix(hr_metric, ff_metric, ar_metric):
    #hr = heart rate
    #ff = fundamental frequency
    #ar = articulation rate
    #mo = matrix output
    #va = vocal analysis

    print("Beginning matrix manipulation calculations...");

    if type(hr_metric) == None:
        raise Exception("ERROR: Heart-rate metric not defined.");
    if type(ff_metric) == None:
        raise Exception("ERROR: Fundamental frequency metric not defined.");
    if type(ar_metric) == None:
        raise Exception("Error: Articulation rate metric not defined.");

    
    mo = 0;
    mo_indicator = 'VALID';

    #CASE STRUCTURE ACCORDING TO MATRIX THINGY
    #SPECIAL CASE INDICATES THAT THE HEART-RATE DATA IS TAKING PRIORITY OF AUDITORY ANALYSIS
    if hr_metric == 0:
        if ff_metric == 0 and ar_rate == 0:
            mo = 0;
        elif (ff_metric == 0 or ar_rate == 0) and (ff_metric < 0 or ff_metric < 0):
            mo = -1;
        elif (ff_metric == 0 or ar_rate == 0) and (ff_metric > 0 or ff_metric > 0):
            mo = 1;
        elif (ff_metric > 0 or ar_rate > 0) and (ff_metric < 0 or ff_metric < 0):
            mo = 'NOT VALID';
            
    elif hr_metric > 0:
        if ff_metric == 0 and ar_rate == 0:
            mo = 1; #SPECIAL CASE
        elif ff_metric > 0 and ar_rate > 0:
            mo = 2;
        elif ff_metric < 0 and ar_rate < 0:
            mo = 1; #SPECIAL CASE
        elif (ff_metric == 0 or ar_rate == 0) and (ff_metric < 0 or ff_metric < 0):
            mo = 1; #SPECIAL CASE
        elif (ff_metric == 0 or ar_rate == 0) and (ff_metric > 0 or ff_metric > 0):
            mo = 1;
        elif (ff_metric > 0 or ar_rate > 0) and (ff_metric < 0 or ff_metric < 0):
            mo = 2; #SPECIAL CASE
            
    elif hr_metric < 0:
        if ff_metric == 0 and ar_rate == 0:
            mo = -1; #SPECIAL CASE
        elif ff_metric > 0 and ar_rate > 0:
            mo = -1; #SPECIAL CASE
        elif ff_metric < 0 and ar_rate < 0:
            mo = -2;
        elif (ff_metric == 0 or ar_rate == 0) and (ff_metric < 0 or ff_metric < 0):
            mo = -2;
        elif (ff_metric == 0 or ar_rate == 0) and (ff_metric > 0 or ff_metric > 0):
            mo = -1; #SPECIAL CASE
        elif (ff_metric > 0 or ar_rate > 0) and (ff_metric < 0 or ff_metric < 0):
            mo = -2; #SPECIAL CASE
            
    return mo;



#SEND SERIAL OUTPUT TO THE HAXYLS TO NOTIFY THE USER AS INDICATED BY THE METRIC OUTPUT
#CALCULATED ABOVE
def haptic_output():
    print("Current Speaker Tag: " + current_speaker);
    
    if mo == -2:
        
    elif mo == -1:
        
    elif mo == 0:

    elif mo == 1:

    elif mo == 2:



#NEED TO FIX THIS THIS SYNTAX DOESNT EXIST LOL WILL FIX LATER
#WRITE TO FILES TO SAVE THE DATA FOR THE ENTIRE ANALYSIS RUN
hr_f= open("heartratedata.txt", "w")
hr_f.write(hr_data_log)
hr_f.close()

ff_f = open("fundamentalfrequency.txt","w")
ff_f.write(ff_data_log)
ff_f.close()

ar_f = open("articulationrate.txt","w")
ar_f.write(ar_data_log)
ar_f.close()












    
    
