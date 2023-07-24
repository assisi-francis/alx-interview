#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """


import sys
import re
from collections import defaultdict

# Regular expression pattern to match the input format
pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
regex = re.compile(pattern)

# Dictionary to store the file sizes and status code counts
file_sizes = []
status_counts = defaultdict(int)

try:
    for line_number, line in enumerate(sys.stdin, start=1):
        # Check if the line matches the input format
        match = regex.match(line)
        if not match:
            continue

        # Extract the file size and status code from the matched groups
        file_size = int(match.group(4))
        status_code = match.group(3)

        # Update the total file size
        file_sizes.append(file_size)
        total_size = sum(file_sizes)

        # Update the status code counts
        if status_code.isdigit():
            status_counts[status_code] += 1

        # Print statistics after every 10 lines
        if line_number % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")
            print()

except KeyboardInterrupt:
    # Print the final statistics upon receiving a keyboard interruption
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
    sys.exit(0)
