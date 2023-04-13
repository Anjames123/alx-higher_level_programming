#!/usr/bin/python3
"""
101-stats.py: reads stdin line by line and computes metrics.
Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
"""

import sys

count = 0
file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        count += 1
        split_line = line.split()
        try:
            file_size += int(split_line[-1])
        except Exception:
            pass
        try:
            status_code = int(split_line[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except Exception:
            pass
        if count % 10 == 0:
            print("File size: {}".format(file_size))
            for k in sorted(status_codes.keys()):
                if status_codes[k] != 0:
                    print("{}: {}".format(k, status_codes[k]))
except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for k in sorted(status_codes.keys()):
        if status_codes[k] != 0:
            print("{}: {}".format(k, status_codes[k]))
    raise
