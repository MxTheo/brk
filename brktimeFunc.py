
import psutil
import datetime
import breakTimer

def calcMinsPassedAndRemaining():
    '''Returns the mins passed and the mins remaining after the brk call'''
    breakProc = returnBreakProcess()
    if not breakProc:
        print('No breaktimer has started')
        return [0, 0]
    startTime = datetime.datetime.fromtimestamp(breakProc.create_time())
    timeDifference = datetime.datetime.now() - startTime
    
    minsPassed = round(timeDifference.total_seconds() / 60)
    minsRemaining = (breakTimer.defaultTime if len(breakProc.cmdline()) < 3 
                     else int(breakProc.cmdline()[2]))
    minsRemaining = minsRemaining - minsPassed
    return [minsPassed, minsRemaining]

def returnBreakProcess():
    for proc in psutil.process_iter(['cmdline']):
        if (proc.info['cmdline'] and 'breakTimer.py' in proc.info['cmdline']):
            return proc