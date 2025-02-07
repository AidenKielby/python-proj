
def findInt(input: str, numberOfInts: int):
    outputs = []
    # list of base 10 integers and operator (negative only)
    intL = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']

    string = list(input)
    while " " in string:
        string.remove(" ")

    currentInt = []
    for index in range(len(string) + 1):
        # if not done with list
        if index < len(string):
            character = string[index]
            # if the character is an integer, and it isn't an exponent...
            if character in intL and string[index-1] != "^":
                # add it to the current integer list
                currentInt.append(character)
            else:
                # otherwise, if there is a current integer, add that to outputs and reset current integer
                if len(currentInt) > 0:
                    currentInt = "".join(currentInt)
                    outputs.append(currentInt)
                    currentInt = []
        else:
            # if done with list, finsh the last integer using same proces as on line 21
            if len(currentInt) > 0:
                currentInt = "".join(currentInt)
                outputs.append(currentInt)
                currentInt = []

    if len(outputs) == numberOfInts:
        return outputs
    else:
        return f"error: number of outputs ({len(outputs)}) does not match expected number ({numberOfInts})"



