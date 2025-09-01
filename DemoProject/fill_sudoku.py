numbers_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

su=[][]
def fill_in_sudoku(su):
    for i in range(0..9):
        for j in range(0..9):
            su[i][j] = '0'
    return


def fill_in_sudoku_puzzle(su):
    res = input("Do you want to continue?")
    fill_in_sudoku(su)
    while (res='y'):
        i = input("Enter row no")
        j = input("Enter column no")
        val = input("Enter val")
        su[i][j] = val
        res = input("Do you want to continue?")
        

def test_row(su) -> bool:
    for i in range(0..9):
        for j in range(0..8):
            if su[i][j] != '0':
                if su[i][j] == su[i][j+1]
                    return False
    return True


def test_col(su) - > bool:
    for i in range(0..8):
        for j in range(0..8):
            if su[i][j] != '0':
                if su[i][j] == su[i+1][j]
                    return False
    return True

def test_grid(su, i, j) -> bool:
    