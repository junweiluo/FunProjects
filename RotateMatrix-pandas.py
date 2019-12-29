# Using pandas Transpose function to solve the problem. 

import pandas as pd

# Transform list of list as DataFrame
df = pd.DataFrame.from_records([['.','.','.','.','.','.'],
                ['.','0','0','.','.','.'],
                ['0','*','0','0','.','.'],
                ['0','0','0','0','0','.'],
                ['.','0','0','0','0','0'],
                ['0','0','0','0','0','.'],
                ['0','0','0','0','.','.'],
                ['.','0','0','.','.','.'],
                ['.','.','.','.','.','.']])
print(df)

# check if input is n times 90 degrees
while True:
    try:
        YourInput = int(input("Please input the degree of rotation: "))
        if YourInput%90 == 0 and YourInput != 0:
            break
        print("Oops!  That was not valid degree.  Try again...")
    except ValueError:
        print("Oops!  That was not valid number.  Try again...")

# assign the original DataFrame as working DataFrame
Working_df = df

if YourInput >=0:
    for n in range(abs(int(YourInput/90))):
        # Transpose DataFrame and flip
        Working_df = (Working_df.T).iloc[:,::-1]
    print(Working_df)

else:
    for n in range(abs(int(YourInput/90))):
        # Transpose DataFrame and flip
        Working_df = (Working_df.T).iloc[::-1,:]
    print(Working_df)