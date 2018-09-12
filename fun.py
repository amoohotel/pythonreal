import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


import calendar;
cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print ("cal")



import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)

import sys
print("JournalDev")
sys.exit(1)
print("Hello")
