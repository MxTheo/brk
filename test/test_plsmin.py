from .. import brktimeFunc
import os
import time
import subprocess

class TestClass:
    initPassed = 0
    initRemaining = 0
    
    @classmethod
    def setup_class(cls):
        cls.initPassed, cls.initRemaining = brktimeFunc.calcMinsPassedAndRemaining()

    @classmethod
    def teardown_class(cls):
        time.sleep(1.6)
        os.system(f'brk {cls.initRemaining}')

    def teardown_method(self, method):
        process = brktimeFunc.returnBreakProcess()
        if process: process.terminate()

    def test_add5(self):
        os.system('brk 15')
        time.sleep(1.7)
        os.system('plsmin 5')
        passed, remaining = brktimeFunc.calcMinsPassedAndRemaining()
        assert passed == 0
        assert remaining == 20
    
    def test_min5(self):
        os.system('brk 15')
        time.sleep(1.7)
        os.system('plsmin -5')
        passed, remaining = brktimeFunc.calcMinsPassedAndRemaining()
        assert passed == 0
        assert remaining == 10

    def test_to0(self):
        os.system('brk 5')
        time.sleep(1.7)
        message = subprocess.run(['plsmin','-5'], capture_output=True, text=True)
        assert message.stdout[10] == '0'
    
    def test_toMin5(self):
        os.system('brk 5')
        time.sleep(1.7)
        message = subprocess.run(['plsmin','-10'], capture_output=True, text=True)
        assert message.stdout[10] == '0'
        
    def test_empty(self):
        os.system('brk 15')
        time.sleep(1.7)
        os.system('plsmin')
        passed, remaining = brktimeFunc.calcMinsPassedAndRemaining()
        assert passed == 0
        assert remaining == 15