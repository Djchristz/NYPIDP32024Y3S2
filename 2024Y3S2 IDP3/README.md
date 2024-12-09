REV 0.01
Started on the rough code for IR sensing and general variable functions declarations

Rev 0.02
Added motor functions and abit of logic
Splitted the variables from the mainsystem for easier debugging down the line

Rev 0.03 
Somehow broke everything, did not publish.
Cause of code breakage: Attempted to code a method of scanning the recylable using IR by adding a data reading every 0.1 seconds. Somehow managed to break motor logic along the way

Rev 0.04
Fixed Ir scanning logic
Fixed motor logic and cleaned up motor logic
Implemented ultrasonic logic as a button, incomplete.

Rev 0.05
Need to rework the whole file, everything is too nested.
Fixed state machine that was part of ultrasonic logic
Cleaned up IR scanning logic again. This will be a common trend as its abit buggy here and there.

As of right now the whole system would start off one line. Its fine considering what the purpose of this system is but need to try and rework it as all the definitions are utilizing each other
