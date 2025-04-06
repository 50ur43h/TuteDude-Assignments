
#Task 1: Calculate Factorial Using a Function

def fact(x):
    if x<0:
        return 0
    elif x<2:
        return 1
    else:
        return x*(fact(x-1))

x=int(input('\nEnter a number: '))

res=fact(x)

if res==0:
    print('Next time please enter a valid number!\n')
else:
    print('Factorial of',x,'is:',res,'\n')


#Task 2: Using the Math Module for Calculations

import math

num=float(input('\nEnter a number: '))
if num<1:
    print('Please enter any valid number above "0".\n')
else:
    print('Square root:',math.sqrt(num))
    print('Logarithm:',math.log(num))
    print('Sine:',math.sin(num),'\n')