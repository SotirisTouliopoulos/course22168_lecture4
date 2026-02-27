
import sys

# save command line input parameters to list
command_line_input = sys.argv
column_id = (command_line_input[1]).split("-")[1]
filename = command_line_input[2]

# control whether column id is not an integer
try:
    int(column_id)
except ValueError:
    # This raises an error and stops the script immediately
    raise ValueError(f"Error in parsing column id. Input is not a valid integer.")

# control whether filename does not exist
try:
    with open(filename, "r") as input:
        k_column_list = []
        for line in input:
            split_line = line.split()
            k_column_value = split_line[int(column_id) -1]
            k_column_list.append(k_column_value)

except FileNotFoundError:
    raise FileNotFoundError(f"The file '{filename}' was not found. Please check the path.")
