# ASCII Art of Bad Bunny (Minor Project)

def draw(ch, no):
    char = ""
    index = 0
    while index < no:
        char += ch
        index += 1
    return char


def row1():
    string = ""
    string += draw(" ", 20)
    string += draw("#", 20)
    return string

def row2():
    string = ""
    string += draw(" ", 16)
    string += draw("#", 28)
    return string

def row3():
    string = ""
    string += draw(" ", 14)
    string += draw("#", 32)
    return string

def row4():
    string = ""
    string += draw(" ", 12)
    string += draw("#", 36)
    return string

def row5():
    string = ""
    string += draw(" ", 10)
    string += draw("#", 10)
    string += draw(" ", 6)
    string += draw("#", 10)
    return string

def row6():  # Eyes
    string = ""
    string += draw(" ", 10)
    string += draw("#", 4)
    string += draw(" ", 4)
    string += draw("#", 4)
    return string

def row7():
    string = ""
    string += draw(" ", 12)
    string += draw("#", 16)
    return string

def row8():  # Nose
    string = ""
    string += draw(" ", 14)
    string += draw("#", 8)
    return string

def row9():  # Mouth
    string = ""
    string += draw(" ", 12)
    string += draw("#", 12)
    return string

def row10():
    string = ""
    string += draw(" ", 14)
    string += draw("#", 8)
    return string

def row11():
    string = ""
    string += draw(" ", 16)
    string += draw("#", 4)
    return string


functions = [
    row1, row2, row3, row4, row5,
    row6, row7, row8, row9, row10, row11
]

for func in functions:
    print(func())
