from systemvars import *

ircallibration()

if irsens >= 10:
    m1f()
    if recyclable == 1: #Need base off Rain's code, change recyclable to whatever he has to detect if object present
        m1s()
        #Rain's code to detect stuff comes here
        #Either that or just put if done == 1 then run
        m1f()

