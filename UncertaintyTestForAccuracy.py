from uncertainties import *
from uncertainties.umath import *

EPSILON = 0.0000000001  #because uncertainty appearantly has more significant digits in error than regular python's floats? wow. 



#Checks Multiplication
print("\nMultiplication Check!:")

#definition
a       =   9
aErr    = .01
b       =   2
bErr    = 0.1

#conversion to uncertainty type
aFl     = ufloat(a, aErr)
bFl     = ufloat(b, bErr)

#calculation
uncResult = aFl*bFl

result = a*b
desErr = result*((aErr/a)**2 + (bErr/b)**2)**.5

#print statements so humans can make sure its right
print("Result:      {:5.17}".format(uncResult))
print("Expected:    {:5.17}+/-{:5.17}".format(float(result), desErr))

#computerized results for quick veiwing
if(abs(uncResult.n - float(result)) < EPSILON):
    print("Calculation:   Correct!")
else:
    print("Calculation: Incorrect!")


if(abs(uncResult.s - float(desErr)) < EPSILON):
    print("Error:         Correct!")
else:
    print("Error:       Incorrect!")



#Checks Addition
print("\nAddition Check!:")

#definition
a       =   5
aErr    = .01
b       =   9
bErr    = .05

#conversion to uncertainty type
aFl     = ufloat(a, aErr)
bFl     = ufloat(b, bErr)

#calculation
uncResult = aFl+bFl
result = a + b
desErr = ((aErr)**2 + (bErr)**2)**.5

#print statements so humans can make sure its right
print("Result:      {:5.17}".format(uncResult))
print("Expected:    {:5.17}+/-{:5.17}".format(float(result), desErr))

#computerized results for quick veiwing
if(abs(uncResult.n - float(result)) < EPSILON):
    print("Calculation:   Correct!")
else:
    print("Calculation: Incorrect!")


if(abs(uncResult.s - float(desErr)) < EPSILON):
    print("Error:         Correct!")
else:
    print("Error:       Incorrect!")



#Checks functions with sine
print("\nFunction Check!:")

#definition
a       =   radians(30)
aErr    =   radians(.5)
print(a)

#conversion to uncertainty type
aFl     = ufloat(a, aErr)


#calculation
uncResult = sin(2 * aFl)
result = sin(2*a)
desErr = 2 * cos(2 * a) *aErr

#print statements so humans can make sure its right
print("Result:      {:5.17}".format(uncResult))
print("Expected:    {:5.17}+/-{:5.17}".format(float(result), float(desErr)))

#computerized results for quick veiwing
if(abs(uncResult.n - float(result)) < EPSILON):
    print("Calculation:   Correct!")
else:
    print("Calculation: Incorrect!")


if(abs(uncResult.s - float(desErr)) < EPSILON):
    print("Error:         Correct!")
else:
    print("Error:       Incorrect!")

