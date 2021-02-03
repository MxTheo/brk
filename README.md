# brk
A simple breaktimer that results at breaktime.png flashing after the time expires

DEPENDENCIES:
1. subprocess
2. keyboard
3. psutil
  
---

USAGE:
- brk 30 -> breaktime.png flashing after 30 minutes
- brk    -> breaktime.png flashing after default amount of minutes

You can reset the break timer by calling the brk command again with the new time set

Thus first calling 'brk 45' and then 'brk 30', will keep the timer to only 30 minutes

---

brktime--This command outputs the minutes passed and the minutes till break timer ends

Example output:

    Passed:    15 minutes
    Till break: 15 minutes
