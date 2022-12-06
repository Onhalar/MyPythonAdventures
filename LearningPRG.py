from random import randint
import os
from pathlib import Path
from time import sleep

#global variables
tasks = []
resaults = []
wrongRes = []
CorrectRes = []
wrong = []
done = []
show_right = False
enable_switch = False
name = ""
loaded = False

#loads tasks
def inp():
    global name
    name = input("Enter name for context: ")
    while True:
        os.system("cls")
        task = input("Enter task: ")
        resault = input("Enter resault: ")
        tasks.append(task)
        resaults.append(resault)
        repeat = input("Add another? (y/n): ")
        if repeat != "y":
            break

#picks random task
def pick_task():
    while True:
        task = randint(0, len(tasks)-1)
        if task in done:
            continue
        return task

#picks wheter or not to switch task and resault
def switch_task():
    num = randint(0,1)
    if num == 0:
        return False
    else:
        return True

#displaying tasks
def display_task():
    os.system("cls")
    print(name,"\n")
    id = pick_task()
    switch = switch_task()
    #switched task and resault
    if switch and enable_switch:
        print("Task:",resaults[id])
        resault = input("Resault: ")
        if resault.lower() != tasks[id].lower():
            if id in wrong:
                wrongRes[wrong.index(id)] += ", " + resault
            else: 
                wrongRes.append(resault)
                wrong.append(id)
                CorrectRes.append(tasks[id])
            if show_right:
                    print("Correct resault:", tasks[id], "|", "Your resault:", resault)
                    sleep(len(resaults[id]))
        else:
            done.append(id)
    #normal rask ans resault
    else:
        print("Task:",tasks[id])
        resault = input("Resault: ")
        if resault.lower() != resaults[id].lower():
            if id in wrong:
                wrongRes[wrong.index(id)] += ", " + resault
            else: 
                wrongRes.append(resault)
                wrong.append(id)
                CorrectRes.append(resaults[id])
            if show_right:
                    print("Correct resault:", resaults[id], "|", "Your resault:", resault)
                    sleep(len(resaults[id]))
        else:
            done.append(id)

#saving function
def save():
    global name
    save = name + ";"
    for item in range(len(tasks)):
        save += tasks[item] + ";" + resaults[item] + ";"
    save += str(show_right) + ";" + str(enable_switch)
    file = open("save.txt", "w")
    file.write(save)

#loading function
def loa():
    global enable_switch
    global loaded
    global name
    global show_right
    loaded = True
    text = open("save.txt", "r").read()
    temp = text.split(";")
    name = temp[0]
    temp.pop(0)
    for item in range(len(temp)):
        if item == len(temp) - 1:
            enable_switch = bool(temp[item])
        if item == len(temp) -2:
            show_right = bool(temp[item])
        elif item % 2 != 0:
            resaults.append(temp[item])
        elif item % 2 == 0:
            tasks.append(temp[item])

#program manager
check = True
while True:
    if Path("save.txt").exists() and check:
        load = input("Save file detected!\nDo you want to load from there? (y/n): ")
        if load == "y":
            loa()
            check = False
            continue
    if check:
        os.system("cls")
        inp()
        #asks if if you want to display right resaults
        show = input("Show right resaults? (y/n): ")
        if show == "y":
            show_right = True
        #asks if you want to switch tasks and resaults
        switch = input("Switch tasks? (y/n): ")
        if switch == "y":
            enable_switch = True
        #asks if you want to just save
        savetasks = input("Just save? (y/n): ")
        if savetasks == "y":
            save()
            break
        check = False
    if len(done) != len(tasks):
        print(name)
        display_task()
    else:
        os.system("cls")
        print("Wrong resaults:")
        for i in range(len(wrong)):
            print("Correct resault:",CorrectRes[i], "|", "Your resault:", wrongRes[i])
        if loaded == False:
            savetasks = input("Do you want to save these tasks? (y/n):")
            if savetasks == "y":
                save()
        repeat = input("Do you want to repeat? (y/n): ")
        if repeat == "y":
            done.clear()
            wrong.clear()
            wrongRes.clear()
        else:
            break
