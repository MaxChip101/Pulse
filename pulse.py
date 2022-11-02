########################################
# PULSE 
########################################
#pycharm test
#Libraries
import os
import time

#Data

#Functions

#variable saving testing
global a1
global b1
global c1
global d1
global e1

#variable saving | PROG : saves a variable name and variable value together and returns it
def savevar(n, v):
    a = str(v)
    b = n + " ," + v
    return b

#experiments | experiments that are being tested
def exp1():
    pass

def exp2():
    pass

def exp3():
    pass

def exp4():
    pass

def exp5():
    pass

#commands | list of commands
cmds = (
    "print: txt                                            | Prints a text to the Terminal"
    "\n"
    "printvar: (var)                                       | Prints a variable to the Terminal"
    "\n"
    "pulse.logo                                            | Prints the logo for Pulse in the Terminal"
    "\n"
    "pulse.terminate                                       | Kills the program"
    "\n"
    "time: (seconds)                                       | Sets a timer for X amount of seconds" # - in dev when var gets fully made
    "\n"
    "pulse                                                 | Pulse by MaxChip & Talleeenos69 2022 - 2022"
    "\n"
    "X + Y                                                 | Adds 2 numbers together" # -
    "\n"
    "X - Y                                                 | Subtracts 2 numbers from each other" # -
    "\n"
    "X * Y                                                 | Multiplies 2 numbers together" # -
    "\n"
    "X / Y                                                 | Divides 2 numbers from each other" # -
    "\n"
    "N = V                                                 | Creates a variable with a value in the pulse instance" #dev
    "\n"
    "file: (file.filetype) // N> (e, w, r) // (w) > (text) | Creates / writes, deletes, reads a file"
    "\n"
    "pulse.experiments                                     | Shows a list of experiments that are available"
)
#experiments | list of experiments 
experiments = (
    "pulse.experiment1 | Experiment1 has no value"
    "\n"
    "pulse.experiment2 | Experiment2 has no value"
    "\n"
    "pulse.experiment3 | Experiment3 has no value"
    "\n"
    "pulse.experiment4 | Experiment4 has no value"
    "\n"
    "pulse.experiment5 | Experiment5 has no value"
    "\n"
    "More experiments coming soon!"
)

#logo
def Logo():
    print("""
    ,,,,.....                                                        .............,,
    ,,,*/****,.                      (@(                              ..............
    ,,,@@(..../@@@                   (@(                               .............
    *,,@@#..... (@@  ,@@       @@    (@(     #@@@@@@%      %@@@@@%  ................
    *,,@@#......@@/  ,@@       @@    #@#   (@#      ..   @@.     /@&    ............
    **,@@@@@@@@@#    ,@@       @@    #@#   ,@@@(,.   ...@@@@@@@@@@@@................
    **,@@#......     ,@@       @@    #@#       .*#@@@*..@@,.........................
    **,@@#......      @@      /@@    #@#   *.......#@#...@@/.......*................
    **,@@#......       %@@@@@, @@    #@#...*@@@@@@@&.......&@@@@@@@(................
    *,,,,,.....                     ....................,,,,,,,,,,,,,,,,,,,,,,,,,,,.
    *,,,,,......                 .................,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    *,,,,.......               ...............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,.......             ..............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,.......            .............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,.......            ............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,.......          ............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,........          ............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    .......           ...........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ......           ...........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    .....            ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
      .             ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                   ...........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                   ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                   ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                   ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                   ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                   ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                   ...........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                    ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                    ...........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                     ...........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                      ...........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    """)
# Tips
print('''
Type "pulse.cmds" for a list of commands.
''')

while True:

    #input
    enit = input(" : ")

    #Commands

    #logo
    if enit == "pulse.logo":
        Logo()
    
    #print
    elif enit[0:7] == "print: ":
        print(enit[7:])

    #printvar
    elif enit[0:10] == "printvar: ":
        q = enit.find(":")
        #print([10:])

    #experiments
    elif enit == "pulse.experiments":
        print(experiments)

    #experiment1
    elif enit == "pulse.experiment1":
        exp1()

    #experiment2
    elif enit == "pulse.experiment2":
        exp2()

    #experiment3
    elif enit == "pulse.experiment3":
        exp3()

    #experiment4
    elif enit == "pulse.experiment4":
        exp4()

    #experiment5
    elif enit == "pulse.experiment5":
        exp5()

    #file editor
    elif enit[0:6] == "file: ":
        a = enit[6:]
        c = input(" N> ")

        if c == "e":
            print("ARE YOU SURE YOU WANT TO ERASE THIS FILE.\n Y / N")
            o = input(" > ")
            if o == "y":
                os.remove(a)
            else:
                pass
        elif c == "w":            
            f = open(a, "w")
            b = input(" > ")
            f.write(b + "\n")
        elif c == "r":
            f = open(a, "r")
            d = f.read()
            print(d)

        f.close()
        

    #terminate
    elif enit == "pulse.terminate":
        exit(0)

    #pulse
    elif enit == "pulse":
        print("Pulse by MaxChip and Talleeenos69 2022 - 2022")

    #timer
    elif enit[0:6] == "time: ":
        time.sleep(int(enit[6:]))

    #variables
    elif "=" in enit:
        s = enit.find("=")
        n = enit[:s-1]
        v = enit[s+1:]

        if "+" in v:
            a = v.find("+")
            b = v[:a-1]
            c = v[a+1:]
            global x 
            if "." in v:
                b = float(b)
                c = float(c)
            else:
                b = int(b)
                c = int(c)
            d = b + c
            savevar(n,d)

        #detects if the variable has a math function and gets the result and saves it
        if "-" in v:
            a = v.find("-")
            b = v[:a-1]
            c = v[a+1:]
            if "." in v:
                b = float(b)
                c = float(c)
            else:
                b = int(b)
                c = int(c)
            d = b - c
            savevar(n,d)

        if "*" in v:
            a = v.find("*")
            b = v[:a-1]
            c = v[a+1:]
            if "." in v:
                b = float(b)
                c = float(c)
            else:
                b = int(b)
                c = int(c)
            d = b * c
            savevar(n,d)

        if "/" in v:
            a = v.find("/")
            b = v[:a-1]
            c = v[a+1:]
            if "." in v:
                b = float(b)
                c = float(c)
            else:
                b = int(b)
                c = int(c)
            d = b / c
            savevar(n,d)

        if "%" in v:
            a = v.find("%")
            b = v[:a-1]
            c = v[a+1:]
            if "." in v:
                b = float(b)
                c = float(c)
            else:
                b = int(b)
                c = int(c)
            d = b % c
            savevar(n,d)       
        else:
            #if the variable does not have a math function then it will just save it
            savevar(n,v)
            q = savevar(n,v)
            print(q)
    
    #addition
    elif "+" in enit:
        a = enit.find("+")
        b = enit[:a-1]
        c = enit[a+1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b + c
        print(round(d, 3))

    #subtraction
    elif "-" in enit:
        a = enit.find("-")
        b = enit[:a-1]
        c = enit[a+1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b - c
        print(round(d, 3))

    #multiplication
    elif "*" in enit:
        a = enit.find("*")
        b = enit[:a-1]
        c = enit[a+1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b * c
        print(round(d, 3))

    #devision
    elif "/" in enit:
        a = enit.find("/")
        b = enit[:a-1]
        c = enit[a+1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b / c
        print(round(d, 3))

    #modulus
    elif "%" in enit:
        a = enit.find("%")
        b = enit[:a-1]
        c = enit[a+1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b % c
        print(round(d, 3))
    
    #cmds
    elif enit == "pulse.cmds":
        print(cmds)
    # non-existant command | if the input does not have a existing command then it will print the non existant command
    else:
        print('"' + enit + '"' + " is not a valid command")
