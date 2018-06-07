import converter as cnv
import read_instruction as read
import neighbour as nb

def main():

    inline = "a"
    command = ""

    first = True

    try:
        while True:
            if not first:
                command += "\n"
            else:
                first = False
            inline = input()
            command += inline
    except:
        pass
    command = command[:-1]
    
    #command = "41212\n\
#11313\n\
#22113\n\
#34133\n\
#31121\n\
#GET 3 1"

    command = command.split("\n")

    # On parse la grille
    height = 0
    while (command[height][0].isdigit() or command[height][0] == '.'):
        height += 1

    array = [command[i] for i in range(height)]

    array = cnv.str_array_to_int_array(array)

    # On parse les commandes
    command = command[height:]

    for com in command:
        array = cnv.str_to_array(read.read_instruction(array, com))

    print(cnv.array_to_str(array))

    return 0

main()