def _set(tab, instruction):
    instruction = instruction.split(" ")
    tab[instruction[1]][instruction[0]] = instruction[2]
    return 0

def _set(tab, instruction):
    instruction = instruction.split(" ")
    return tab[instruction[1]][instruction[0]]

def read_instruction(tab, instruction):
    # clic 0 0
    # reserve 0
    # score 0
    # get 0 0
    # set 0 0 0
    instruction = instruction.lower()

    if instruction[0] == "c":
        return clic(tab, instruction[4:])

    elif instruction[0] == "r":
        return reserve(tab, instruction[7:])

    elif instruction[0:2] == "sc":
        return score(tab, instruction[5:])

    elif instruction[0:2] == "se":
        return _set(tab, instruction[3:])

    elif instruction[0] == "g":
        return _get(tab, instruction[3:])
    
    else:
        return -1