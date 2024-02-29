#BIG ALGORITHM THAT CODES IN THAT MATRIX TABLE THING THAT WE MADE
#LAST UPDATED 2/29 BY ABBY

import time
import numpy
import my-voice-analysis

start_time = time.time();
system_status = True;

hr_list = [];
hr_avg = 0;
ff_list = [];
ff_avg = 0;
ar_list[];
ar_avg = 0;
    

while system_status:
    current_time = time.time() - start_time;
    #calculate heart rate
    #calculate fundamental frequency and articulation rate


#WEIGHTS THE HEART RATE DATA
def hr_weight():
    prev_hr_avg = hr_avg;
    hr_avg = sum(hr_list)/len(hr_list);
    delta_hr = current_hr - hr_list[-1];
    hr_list.append(current_hr);
    delta_hr_avg = hr_avg - prev_hr_avg;

    
#WEIGHTS THE FUNDAMENTAL FREQUENCY DATA
def fr_weight():


#WEIGHTS THE ARTICULATION RATE DATA
def ar_weight():


#CALCULATES THE OUTPUT OF THE MATRIX TO BE SENT TO THE HAPTIC SYSTEM DEPENDING ON THE INPUT DATA
#FOR THE HEART RATE, FUNDAMENTAL FREQUENCY, AND ARTICULATION RATE
def matrix(hr_metric, ff_metric, ar_metric):
    #hr = heart rate
    #ff = fundamental frequency
    #ar = articulation rate
    #mo = matrix output
    
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











    
    
