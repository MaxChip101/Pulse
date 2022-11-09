########################################
# PULSE
########################################

# Libraries
import os
import time
import math
import requests  # terminal > pip install requests


def isnumber(string):
    return any(char.isdigit() for char in string)


# Variable table
var = []


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
    "print: (txt)                                             | Prints a text to the Terminal"
    "\n"
    "printvar: (varn num)                                     | Prints a variable in the variable list"
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
    "pi: (num)                                                | Puts the number you put in to pi"
    "\n"
    "sin: (num)                                               | Puts the number you put in to sine"
    "\n"
    "cos: (num)                                               | Puts the number you put in to cosine"
    "\n"
    "tan: (num)                                               | Puts the number you put in to tangent"
    "\n"
    "(var num) = (var val)                                    | Sets / creates a variable number to a specific value"
    "\n"
    "file: (file.filetype) // N> (e, w, r) // (w) > (text)    | Creates / writes, deletes, reads a file"
    "\n"
    "pulse.variables                                          | Prints all variables in a list"
    "\n"
    "pulse.experiments                                        | Shows a list of experiments that are available"
    "\n"
    "pulse.code                                               | Prints the code of pulse into the terminal"
    "\n"
    "http: {https://web.domain/} // N> (html, status)         | Does a lot of things with website html and requests"
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
    **************                   #@#                              ..............
    ***@@@@@@@@@@                    #@#                               .............
    **,@@...... @@    @@       @@    #@#     #@@@@@@%.    @@@@@@@@ .................
    **,@@.......@@    @@       @@    #@#   #@#     ...  @@        @@    ............
    **,@@@@@@@@@@     @@       @@    #@#     #@#   ...  @@@@@@@@@@@.................
    **,@@.......      @@       @@    #@#      ..#@#..   @@..........................
    **,@@.......      @@       @@    #@#   ........#@#...#@.........................
    **,@@.......       @@@@@@@@@     #@#...@@@@@@@@@....  #@@@@@@@#.................
    **,,,,.....                     ....................,,,,,,,,,,,,,,,,,,,,,,,,,,,,
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
    ...             ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ..             ...........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    .              ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
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

    # code
    elif enit == "pulse.code":
        f = open("pulse.py", "r")
        d = f.read()
        print(d)

    # variable editing/adding
    elif "=" in enit:
        a = enit.find("=")
        b = enit[:a - 1]
        c = enit[a + 2:]
        if isnumber(c):
            if "." in c:
                c = float(c)
            else:
                c = int(c)
        else:
            c = str(c)
        if var.__contains__(b):
            var[int(b)] = c
        else:
            var.append(c)

    # variables
    elif enit == "pulse.variables":
        print(var)

    # print variable
    elif enit[0:10] == "printvar: ":
        a = enit.find(":")
        b = enit[a + 1:]
        print(var[int(b)])

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
            os.remove(a)

        # Write to Files
        elif c == "w":
            f = open(a, "w")
            b = input(" > ")
            f.write(b + "\n")
        # Read Files
        elif c == "r":
            f = open(a, "r")
            d = f.read()
            print(d)
    # end of file editor

    # http requests
    elif enit[0:6] == "http: ":
        a = enit[6:]
        r = requests.get(a)
        c = input(" N> ")
        # gets website html data
        if c == "html":
            print(r.text)
            print(r)
        elif c == "status":
            print(r.ok)
            print(r)

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

    # division
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

    # pi
    elif enit[0:4] == "pi: ":
        a = enit.find("pi: ")
        b = enit[a + 4:]
        if "." in enit:
            b = float(b)
        else:
            b = int(b)
        d = math.pi(b)
        print(round(d, 3))

    # sine
    elif enit[0:5] == "sin: ":
        a = enit.find("sin: ")
        b = enit[a + 5:]
        if "." in enit:
            b = float(b)
        else:
            b = int(b)
        d = math.sin(b)
        print(round(d, 3))

    # cosine
    elif enit[0:5] == "cos: ":
        a = enit.find("cos: ")
        b = enit[a + 5:]
        if "." in enit:
            b = float(b)
        else:
            b = int(b)
        d = math.cos(b)
        print(round(d, 3))

    # tangent
    elif enit[0:5] == "tan: ":
        a = enit.find("tan: ")
        b = enit[a + 5:]
        if "." in enit:
            b = float(b)
        else:
            b = int(b)
        d = math.tan(b)
        print(round(d, 3))

    # cmds
    elif enit == "pulse.cmds":
        print(cmds)
    # non-existent command | if the input does not have an existing command then it will print the non-existent command as an error
    else:
        print('"' + enit + '"' + " is not a valid command")
