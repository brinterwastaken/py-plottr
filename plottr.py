import numpy as np

def braille(matrix):
    if len(matrix) != 4 or len(matrix[0]) != 2:
        raise ValueError("Matrix must be 4x2")
    
    braille_char = 0
    
    for c in range(2):
        for r in range(3):
            if matrix[r][c] == True:
                braille_char |= 1 << r + 3*c
        if matrix[3][c] == 1:
            braille_char |= 1 << 6+c

    return chr(0x2800+braille_char)

def pointmatrix(func:function, xmin, xmax, ymin, ymax, res):
    def func_satisfied(r,c):
        y,x = ymax - r*res, c*res + xmin
        return y == np.round(func(x)/res)*res

    return np.fromfunction(func_satisfied, (int((ymax-ymin)//res), int((xmax-xmin)//res)), dtype=int)

def display_full(*args):
    points:np.ndarray = pointmatrix(*args)
    for r in points:
        for c in r:
            print("●" if c else ' ', end=" ")
        print()

def display_braille(filename, to_file=False, *args):
    # get 4x2 blocks
    points:np.ndarray = pointmatrix(*args)
    
    blocks:np.ndarray = points.reshape((-1, 4, points.shape[1]//2, 2)).transpose((0,2,1,3))

    string = ""

    for r in blocks:
        for c in r:
            if to_file: string += braille(c)
            else: print(braille(c), end='')
        if to_file: string += '\n'
        else: print()

    if to_file:
        with open(filename, "w") as f:
            f.write(string)
        print("Written output to file: ", filename)

def plot(f:function, xmin=-10, xmax=10, ymin=-10, ymax=10, res=1/32, to_file=False, filename="plot.txt"):
    display_braille(filename, to_file, f, xmin, xmax, ymin, ymax, res)

plot(np.sin, to_file=True, ymin=-2,ymax=2)

