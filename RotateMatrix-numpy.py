import numpy as np
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
#print(arr.T[:,::-1])
#print('\n')
#print(arr.T[:,::-1].T[:,::-1])
while True:
    try:
        YourInput = int(input("Please input the degree of rotation: "))
        if YourInput%90 == 0 and YourInput != 0:
            break
        print("Oops!  That was not valid degree.  Try again...")
    except ValueError:
        print("Oops!  That was not valid number.  Try again...")

WorkingArray = arr

if YourInput >=0:
    for n in range(abs(int(YourInput/90))):
        WorkingArray = WorkingArray.T[:,::-1]
    print(WorkingArray)

else:
    for n in range(abs(int(YourInput/90))):
        WorkingArray = WorkingArray.T[::-1,:]
    print(WorkingArray)