
#Task 1: Create a Dictionary of Student Marks
studict={'rohit':50, 'mohit':60, 'lohit':70, 'katya':55, 'satya':75, 'matya':65, 'patya':80}
nm=str(input("Enter the Student's name: "))
if nm.isalpha():
    if nm in studict:
        print(nm+"'s marks is",studict[nm])
    else:
        print("Student not found.")
else:
    print('Please enter a human name.')


#Task 2: Demonstrate List Slicing
lst1=[]
n=int(input('\nHow much elements you want to enter (minimum 5)?\n'))
print('Enter your {} elements: '.format(n))
for i in range(n):
    lst1.append(int(input()))
print('\nOriginal list (with {} elements): {}'.format(n,lst1))
lst2=lst1[:5]
print('\nExtracted first five elements:{}'.format(lst2))
lst2.reverse()
print('\nReversed extracted elements:{}\n'.format(lst2))