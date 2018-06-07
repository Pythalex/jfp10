import converter

def has_same_value_neighbour(tab, x, y):

    neighbours = []
    val = tab[y][x]

    xleft = (x == 0)
    xright = (x == len(tab) - 1)
    yup = (y == 0)
    ybottom = (y == len(tab[0]) - 1)

    if not xleft:
        if tab[y][x - 1] == val:
            neighbours.append([x, y])

    if not yup:
        if tab[y - 1][x]] == val:
            neighbours.append([x, y])

    if not xright:
        if tab[y][x + 1] == val:
            neighbours.append([x, y])

    if not ybottom:
        if tab[y + 1][x] == val:
            neighbours.append([x, y])

    return neighbours

def del_voisin(tab, x, y, voisin):
    all_v = has_same_value_neighbour(tab, x, y)
    for elem in all_v:
        if elem not in voisin:
            voisin.append(elem)
            del_voisin(tab, elem[0], elem[1], voisin)


def clic(tab, inst):
    inst = inst.split(" ")
    save = tab[int(inst[1])][int(inst[0])] + 1
    t = del_voisin(tab, int(inst(0)), int(inst(1)), [int(inst(0)), int(inst(1))])
    for elem in t:
        tab[elem[1]][elem[0]] = "."
    tab[int(inst[1])][int(inst[0])] = save
    return tab

def _set(tab, inst):
    inst = inst.split(" ")
    tab[int(inst[1])][int(inst[0])] = int(inst[2])
    return tab

def _get(tab, inst):
    inst = inst.split(" ")
    return tab[int(inst[1])][int(inst[0])]

def read_instruction(tab, instruction):
    # clic 0 0
    # reserve 0
    # score 0
    # get 0 0
    # set 0 0 0
    instruction = instruction.lower()

    if instruction[0:2] == "se":
        return converter.array_to_str(_set(tab, instruction[4:]))

    elif instruction[0] == "g":
        return _get(tab, instruction[4:])
    elif instruction[0] == "c":
        return converter.array_to_str(clic(tab, instruction[5:]))

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