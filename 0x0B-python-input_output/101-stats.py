#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys

metrics = {
    "size": 0,
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for i, line in enumerate(sys.stdin, start=1):
        split_line = line.split()
        try:
            status_code = split_line[-2]
            if status_code in metrics:
                metrics[status_code] += 1
            metrics["size"] += int(split_line[-1])
        except Exception:
            pass

        if i % 10 == 0:
            print("File size: {}".format(metrics["size"]))
            for k, v in sorted(metrics.items()):
                if k != "size" and v != 0:
                    print("{}: {}".format(k, v))

except KeyboardInterrupt:
    print("File size: {}".format(metrics["size"]))
    for k, v in sorted(metrics.items()):
        if k != "size" and v != 0:
            print("{}: {}".format(k, v))
    sys.exit(0)
