#import mysolution as mysp
mysp = __import__('my-voice-analysis')
#import my_voice_analysis #as mysp

#f = 'MeetStrawberryShortcake'
file_name = 'homecoming'
c = r'C:\Users\M\Documents\Voice Analysis'
f = file_name + '.5x'
print(f)

mysp.mysptotal(f,c)

f = file_name + '1x'
print('\n' + f)
mysp.mysptotal(f,c)

f = file_name + '1.5x'
print('\n' + f)
mysp.mysptotal(f,c)

f = file_name + '2x'
print('\n' + f)
mysp.mysptotal(f,c)


"""
#RETURN GENDER AND MOOD OF SPEECH
mysp.myspgend(f,c) 

#RETURN NUMBER OF FILLERS/PAUSES
mysp.mysppaus(f,c)

#RETURN RATE OF SPEECH
mysp.myspsr(f,c)

#RETURN ARTICULATION SPEED
mysp.myspatc(f,c)

#RETURN RATIO BETWEEN SPEAKING DURATION & TOTAL SPEAKING DURATION
mysp.myspbala(f,c)

# MEASURE FUNDAMENTAL FREQUENCY DISTRIBUTION MEAN
mysp.myspf0mean(f,c)

# MEASURE FUNDAMENTAL FREQUENCY DISTRIBUTION MEDIUM
mysp.myspf0med(f,c)

# MEASURE FUNDAMENTAL FREQUENCY DISTRIBUTION MINIMUM
mysp.myspf0min(f,c)


results = mysp.mysptotal(f,c)
num_pause = results[1]
rate_speech = results[2]
rate_articulation = results[3]
speech_balance = results[6]
"""


def voice_results(results):
    print('yay!')
