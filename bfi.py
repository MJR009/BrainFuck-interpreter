import sys

CELL_COUNT = 30_000
MAX = 256

cells = [0] * CELL_COUNT
index = 0

def Greater_than():
    global index
    index = (index + 1) % CELL_COUNT

def Less_than():
    global index
    index = (index - 1) % CELL_COUNT

def Plus():
    global cells, index
    cells[index] = (cells[index] + 1) % MAX

def Minus():
    global cells, index
    cells[index] = (cells[index] - 1) % MAX

def Period():
    global cells, index
    print(chr(cells[index]), end="")

def Colon():
    global cells, index
    cells[index] = ord(sys.stdin.read(1))

def Left_bracket(c, src):
    global cells, index
    if cells[index] == 0:
        while c != "]":
            c = src.read(1)

def Right_bracket(c, src):
    global cells, index
    if cells[index] != 0:
        while c != "[":
            src.seek(src.tell() - 1)
            c = src.read(1)
            src.seek(src.tell() - 1)

def Interpret(c, src):
    match c:
        case ">":
            Greater_than()
        case "<":
            Less_than()
        case "+":
            Plus()
        case "-":
            Minus()
        case ".":
            Period()
        case ",":
            Colon()
        case "[":
            Left_bracket(c, src)
        case "]":
            Right_bracket(c, src)
        case _:
            pass

with open(sys.argv[1], "r") as src:
    while True:
        c = src.read(1)
        if not c:
            break
        Interpret(c, src)
