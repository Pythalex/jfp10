import converter as cnv
import neighbour as nb

def del_voisin(tab, x, y, voisin):
    # prend tous les voisins
    all_v = nb.get_neighbours(tab, x, y)
    # regarde les voisins non encore détruits (évite les boucles)
    for elem in all_v:
        if elem not in voisin:
            voisin.append(elem)
            del_voisin(tab, elem[0], elem[1], voisin)


def clic(tab, inst):
    # commandes
    inst = inst.split(" ")
    save = tab[int(inst[1])][int(inst[0])] + 1

    # Position de départ
    t = [[int(inst[0]), int(inst[1])]]

    del_voisin(tab, int(inst[0]), int(inst[1]), t)

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
        return cnv.array_to_str(_set(tab, instruction[4:]))

    elif instruction[0] == "g":
        return _get(tab, instruction[4:])
    elif instruction[0] == "c":
        return cnv.array_to_str(clic(tab, instruction[5:]))

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