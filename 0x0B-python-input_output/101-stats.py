#!/usr/bin/python3

"""
Reads stdin line by line and computes metrics.

Input format: <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
Every 10 lines or on keyboard interrupt, prints:
- Total file size: <total size>
- Number of lines by status code in ascending order (if seen):
  - <status>: <number>
"""

import sys

# Initialize variables for tracking metrics
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read input from stdin line by line
    for line in sys.stdin:
        line_count += 1
        fields = line.split(" ")
        status_code = int(fields[3])
        file_size = int(fields[4])

        # Update metrics
        total_file_size += file_size
        status_codes[status_code] += 1

        # Every 10 lines or on keyboard interrupt, print metrics
        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(str(code) + ":", status_codes[code])

except KeyboardInterrupt:
    # Print final metrics on keyboard interrupt
    print("Total file size:", total_file_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(str(code) + ":", status_codes[code])
