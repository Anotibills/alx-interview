#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_file_size, status_code_counts):
    '''
    This prints the taotal file size and code status
    '''
    print('File size: {}'.format(file_size[0]))
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print('{}: {}'.format(key, status_codes[key]))


def parse_line(line, file_size, status_codes):
    '''
    This correlate the line and file sizes
    '''
    try:
        line = line.rstrip('\n')
        words = line.split(' ')
        file_size[0] += int(words[-1])
        status_code = int(words[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
    except ValueError:
        pass


if __name__ == '__main__':
    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    linenum = 1
    try:
        for line in sys.stdin:
            parse_line(line, file_size, status_codes)
            if linenum % 10 == 0:
                print_stats(file_size, status_codes)
            linenum += 1
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
    print_stats(file_size, status_codes)
