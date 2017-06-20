#This code requires E.mp3 file to be present in the same Directory
import time , subprocess

timeleft = 10
print('Time Left:' , end='')
while(timeleft > 0):
    print(str(timeleft) + ' ' , end='')
    time.sleep(1)
    timeleft -= 1

subprocess.Popen(['start', 'E.mp3'], shell=True)
