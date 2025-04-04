
#Task 1: Check if a Number is Even or Odd

num=int(input('\nEnter a number: '))
if (num%2==0):
    print(num,'is an Even Number')
else:
    print(num,'is an Odd Number')
print('\n')


#Task 2: Sum of Integers from 1 to 50 Using a Loop

sum=0
for i in range(1,51):
    sum+=i
print('\nThe sum of numbers from 1 to 50 is:',sum,'\n')