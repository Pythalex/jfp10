def str_to_array(str_grid):
    """
    Convertit le tableau string en array 2d
    """

    # suppose la forme 2535\n4564\n4456\n4758

    splitted = str_grid.split("\n")
    array2d = [[] for i in range(len(splitted))]

    for i in range(len(splitted)):
        for j in range(len(splitted[i])):
            array2d[i].append(int(splitted[i][j]))

    return array2d

def array_to_str(grid_array):
    """
    Convertit le tableau 2d en string
    """

    stringified = []

    array = []
    for i in range(len(grid_array)):
        array.append("".join([str(grid_array[i][j]) for j in range(len(grid_array[i]))]))

    stringified = "\n".join(array)

    return stringified

if __name__ == "__main__":

    str_grid = "2535\n4564\n4456\n4758"

    array = str_to_array(str_grid)

    print(array)

    stringified = array_to_str(array)

    print(stringified)