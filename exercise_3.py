import sys

# Average function definition
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Median function definition
def median(numbers):
    if not numbers:
        return 0
    sorted_data = sorted(numbers)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

# Function to count observations
def obs(numbers):
    return len(numbers)

# New: Function to find the biggest number
def biggest(numbers):
    """Returns the maximum value in the list."""
    if not numbers:
        return None
    return max(numbers)

# Getting the argument
args = sys.argv[1:]

# Initializing variables
column_id = None
filename = None
do_average = False
do_median = False
do_obs = False
do_biggest = False  # New flag for biggest

# Loop through to find the flags
while len(args) > 0:
    arg = args.pop(0)
    if arg == "-c":
        if args:
            column_id = args.pop(0)
        else:
            raise ValueError("-c requires a column index.")
    elif arg == "-a":
        do_average = True
    elif arg == "-m":
        do_median = True
    elif arg == "-n":
        do_obs = True
    elif arg == "-b":
        do_biggest = True
    else:
        filename = arg 

if column_id:
    try:
        int(column_id)
    except ValueError:
        raise ValueError(f"Error in parsing column id. Input is not a valid integer.")

# File reading 
try:
    if filename is None:
        raise ValueError("No filename provided.")
        
    with open(filename, "r") as input_file:
        data_list = []
        for line in input_file:
            split_line = line.strip().split('\t')
            if not any(split_line):
                continue

            if column_id:
                col_idx = int(column_id) - 1
                if col_idx < len(split_line):
                    val = split_line[col_idx]
                    if val:
                        data_list.append(float(val))
            else:
                for item in split_line:
                    if item:
                        data_list.append(float(item))

except FileNotFoundError:
    raise FileNotFoundError(f"The file '{filename}' was not found.")
except ValueError as e:
    raise ValueError(f"Data error: {e}")

# Output results
if do_average:
    print(f"Average: {average(data_list)}")

if do_median:
    print(f"Median: {median(data_list)}")

if do_obs:
    print(f"Number of Observations: {obs(data_list)}")

if do_biggest:
    print(f"Biggest: {biggest(data_list)}")