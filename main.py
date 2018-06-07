import converter
import read_instruction as read

def main():

    command = input()
    #command = "41212\n\
#11313\n\
#22113\n\
#34133\n\
#31121\n\
#GET 3 1"

    command = command.split("\n")

    array = [command[i] for i in range(len(command) - 1)]
    array = converter.str_array_to_int_array(array)

    command = command[-1]

    print(read.read_instruction(array, command))

    return 0

main()