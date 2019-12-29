# Using numpy Transpose function to solve the problem. 

import numpy as np

# Transform list of list as array
arr = np.array([['.','.','.','.','.','.'],
                ['.','0','0','.','.','.'],
                ['0','*','0','0','.','.'],
                ['0','0','0','0','0','.'],
                ['.','0','0','0','0','0'],
                ['0','0','0','0','0','.'],
                ['0','0','0','0','.','.'],
                ['.','0','0','.','.','.'],
                ['.','.','.','.','.','.']])
print(arr)

# check if input is n times 90 degrees
while True:
    try:
        YourInput = int(input("Please input the degree of rotation: "))
        if YourInput%90 == 0 and YourInput != 0:
            break
        print("Oops!  That was not valid degree.  Try again...")
    except ValueError:
        print("Oops!  That was not valid number.  Try again...")

# assign the original array to as working array
WorkingArray = arr

if YourInput >=0:
    for n in range(abs(int(YourInput/90))):
        # Transpose array and flip
        WorkingArray = WorkingArray.T[:,::-1]
    print(WorkingArray)

else:
    for n in range(abs(int(YourInput/90))):
        # Transpose array and flip
        WorkingArray = WorkingArray.T[::-1,:]
    print(WorkingArray)
