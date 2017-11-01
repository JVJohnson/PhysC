README.txt for the Uncertainty test python file
Author: James Johnson

The UncertaintyTestForAccuracy.py file manually calculates the result and error of three calculations using regular python math functions
The file then compares it to the automatic error propagation done by the Uncertainty Python package. 
This file exists to prove that Uncertainty provides accurate and precise enough results to trust in Dr. Whitbeck's Physics C Lab.



---------------------------------------------------------
RUN INSTRUCTIONS

1. -have python 3 installed (3.5.2)
2. -have uncertainty installed for said version
3.a-run this command in a linux terminal"python3 UncertaintyTestForAccuracy.py"
	.b) Otherwise execute the python file however is required for your system. 
4. Program should run and display the output


---------------------------------------------------------
OUTPUT


Multiplication Check!:
Result:      18.000000000000000+/-0.900222194794152
Expected:     18.0+/-0.900222194794152
Calculation:   Correct!
Error:         Correct!

Addition Check!:
Result:      14.000000000000000+/-0.050990195135928
Expected:     14.0+/-0.050990195135927854
Calculation:   Correct!
Error:         Correct!

Function Check!:
0.5235987755982988
Result:      0.86602540378443860+/-0.00872664625997165
Expected:    0.8660254037844386+/-0.0087266462599716495
Calculation:   Correct!
Error:         Correct!
