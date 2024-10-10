# Open the input file and output file
with open('input21.txt', 'r') as infile, open('output21.txt', 'w') as outfile:
    # Process each line in the input file
    for line in infile:
        # Split the line into columns
        columns = line.split()

        # Skip lines that don't have enough columns
        if len(columns) < 5:
            continue

        # Reformat the columns
        formatted_columns = [
            "{:3.0f}".format(float(columns[0])),
            "{:6.3f}".format(float(columns[1])),
            "  ",  # 2 skipped characters
            "{:12.8f}".format(float(columns[2])),
            "{:12.8f}".format(float(columns[3])),
            "{:12.8f}".format(float(columns[4])),
        ]

        # Write the reformatted line to the output file
        outfile.write(''.join(formatted_columns) + '\n')
