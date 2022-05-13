import time
from playsound import playsound
start_time = time.time()
elapsed_time = time.time() - start_time
from pynput.keyboard import Key, Listener
import keyboard


time_signature = 4
n = 1
tempo_set = 150
tempo_global = 60 / tempo_set



 
def one_bar(timeSig, tempo):
    time_signature = timeSig
    n = 1
    met_on = True
    print(met_on)
    while n <= time_signature:
        print(n)
        if n == 1:
            print("downbeat")
        else:
            print("upbeat")
        time.sleep(tempo)
        n += 1
        if n == time_signature + 1:
            n = 1
    
one_bar(time_signature, tempo_global)

# Collect events until released



    
    
