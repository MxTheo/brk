from .. import breakTimer
from .. import brktimeFunc
import os
import time

class TestClass:
    initPassed = 0
    initRemaining = 0
    
    @classmethod
    def setup_class(cls):
        cls.initPassed, cls.initRemaining = brktimeFunc.calcMinsPassedAndRemaining()

    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        os.system(f'brk {cls.initRemaining}')
        
    def teardown_method(self, method):
        process = brktimeFunc.returnBreakProcess()
        if process: process.terminate()
        
    def test_1secBetween(self):
        os.system('brk 5')
        time.sleep(1)
        os.system('brk 10')
        breakTimer.killBreakTimers()
        breakProc = brktimeFunc.returnBreakProcess()
        assert breakProc.cmdline()[2] == '10'
    
    #treshold of 1.57 seconds. Below fails, above succeeds
    def test_1and57secBetween(self):
        os.system('brk 5')
        time.sleep(1.57)
        os.system('brk 10')
        breakTimer.killBreakTimers()
        breakProc = brktimeFunc.returnBreakProcess()
        assert breakProc.cmdline()[2] == '10'
    
    def test_2secBetween(self):
        os.system('brk 5')
        time.sleep(2)
        os.system('brk 10')
        breakTimer.killBreakTimers()
        breakProc = brktimeFunc.returnBreakProcess()
        assert breakProc.cmdline()[2] == '10'