import time
import subprocess
import sys
import keyboard
import psutil
import math
import datetime

defaultTime = 45 #Change this to set a different amount of minutes for work

def killBreakTimers():
    for proc in psutil.process_iter(['cmdline']):
        if proc.info['cmdline'] and 'breakTimer.py' in proc.info['cmdline']:
            if math.isclose(proc.create_time(), time.time(), rel_tol=5):
                continue
            proc.terminate()

def timeBreak(minutes):
    showInfo(minutes)
    time.sleep(minutes*60)
    closeWindow = 'cmd+w' if sys.platform == 'darwin' else 'ctr+w'
    for i in range(2):
        subprocess.Popen(['open', 'breaktime.png'])
        time.sleep(0.95)
        keyboard.send(closeWindow)
        time.sleep(0.5)
    subprocess.Popen(['open', 'breaktime.png'])

def showInfo(minutes):
    breaktime = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    print('\nBreak in', minutes, 'minutes at', breaktime.strftime('%H:%M'))

if __name__ == "__main__":
    killBreakTimers()
    minutes = defaultTime if len(sys.argv) == 1 else int(sys.argv[1])
    timeBreak(minutes)
