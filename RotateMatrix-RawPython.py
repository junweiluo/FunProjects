OriginalGrid = [[".", ".", ".", ".", ".", "."],
        [".", "0", "0", ".", ".", "."],
        ["0", ".", "0", "0", ".", "."],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", ".", "."],
        [".", "0", "0", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]

while True:
    try:
        YourInput = int(input("Please input the degree of rotation: "))
        if YourInput%90 == 0 and YourInput != 0:
            break
        print("Oops!  That was not valid degree.  Try again...")
    except ValueError:
        print("Oops!  That was not valid number.  Try again...")

WorkingGrid = OriginalGrid

if YourInput >=0:
    Coeff1 = 1
    Coeff2 = 0
else:
    Coeff1 = 0
    Coeff2 = 1

for n in range(abs(int(YourInput/90))):
    StandingGrid = []
    for b in range((len(WorkingGrid[0])-1)*Coeff2, len(WorkingGrid[0])*Coeff1-Coeff2, Coeff1 -Coeff2):
        x = []
        for a in range(Coeff1*(len(WorkingGrid) - 1), -Coeff1 +len(WorkingGrid)*Coeff2, -Coeff1 +Coeff2):
            x.append(WorkingGrid[a][b])
        print(x)
        StandingGrid.append(x)
    WorkingGrid = StandingGrid
    print("\n")