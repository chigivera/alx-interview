#!/usr/bin/python3
"""
A script that reads log data from standard input, computes metrics,
and prints statistics.

This script processes log entries line by line from stdin. It expects entries
in the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

It calculates the total file size and counts the occurrences of each
HTTP status code. These statistics are printed to standard output after
every 10 lines of input and upon a keyboard interruption (CTRL+C).
"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints the accumulated file size and status code counts.

    The status codes are printed in ascending order.

    Args:
        total_size (int): The total accumulated file size.
        status_codes (dict): A dictionary of status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        # Only print the status code if its count is greater than zero.
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    # Dictionary to store counts for the valid status codes.
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                # The file size is the last part of the split line.
                size = int(parts[-1])
                # The status code is the second to last part.
                code = int(parts[-2])

                # Update the total file size.
                total_size += size

                # If the status code is one of the valid codes, increment its count.
                if code in status_codes:
                    status_codes[code] += 1

            except (ValueError, IndexError):
                # If the line is malformed (e.g., cannot convert to int or
                # parts are missing), skip to the next line.
                continue

            # After every 10 lines, print the current statistics.
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # When CTRL+C is pressed, print the final statistics and then exit.
        print_stats(total_size, status_codes)
        # Re-raising the exception allows the script to terminate and show
        # the traceback as seen in the project example.
        raise

    # This final call ensures that statistics for the last lines are printed
    # if the input ends before a multiple of 10 and without a keyboard interrupt.
    print_stats(total_size, status_codes)
