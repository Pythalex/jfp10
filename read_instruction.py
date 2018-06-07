def _set(tab, instruction):
    instruction = instruction.split(" ")
    tab[int(instruction[1])][int(instruction[0])] = int(instruction[2])
    return tab

def _get(tab, instruction):
    instruction = instruction.split(" ")
    return tab[int(instruction[1])][int(instruction[0])]



def read_instruction(tab, instruction):
    # clic 0 0
    # reserve 0
    # score 0
    # get 0 0
    # set 0 0 0
    instruction = instruction.lower()

    if instruction[0:2] == "se":
        return _set(tab, instruction[4:])

    elif instruction[0] == "g":
        return _get(tab, instruction[4:])
    elif instruction[0] == "c":
        return clic(tab, instruction[5:])

    elif instruction[0] == "r":
        return reserve(tab, instruction[8:])

    elif instruction[0:2] == "sc":
        return score(tab, instruction[6:])
    else:
        return -1

if __name__ == "__main__":
    a = [[4,1,2,1,2],[1,1,3,1,3],[2,2,1,1,3],[3,4,1,3,3],[3,1,1,2,1]]
    b = "SET 3 3 4"
    print(read_instruction(a, b))