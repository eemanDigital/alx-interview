#!/usr/bin/env python3
"""
Module that reads stdin line by line and computes
some given metrics
"""
import re
import sys


def get_status_code(line):
    """
    Get the status code from a log line.

    Args:
        line: The log line.

    Returns:
        The status code, or None if the status code is not in the line.
    """
    match = re.search(r" \d{3}", line)
    if match:
        return int(match.group(0))
    return None


def main():
    """
    Read lines from stdin and print statistics about them.
    """
    file_size = 0
    status_code_counts = {}
    for line in sys.stdin:
        line = line.rstrip()

        # Ignore lines that do not match the expected format.
        match = re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"(.*?) /(.*?) HTTP/1.1\" (\d{3}) (\d+)$", line)
        if not match:
            continue

        ip_address, date, method, path, _, status_code, file_size_str = match.groups()

        file_size += int(file_size_str)

        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        if len(status_code_counts) % 10 == 0:
            print("File size: {}".format(file_size))
            for status_code, count in sorted(status_code_counts.items()):
                print("{}: {}".format(status_code, count))

    print("File size: {}".format(file_size))
    for status_code, count in sorted(status_code_counts.items()):
        print("{}: {}".format(status_code, count))


if __name__ == "__main__":
    main()
