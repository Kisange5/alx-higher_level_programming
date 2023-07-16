#!/usr/bin/python3


import sys
from collections import defaultdict


def print_metrics(total_file_size, status_codes):
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def main():
    total_file_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split(" ")
            if len(parts) >= 9:
                status_code = parts[7]
                file_size = int(parts[8])
                total_file_size += file_size
                status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_codes)


if __name__ == "__main__":
    main()
