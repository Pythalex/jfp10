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