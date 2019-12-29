"""
Author: Junwei Luo

Collatz probelm: any positive integer, if is even, then divide by two; if odd, times 3 plus 1.

Continue doing last step, eventually any positive integer will get to 1.
"""

# define function for collatz
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

# ask for an positive input; if not a positive input, ask again.
while True:
    input1 = input("Please input an positive integer: ")
    try:
        intInput = int(input1)
        if intInput > 0:
            break
        else:
            print("Not an positive integer.  Please input again: ")
    except:
        print("Not an integer.  Please input again: ")

# print result of collatz transformation and collatz again until 1.
while True:
    print(intInput)
    if collatz(intInput) == 1:
        print(collatz(intInput))
        break
    else:
        intInput = collatz(intInput)