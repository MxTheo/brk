# brk
A simple breaktimer that results at breaktime.png flashing after the time expires

INSTALLING:
- Download the files (into zip)
- Extract the files into a directory which is in your bash $PATH
- In the brk file:
    Change the path after 'cd' to the location where you extracted the brk files
  
USAGE:
    brk 30 -> breaktime.png flashing after 30 minutes
    brk    -> breaktime.png flashing after default amount of minutes

You can reset the break timer by calling the brk command again
with the new time set
    Thus first calling 'brk 45' and then 'brk 30',
    will keep the timer to only 30 minutes

brktime--This command outputs the minutes passed
and the minutes till break timer ends
Example output:
    Passed:    15 minutes
    Till break: 15 minutes
