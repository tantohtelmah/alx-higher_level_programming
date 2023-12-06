#!/usr/bin/python3

import sys

def print_metrics(total_size, status_codes):
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            ip, date, request, status, size = line.split()
            total_size += int(size)
            status_codes[int(status)] += 1
            if count % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
