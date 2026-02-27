
def exercise_9_function(input_file, output_file):
    # This list will never hold more than 11 items at a time
    top_10_running = []
    
    # Read and Calculate
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            parts = line.split('\t')
            
            # Sum the scores
            total_accession_score = 0
            numbers = parts[1:]
            for number in numbers:
                total_accession_score += float(number)
            
            # Add the current score and line to our running list
            top_10_running.append([total_accession_score, line])
            
            # Sort the running list (High to Low)
            top_10_running.sort(reverse=False)
            
            # Keep only the top 10; discard anything beyond that
            # This prevents the list from growing with the file size
            top_10_running = top_10_running[:10]

    # Extract just the original lines (strings)
    top_10_lines = []
    for item in top_10_running:
        top_10_lines.append(item[1])

    # Write to the output file
    with open(output_file, "w") as out:
        for line in top_10_lines:
            out.write(line + "\n")

# Run the function
exercise_9_function('../data/scores.txt', '../data/scoresextreme.txt')