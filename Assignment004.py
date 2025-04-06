
#Task 1: Read a File and Handle Errors

try:
    f1=open('sample.txt','r')
    print('\nReading file content:\n',f1.read())
    f1.close()

except FileNotFoundError:
    print("\nError: The file 'sample.txt' was not found.\n")

#Task 2: Write and Append Data to a File

try:
    open('output.txt','w').close()

    f1=open('output.txt','a')
    f1.write(input('\nEnter text to write to the file: '))
    f1.write('\n')
    print('Data successfully written to the output.txt.')
    f1.write(input('\nEnter additional text to append: '))
    print('Data successfully appended.')
    f1.write('\n')
    f1.close()

    f1=open('output.txt','r')
    print('\nFinal content of output.txt:\n',f1.read())
    f1.close()

except FileNotFoundError:
    print("\nError: The file 'output.txt' was not found.\n")