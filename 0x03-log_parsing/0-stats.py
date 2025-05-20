#!/usr/bin/python3
import sys
import re

# Regular expression to match the log format
log_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$')

# Initialize counters
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        match = log_pattern.match(line.strip())
        if match:
            ip, date, status, size = match.groups()
            status = int(status)
            size = int(size)
            total_size += size
            if status in status_counts:
                status_counts[status] += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for status in sorted(status_counts.keys()):
                if status_counts[status] > 0:
                    print(f"{status}: {status_counts[status]}")

except KeyboardInterrupt:
    # Print statistics on keyboard interruption
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")
    sys.exit(0) 