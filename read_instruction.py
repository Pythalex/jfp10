import converter

def check_and_erase_neighbours(tab, x, y):

    def rec(tab, x, y, x_parent, y_parent):

        neighbours = []

        xleft = (x == 0)
        xright = (x == len(tab) - 1)
        yup = (y == 0)
        ybottom = (y == len(tab[0]) - 1)

        # On sauvegarde la valeur de la case
        val = tab[y][x]
        # On détruit la case
        tab[y][x] = -1

        # On regarde si les voisins sont de meme valeur et ne sont pas des cases déjà testées

        if not xleft and x - 1 != x_parent:
            neighbours.append(tab[y][x - 1])
            if tab[y][x - 1] == val:
                tab[y][x - 1] = -1
                # On propage la destruction au voisin
                rec(tab, x - 1, y, x, y)

        if not yup and y - 1 != y_parent:
            neighbours.append(tab[y - 1][x])
            if tab[y - 1][x] == val:
                tab[y - 1][x] = -1
                # On propage la destruction au voisin
                rec(tab, x, y - 1, x, y)

        if not xright and x + 1 != x_parent:
            neighbours.append(tab[y][x + 1])
            if tab[y][x + 1] == val:
                tab[y][x + 1] = -1
                # On propage la destruction au voisin
                rec(tab, x + 1, y, x, y)

        if not ybottom and y + 1 != y_parent:
            neighbours.append(tab[y + 1][x])
            if tab[y + 1][x] == val:
                tab[y + 1][x] = -1
                # On propage la destruction au voisin
                rec(tab, x, y + 1, x, y)

        return val in neighbours

    return rec(tab, x, y, x, y)

def has_same_value_neighbour(tab, x, y):

    neighbours = []

    xleft = (x == 0)
    xright = (x == len(tab) - 1)
    yup = (y == 0)
    ybottom = (y == len(tab[0]) - 1)

    if not xleft:
        neighbours.append(tab[y][x - 1])
    if not yup:
        neighbours.append(tab[y - 1][x])
    if not xright:
        neighbours.append(tab[y][x + 1])
    if not ybottom:
        neighbours.append(tab[y + 1][x])

    return tab[x][y] in neighbours

def clic(tab, inst):
    inst = inst.split(" ")
    if has_same_value_neighbour(tab, int(inst[0]), int(inst[1])):
        tab[int(inst[1])][int(inst[0])] += 1
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