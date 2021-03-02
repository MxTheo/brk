# brk
A simple breaktimer that results at breaktime.png flashing after the time expires

---

INSTALL:
1. Download the files
2. Extract the files in your custom directory for scripts
3. If you do not have a custom directory for scripts, create one and add the path to your bash_profile
    - For example PATH="/path/to/scripts/:$PATH"
4. If you are running on a different system then Mac OS, change the shebang line in brktime and plsmin
    - WINDOWS: #! python3
    - LINUX:         #! /usr/bin/python3
5. Make files brk, brktime and plsmin executable, by running:
    - chmod +x brk brktime plsmin

PYTHON DEPENDENCIES:
1. subprocess
2. keyboard
3. psutil

---

USAGE:
- brk 30 -> breaktime.png flashing after 30 minutes
- brk       -> breaktime.png flashing after default amount of minutes
- brk -h  -> will output this help info in the terminal

You can reset the break timer by calling the brk command again with the new time set

Thus first calling 'brk 45' and then 'brk 30', will keep the timer to only 30 minutes

---

brktime--This command outputs the minutes passed and the minutes till break timer ends

Example output:

    Passed:    15 minutes
    Till break: 15 minutes

---

plsmin--After calling brk, this command will add or substract minutes to the time.

Take for example brk 15:
- plsmin 5  -> Will result in brk after 20 minutes
- plsmin -5 -> Will result in brk after 10 minutes

---

KNOWN BUGS:
- Sometimes you have to call the brk command twice. If a message is printed in the terminal, then the timer started.
    - The time treshold for succeed consecutive breakcalls is 1.56 seconds. See file test_killBreakTimers.py

---

FOR CONTRIBUTION:

You can find the written unittests in the test directory. These unittests can be run with pytest