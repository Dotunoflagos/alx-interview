#!/usr/bin/python3
"""
225.137.79.34 - [2023-08-17 14:31:15.817595] "GET /projects/260 HTTP/1.1" 400 194
<IP Address> - [<date>]               "GET /projects/260 HTTP/1.1" <status code> <file size>
"""


import sys


def main():
    """
    Reads logs
    """
    stdin = sys.stdin
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:
                fileSize += int(line[-1])
                if line[-2] in codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
        report(fileSize, statusCodes)
    except KeyboardInterrupt as e:
        report(fileSize, statusCodes)
        raise


def report(fileSize, statusCodes):
    """
    Prints report
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    main()