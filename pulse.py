########################################
# PULSE
########################################

# Libraries
import os
import time
import math


# experiments | experiments that are being tested
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


# commands | list of commands
cmds = (
    "print: (txt)                                               | Prints a text to the Terminal"
    "\n"
    "pulse.logo                                               | Prints the logo for Pulse in the Terminal"
    "\n"
    "pulse.terminate                                          | Kills the program"
    "\n"
    "pause: (seconds)                                         | Sets a timer for X amount of seconds"
    "\n"
    "pulse.time                                               | Prints the time into the Terminal"
    "\n"
    "pulse                                                    | Pulse by MaxChip & Talleeenos69 2022 - 2022"
    "\n"
    "X + Y                                                    | Adds 2 numbers together"
    "\n"
    "X - Y                                                    | Subtracts 2 numbers from each other"
    "\n"
    "X * Y                                                    | Multiplies 2 numbers together"
    "\n"
    "X / Y                                                    | Divides 2 numbers from each other"
    "\n"
    "X $ Y                                                    | Mods 2 numbers from each other"
    "\n"
    "X ^ Y                                                    | Puts a number to the exponent to another number"
    "\n"
    "sqrt: (num)                                              | Puts the number you put in to the square root"
    "\n"
    "pi: (num)                                                | Puts the number you put in to the square root"
    "\n"
    "sin: (num)                                               | Puts the number you put in to the square root"
    "\n"
    "cos: (num)                                               | Puts the number you put in to the square root"
    "\n"
    "tan: (num)                                               | Puts the number you put in to the square root"
    "\n"
    "file: (file.filetype) // N> (e, w, r, c) // (w) > (text) | Creates / writes, deletes, reads a file"
    "\n"
    "pulse.experiments                                        | Shows a list of experiments that are available"
)
# experiments | list of experiments
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
)


# logo
def Logo():
    print("""
    ..........                                                        ..............
    **************                   #@#                              ..............
    ***@@@@@@@@@@                    #@#                               .............
    **,@@...... @@    @@       @@    #@#     #@@@@@@%.    @@@@@@@@ .................
    **,@@.......@@    @@       @@    #@#   #@#     ...  @@        @@    ............
    **,@@@@@@@@@@     @@       @@    #@#     #@#   ...  @@@@@@@@@@@.................
    **,@@.......      @@       @@    #@#      ..#@#..   @@..........................
    **,@@.......      @@       @@    #@#   ........#@#...#@.........................
    **,@@.......       @@@@@@@@@     #@#...@@@@@@@@@....  #@@@@@@@#.................
    **,,,,.....                     ....................,,,,,,,,,,,,,,,,,,,,,,,,,,,.
    **,,,,......                 .................,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    **,,,.......               ...............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    *,,,,.......             ..............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
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
                      ...........,,,,,,,,,,,,,,,,,,,,,,| MaxChip101 & Talleeenos69 |

    """)


# Tips
print('''
Type "pulse.cmds" for a list of commands.
''')

while True:

    # input
    enit = input(" : ")

    # Commands

    # null
    if enit == "null":
        pass
    # logo
    elif enit == "pulse.logo":
        Logo()

    # print
    elif enit[0:7] == "print: ":
        print(enit[7:])

    # time
    elif enit == "pulse.time":
        print(time.localtime())

    # experiments
    elif enit == "pulse.experiments":
        print(experiments)

    # experiment1
    elif enit == "pulse.experiment1":
        exp1()

    # experiment2
    elif enit == "pulse.experiment2":
        exp2()

    # experiment3
    elif enit == "pulse.experiment3":
        exp3()

    # experiment4
    elif enit == "pulse.experiment4":
        exp4()

    # experiment5
    elif enit == "pulse.experiment5":
        exp5()

    # file editor
    elif enit[0:6] == "file: ":
        a = enit[6:]
        c = input(" N> ")
        # Remove files
        if c == "e":
            print("ARE YOU SURE YOU WANT TO ERASE THIS FILE.\n Y / N")
            o = input(" > ")
            if o == "y":
                os.remove(a)
            else:
                pass
        # Write to Files
        elif c == "w":
            f = open(a, "w")
            b = input(" > ")
            f.write(b + "\n")
        elif c == "r":
            f = open(a, "r")
            d = f.read()
            print(d)
        elif c == "c":
            f.close()
    # end of file editor

    # terminate
    elif enit == "pulse.terminate":
        exit(0)

    # pulse
    elif enit == "pulse":
        print("Pulse by MaxChip and Talleeenos69 2022 - 2022")

    # timer
    elif enit[0:7] == "pause: ":
        time.sleep(int(enit[7:]))

    # addition
    elif "+" in enit:
        a = enit.find("+")
        b = enit[:a - 1]
        c = enit[a + 1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b + c
        print(round(d, 3))

    # subtraction
    elif "-" in enit:
        a = enit.find("-")
        b = enit[:a - 1]
        c = enit[a + 1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b - c
        print(round(d, 3))

    # multiplication
    elif "*" in enit:
        a = enit.find("*")
        b = enit[:a - 1]
        c = enit[a + 1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b * c
        print(round(d, 3))

    # devision
    elif "/" in enit:
        a = enit.find("/")
        b = enit[:a - 1]
        c = enit[a + 1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b / c
        print(round(d, 3))

    # modulus
    elif "$" in enit:
        a = enit.find("$")
        b = enit[:a - 1]
        c = enit[a + 1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b % c
        print(round(d, 3))

    # exponents
    elif "^" in enit:
        a = enit.find("^")
        b = enit[:a - 1]
        c = enit[a + 1:]
        if "." in enit:
            b = float(b)
            c = float(c)
        else:
            b = int(b)
            c = int(c)
        d = b ** c
        print(round(d, 3))

    # square root
    elif enit[0:6] == "sqrt: ":
        a = enit.find("sqrt: ")
        b = enit[a + 6:]
        if "." in enit:
            b = float(b)
        else:
            b = int(b)
        d = math.sqrt(b)
        print(round(d, 3))

    # cmds
    elif enit == "pulse.cmds":
        print(cmds)
    # non-existent command | if the input does not have a existing command then it will print the non existant command
    else:
        print('"' + enit + '"' + " is not a valid command")

