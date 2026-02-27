import sys

#Average function definition
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

#Getting the argument
args = sys.argv[1:]

#Initializing variables
column_id = None
filename = None
do_average = False

#Loop through to find the flags
while len(args) > 0:
    arg = args.pop(0)
    if arg == "-c":
        column_id = args.pop(0)
    elif arg == "-a":
        do_average = True
    else:
        filename = arg #If it's not a flag, it's the filename

if column_id:
    try:
        int(column_id)
    except ValueError:
        raise ValueError(f"Error in parsing column id. Input is not a valid integer.")

#File reading 
try:
    with open(filename, "r") as input_file:
        data_list = []
        for line in input_file:
            #Using split('\t') 
            split_line = line.strip().split('\t')
            
            if column_id:
                #Getting specific column
                val = split_line[int(column_id) - 1]
                data_list.append(float(val))
            else:
                #Getting all columns
                for item in split_line:
                    data_list.append(float(item))

except FileNotFoundError:
    raise FileNotFoundError(f"The file '{filename}' was not found.")

if do_average:
    print(average(data_list))