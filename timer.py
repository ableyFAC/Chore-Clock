import time as time

washingMachine = 120 # 2 hours 
dryer = 85 

def calculateTime(minutes, seconds):
    if(int(seconds) <= 0):
        seconds = 59
        minutes = int(minutes) - 1
    else:
        seconds = int(seconds) - 1

    if(int(minutes) == 0 and int(seconds) == 0):
        return (0, 0)

    
    return (int(minutes), int(seconds))
        

