#!/usr/bin/env python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys


def process_logs():
    '''
    This computes the process log
    '''
    i = 0
    total_file_size = 0
    status_code_counts = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    try:
        for line in sys.stdin:
            args = line.split(' ')
            if len(args) > 7:
                file_size = int(args[-1])
                status_code = args[-2]
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                total_file_size += file_size
                i += 1
                if i == 10:
                    print_stats(total_file_size, status_code_counts)
                    i = 0
        print_stats(total_file_size, status_code_counts)
    except KeyboardInterrupt:
        print_stats(total_file_size, status_code_counts)


def print_stats(total_file_size, status_code_counts):
    '''
    This prints the taotal file size and code status
    '''
    print(f"Total file size: {total_file_size}")
    sorted_status_codes = sorted(
        status_code_counts.keys(), key=lambda x: int(x)
    )
    for status_code in sorted_status_codes:
        count = status_code_counts[status_code]
        if count != 0:
            print(f"{status_code}: {count}")


if __name__ == "__main__":
    process_logs()
