from random import randint
import os

#parameters
try:
    height = int(input("height: "))
except:
    print("unexpected value detected, deafult value loaded")
    height = 9
try:
    length = int(input("length: "))
except:
    print("unexpected value detected, deafult value loaded")
    length = 9
try:
    mines = int(input("mines: "))
except:
    print("unexpected value detected, deafult value loaded")
    mines = length

#global variables
draw = []
info = []

#intitial info generation
for i in range(height*length):
    info.append("*")
    draw.append("*")

#printing grid

def display_grid():
    space = " "
    line = "-"
    if length < 10:
        space = " "
        line = "-"
    elif length < 100:
        line = "--"
        space = "  "
    elif length < 1000:
        line = "---"
        space = "   "
    for i in range(length):
        if i > 9:
            if i < 100:
                space = " "
        print(str(i), end = space)
    print()
    for j in range(length):
        print("-", end = line)
    print()
    for x in range(height):
        for y in range(length):
            if length < 10:
                space = " "
                line = "-"
            else:
                line = "--"
                space = "  "
            print(draw[y+(length*x)], end = space)
        print("|"+str(x))

#placing mines
mem = 0
done = []
while mem != mines:
    mine = randint(0,(length * height)-1)
    if mine in done:
        continue
    else:
        info[mine] = "mine"
        done.append(mine)
        mem += 1

#returns the height of current block
def ItemHeight(item):
    num = 0
    while True:
        if item - length >= 0:
            item -= length
            num += 1
        else:
            break
    return num

#numbering current block
for item in range(len(info)):
    number = 0
    current_height = ItemHeight(item)
    current_length = item - (current_height * length)
    if info[item] != "mine":
        #numbering corners
        if item == 0:
            if info[1] == "mine":
                number += 1
            if info[length] == "mine":
                number += 1
            if info[length+1] == "mine":
                number += 1
        elif item == length-1:
            if info[item-1] == "mine":
                number += 1
            if info[item + length-1] == "mine":
                number += 1
            if info[item + length] == "mine":
                number += 1
        elif item == length*(height-1):
            if info[item - length] == "mine":
                number += 1
            if info[item - length +1] == "mine":
                number += 1
            if info[item+1] == "mine":
                number += 1
        elif item == length*height-1:
            if info[item - length] == "mine":
                number += 1
            if info[item-length-1] == "mine":
                number += 1
            if info[item-1] == "mine":
                number += 1
        #numbering edges
        elif current_length == length-1:
            if info[item-length] == "mine":
                number += 1
            if info[item-length-1] == "mine":
                number += 1
            if info[item-1] == "mine":
                number += 1
            if info[item+length-1] == "mine":
                number += 1
            if info[item+length] == "mine":
                number += 1
        elif current_height == 0:
            if info[item-1] == "mine":
                number += 1
            if info[item+length-1] == "mine":
                number += 1
            if info[item+1] == "mine":
                number += 1
            if info[item+length] == "mine":
                number += 1
            if info[item+length+1] == "mine":
                number += 1
        elif current_length == 0:
            if info[item+1] == "mine":
                number += 1
            if info[item+length+1] == "mine":
                number += 1
            if info[item-length+1] == "mine":
                number += 1
            if info[item+length] == "mine":
                number += 1
            if info[item-length] == "mine":
                number += 1
        elif current_height == height-1:
            if info[item+1] == "mine":
                number += 1
            if info[item-1] == "mine":
                number += 1
            if info[item-length-1] == "mine":
                number += 1
            if info[item-length] == "mine":
                number += 1
            if info[item-length+1] == "mine":
                number += 1
        else:
            if info[item - length-1] == "mine":
                number += 1
            if info[item - length] == "mine":
                number += 1
            if info[item - length+1] == "mine":
                number += 1

            if info[item - 1] == "mine":
                number += 1
            if info[item + 1] == "mine":
                number += 1

            if info[item + length-1] == "mine":
                number += 1
            if info[item + length] == "mine":
                number += 1
            if info[item + length+1] == "mine":
                number += 1
        info[item] = number

#checks and counts zero regions
for item in range(len(info)):
    current_height = ItemHeight(item)
    current_length = item - (current_height * length)
    if info[item] == 0:
        draw[item] = 0
        if item == 0:
            if info[1] != 0:
                draw[1] = info[1]
            if info[length] != 0:
                draw[length] = info[length]
            if info[length+1] != 0:
                draw[length+1] = info[length+1]
        elif item == length-1:
            if info[item-1] != 0:
                draw[item-1] = info[item-1]
            if info[item + length-1] != 0:
                draw[item + length-1] = info[item + length-1]
            if info[item + length] != 0:
                draw[item + length] = info[item + length]
        elif item == length*(height-1):
            if info[item - length] != 0:
                draw[item - length] = info[item - length]
            if info[item - length +1] != 0:
                draw[item - length +1] = info[item - length +1]
            if info[item+1] != 0:
                draw[item+1] = info[item+1]
        elif item == length*height-1:
            if info[item - length] != 0:
                draw[item - length] = info[item - length]
            if info[item-length-1] != 0:
                draw[item-length-1] = info[item-length-1]
            if info[item-1] != 0:
                draw[item-1] = info[item-1]
        #numbering edges
        elif current_length == length-1:
            if info[item-length] != 0:
                draw[item-length] = info[item-length]
            if info[item-length-1] != 0:
                draw[item-length-1] = info[item-length-1]
            if info[item-1] != 0:
                draw[item-1] = info[item-1]
            if info[item+length-1] != 0:
                draw[item+length-1] = info[item+length-1]
            if info[item+length] != 0:
                draw[item+length] = info[item+length]
        elif current_height == 0:
            if info[item-1] != 0:
                draw[item-1] = info[item-1]
            if info[item+length-1] != 0:
                draw[item+length-1] = info[item+length-1]
            if info[item+1] != 0:
                draw[item+1] = info[item+1]
            if info[item+length] != 0:
                draw[item+length] = info[item+length]
            if info[item+length+1] != 0:
                draw[item+length+1] = info[item+length+1]
        elif current_length == 0:
            if info[item+1] != 0:
                draw[item+1] = info[item+1]
            if info[item+length+1] != 0:
                draw[item+length+1] = info[item+length+1]
            if info[item-length+1] != 0:
                draw[item-length+1] = info[item-length+1]
            if info[item+length] != 0:
                draw[item+length] = info[item+length]
            if info[item-length] != 0:
                draw[item-length] = info[item-length]
        elif current_height == height-1:
            if info[item+1] != 0:
                draw[item+1] = info[item+1]
            if info[item-1] != 0:
                draw[item-1] = info[item-1]
            if info[item-length-1] != 0:
                draw[item-length-1] = info[item-length-1]
            if info[item-length] != 0:
                draw[item-length] = info[item-length]
            if info[item-length+1] != 0:
                draw[item-length+1] = info[item-length+1]
        else:
            if info[item - length-1] != 0:
                draw[item - length-1] = info[item - length-1]
            if info[item - length] != 0:
                draw[item - length] = info[item - length]
            if info[item - length+1] != 0:
                draw[item - length+1] = info[item - length+1]

            if info[item - 1] != 0:
                draw[item - 1] = info[item - 1]
            if info[item + 1] != 0:
                draw[item + 1] = info[item + 1]

            if info[item + length-1] != 0:
                draw[item + length-1] = info[item + length-1]
            if info[item + length] != 0:
                draw[item + length] = info[item + length]
            if info[item + length+1] != 0:
                draw[item + length+1] = info[item + length+1]

#action input
temp = 0
for item in range(len(draw)):
    if info[item] == "mine":
        continue
    else:
        temp += 1
def action():
    while True:
        try:
            heigh = int(input("input height coordinate: "))
            if heigh >= height or heigh < 0:
                os.system("cls")
                print("Error: unexpected value\n")
                display_grid()
                continue
            if heigh >= 100:
                quit()
            lengt = int(input("input length coordinate: "))
            if lengt >= length or lengt < 0:
                os.system("cls")
                print("Error: unexpected value\n")
                display_grid()
                continue
            if lengt >= 100:
                quit()
            action = input("input action(dig/flag): ")
            break
        except:
            print("unexpected values entered!")
            continue
    pr = []
    pr.append(heigh)
    pr.append(lengt)
    pr.append(action)
    return(pr)

#action manager
while True:
    os.system('cls')
    display_grid()
    mem = action()
    pos = mem[1] + mem[0] * length
    if info[pos] == draw[pos]:
        continue
    if mem[2] == "dig":
        if info[pos] == "mine":
            while True:
                print("BOOM")
        else:
            draw[pos] = info[pos]
    elif mem[2] == "flag":
        if draw[pos] == "%":
            if info[pos] == "mine":
                while True:
                    print("BOOM")
            else:
                draw[pos] = info[pos]
        else:
            draw[pos] = "%"
    temp2 = 0
    for item in range(len(draw)):
        if info[item] == "mine":
            continue
        elif info[item] == draw[item]:
            temp2 += 1
    if temp2 == temp:
        while True:
            print("WIN")
    temp2 = 0
