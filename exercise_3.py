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
    # Sorting is required to find the median
    sorted_data = sorted(numbers)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 == 0:
        # If even, average the two middle numbers
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        # If odd, return the middle number
        return sorted_data[mid]

# New: Function to count observations
def obs(numbers):
    return len(numbers)

# Getting the argument
args = sys.argv[1:]

# Initializing variables
column_id = None
filename = None
do_average = False
do_median = False
do_obs = False  # New flag for observations

# Loop through to find the flags
while len(args) > 0:
    arg = args.pop(0)
    if arg == "-c":
        # Check if there's actually an argument after -c
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
            # Using split('\t') 
            split_line = line.strip().split('\t')
            
            # Skip empty lines
            if not any(split_line):
                continue

            if column_id:
                col_idx = int(column_id) - 1
                if col_idx < len(split_line):
                    val = split_line[col_idx]
                    if val:
                        data_list.append(float(val))
            else:
                # Getting all columns
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