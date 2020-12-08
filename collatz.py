#Program name: pixelByPixelLineByLine
#Description: Uses the Collatz formula. Regardless of initial value of c0
#will always go to 1.
#Author: Matthew Wilson EC1841586
#Date: 01/04/2020
#Company: Edinburgh College

number = int(input('Enter a number, please:'))

#set steps zero
steps = 0
while number > 1:
    if number % 2 == 0:
        number = number / 2
        print (int(number))
    else:
        number = number * 3 + 1
        print(int(number))
    #Add one to each step within loop for counting and print after final number
    steps += 1
print('Steps required: ', steps)
