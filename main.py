# -------------------------
# PULSE
# -------------------------

# Libraries
import os
import time
import math
import platform

# External Libraries
import requests  # terminal > pip install requests

# Variable table
Var_Table = []

# Define System-Wide Variables ---------------------------------------
Command_Line_Text = ":"
Command_Choice_Text = "C>"
Command_Write_Text = "W>"

clearScreenTimes = 200

# Define Functions ---------------------------------------------------

# Vowel Counter
def getStringInfo(userIn):
    vowelCount = 0
    consonants = 0
    spaceCount = userIn.count(" ")
    vowelCount += userIn.count("a")
    vowelCount += userIn.count("e")
    vowelCount += userIn.count("i")
    vowelCount += userIn.count("o")
    vowelCount += userIn.count("u")
    consonants = int(len(userIn) - vowelCount)
    print("Length : " + str(len(userIn)) + " | Vowels: " + str(vowelCount) + " | Consonants: " + str(
        consonants) + " | Spaces : " + str(spaceCount) + " | Words : " + str(spaceCount + 2))


# clear screen
def clearScreen(clearScreenNum):
    while clearScreenNum > 1:
        clearScreenNum -= 1
        print("\n")


# commands | list of commands
cmds = (
    "print: (txt) ------------------------------------------- | Prints a text to the Terminal"
    "\n"
    "print-var: (var num) ----------------------------------- | Prints a variable in the variable list"
    "\n"
    "pulse.logo --------------------------------------------- | Prints the logo for Pulse in the Terminal"
    "\n"
    "pulse.terminate ---------------------------------------- | Kills the program"
    "\n"
    "pause: (seconds) --------------------------------------- | Sets a timer for X amount of seconds"
    "\n"
    "pulse.time --------------------------------------------- | Prints the time into the Terminal"
    "\n"
    "pulse -------------------------------------------------- | Pulse by MaxChip & Talleeenos69 2022 - 2023"
    "\n"
    "X + Y -------------------------------------------------- | Adds 2 numbers together"
    "\n"
    "X - Y -------------------------------------------------- | Subtracts 2 numbers from each other"
    "\n"
    "X * Y -------------------------------------------------- | Multiplies 2 numbers together"
    "\n"
    "X / Y -------------------------------------------------- | Divides 2 numbers from each other"
    "\n"
    "X % Y -------------------------------------------------- | Mods 2 numbers from each other"
    "\n"
    "X ^ Y -------------------------------------------------- | Puts a number to the exponent to another number"
    "\n"
    "sqrt: (num) -------------------------------------------- | Puts the number you put in to the square root"
    "\n"
    "pi: (num) ---------------------------------------------- | Puts the number you put in to pi"
    "\n"
    "sin: (num) --------------------------------------------- | Puts the number you put in to sine"
    "\n"
    "cos: (num) --------------------------------------------- | Puts the number you put in to cosine"
    "\n"
    "tan: (num) --------------------------------------------- | Puts the number you put in to tangent"
    "\n"
    "(var type (str, int, float)) (var num) = (var val) ----- | Creates a variable number to a specific value"
    "\n"
    "(var num) = (var val) ---------------------------------- | Sets a variable number to a specific value"
    "\n"
    "file: (file.filetype) ---------------------------------- | Creates / writes, deletes, reads a file"
    "\n"
    "vars --------------------------------------------------- | Prints all variables in a list"
    "\n"
    "pulse.code --------------------------------------------- | Prints the code of pulse into the terminal"
    "\n"
    "http: (https://web.domain/) ---------------------------- | Does a lot of things with website html and requests"
    "\n"
    "string-info: (string) ---------------------------------- | Counts the amount of vowels in a string"
    "\n"
    "pulse.clear -------------------------------------------- | Clears the screen"
    "\n"
    "pulse.settings ----------------------------------------- | Shows the settings"
)

# logo
def Logo():
    print("""         
    **************                   #@#                              ..............
    ***@@@@@@@@@@                    #@#                               .............
    **,@@...... @@    @@       @@    #@#     #@@@@@@#.    @@@@@@@@ .................
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

    # In loop variables
    Command_Line_Text_Fix = " " + Command_Line_Text + " "
    Command_Choice_Text_Fix = " " + Command_Choice_Text + " "
    Command_Write_Text_Fix = " " + Command_Write_Text + " "

    # input
    CommandLine = input(Command_Line_Text_Fix)

    # Commands

    # null

    if CommandLine == "":
        pass

    elif "null" in CommandLine:
        pass

    # logo
    elif "pulse.logo" in CommandLine:
        Logo()

    # code
    elif "pulse.code" in CommandLine:
        with open("main.py", "r") as f:
            pulse_code = f.read()
            print(pulse_code)

    # variable editing/adding
    elif "=" in CommandLine:
        function = CommandLine.find("=")
        variable = CommandLine[:function - 1]
        value = CommandLine[function + 1:]

        if "int" in variable:
            value = int(value)
            Var_Table.append(value)

        elif "float" in variable:
            value = float(value)
            Var_Table.append(value)

        elif "str" in variable:
            value = str(value)
            Var_Table.append(value)

        else:
            Var_Table[int(variable)] = value

    # variables
    elif "vars" in CommandLine:
        print(Var_Table)

    # print variable
    elif "print-var:" in CommandLine:
        function = CommandLine.find(":")
        variable = CommandLine[function + 1:]
        print(Var_Table[int(variable)])

    # print
    elif "print:" in CommandLine:
        function = CommandLine.find(":")
        print(CommandLine[function + 1:])

    # time
    elif "pulse.time" in CommandLine:
        print(time.localtime())

    # settings | Allows user to change settings in pulse
    elif "pulse.settings" in CommandLine:
        print("Command_Text | Clear_Screen_Lines", "\n")
        CommandChoice = input(Command_Choice_Text_Fix)

        # Command texts settings
        if "command_text" in CommandChoice.lower():
            print("Command_Line | Command_Choice | Command_Write ", "\n")

            CommandChoice = input(Command_Choice_Text_Fix)

            if "command_line" in CommandChoice.lower():
                print("Input the text of the command line:", "\n")

                CommandWrite = input(Command_Write_Text_Fix)
                Command_Line_Text = CommandWrite

            elif "command_choice" in CommandChoice.lower():
                print("Input the text of the choice line:", "\n")

                CommandWrite = input(Command_Write_Text_Fix)
                Command_Choice_Text = CommandWrite

            elif "command_write" in CommandChoice.lower():
                print("Input the text of the write line:", "\n")

                CommandWrite = input(Command_Write_Text_Fix)
                Command_Write_Text = CommandWrite

        elif "clear_screen_lines" in CommandChoice.lower():
            print("Input amount of lines when the screen gets cleared:", "\n")

            CommandWrite = input(Command_Write_Text_Fix)
            clearScreenTimes = CommandWrite

    # file editor
    elif "file:" in CommandLine:
        print("Write | Read | Erase")

        function = CommandLine.find(":")
        file = CommandLine[function + 1:]
        CommandChoice = input(Command_Choice_Text_Fix)

        # Remove files
        if "erase" in CommandChoice.lower():
            os.remove(file)

        # Write to Files
        elif "write" in CommandChoice.lower():
            with open(file, "w") as f:
                CommandWrite = input(Command_Write_Text_Fix)
                f.write(CommandWrite + "\n")

        # Read Files
        elif "read" in CommandChoice.lower():
            f = open(file, "r")
            d = f.read()
            print(d)

    # http requests
    elif "http:" in CommandLine:
        print("Html | Status")

        function = CommandLine.find(":")
        website = CommandLine[function + 1:]
        web_data = requests.get(website)
        CommandChoice = input(Command_Choice_Text_Fix)

        # gets website html data
        if "html" in CommandChoice.lower():
            print(web_data.text)
            print(web_data)

        elif "status" in CommandChoice.lower():
            print(web_data.ok)
            print(web_data)

    # terminate
    elif "pulse.terminate" in CommandLine:
        exit(0)

    # pulse
    elif CommandLine == "pulse":
        print("Pulse by MaxChip and Talleeenos69 2022 - 2023")

    # timer
    elif "pause:" in CommandLine:
        function = CommandLine.find(":")
        time.sleep(int(CommandLine[function + 1:]))

    # vowel counter
    elif "string-info:" in CommandLine:
        function = CommandLine.find(":")
        string = CommandLine[function + 1:]
        getStringInfo(string)

    # clear screen
    elif "pulse.clear" in CommandLine:
        clearScreen(int(clearScreenTimes))

    # addition
    elif "+" in CommandLine:
        function = CommandLine.find("+")
        value_1 = CommandLine[:function - 1]
        value_2 = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value_1 = float(value_1)
            value_2 = float(value_2)

        else:
            value_1 = int(value_1)
            value_2 = int(value_2)

        result = value_1 * value_2
        print(round(result, 3))

    # subtraction
    elif "-" in CommandLine:
        function = CommandLine.find("-")
        value_1 = CommandLine[:function - 1]
        value_2 = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value_1 = float(value_1)
            value_2 = float(value_2)

        else:
            value_1 = int(value_1)
            value_2 = int(value_2)

        result = value_1 - value_2
        print(round(result, 3))

    # multiplication
    elif "*" in CommandLine:
        function = CommandLine.find("*")
        value_1 = CommandLine[:function - 1]
        value_2 = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value_1 = float(value_1)
            value_2 = float(value_2)

        else:
            value_1 = int(value_1)
            value_2 = int(value_2)

        result = value_1 * value_2
        print(round(result, 3))

    # division
    elif "/" in CommandLine:
        function = CommandLine.find("/")
        value_1 = CommandLine[:function - 1]
        value_2 = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value_1 = float(value_1)
            value_2 = float(value_2)

        else:
            value_1 = int(value_1)
            value_2 = int(value_2)

        result = value_1 / value_2
        print(round(result, 3))

    # modulus
    elif "%" in CommandLine:
        function = CommandLine.find("%")
        value_1 = CommandLine[:function - 1]
        value_2 = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value_1 = float(value_1)
            value_2 = float(value_2)

        else:
            value_1 = int(value_1)
            value_2 = int(value_2)

        result = value_1 % value_2
        print(round(result, 3))

    # exponents
    elif "^" in CommandLine:
        function = CommandLine.find("^")
        value_1 = CommandLine[:function - 1]
        value_2 = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value_1 = float(value_1)
            value_2 = float(value_2)

        else:
            value_1 = int(value_1)
            value_2 = int(value_2)

        result = value_1 ** value_2
        print(round(result, 3))

    # square root
    elif "sqrt:" in CommandLine:
        function = CommandLine.find(":")
        value = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value = float(value)

        else:
            value = int(value)

        result = math.sqrt(value)
        print(round(result, 3))

    # pi
    elif "pi:" in CommandLine:
        function = CommandLine.find(":")
        value = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value = float(value)

        else:
            value = int(value)

        result = math.pi * value
        print(round(result, 3))

    # sine
    elif "sin:" in CommandLine:
        function = CommandLine.find(":")
        value = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value = float(value)

        else:
            value = int(value)

        result = math.sin(value)
        print(round(result, 3))

    # cosine
    elif "cos:" in CommandLine:
        function = CommandLine.find(":")
        value = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value = float(value)

        else:
            value = int(value)

        result = math.cos(value)
        print(round(result, 3))

    # tangent
    elif "tan:" in CommandLine:
        function = CommandLine.find(":")
        value = CommandLine[function + 1:]

        # Checks if there is a decimal
        if "." in CommandLine:
            value = float(value)

        else:
            value = int(value)

        result = math.tan(value)
        print(round(result, 3))

    # cmds
    elif "pulse.cmds" in CommandLine:
        print(cmds)
    
    # Check Operating System
    elif "osinfo" in CommandLine:
        os_name = platform.system()
        print(os_name)

    # non-existent command | if the input does not have an existing command then it will print the non-existent
    # command as an error
    else:
        print('"', CommandLine, '"', "is not a valid command. Type 'pulse.cmds' for a list of commands")
