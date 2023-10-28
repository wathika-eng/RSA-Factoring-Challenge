#!/usr/bin/env python3
"""
python in the env variables
"""

import sys

"""
module to import
"""


def factors(file):
    """
    Factorizes the numbers from test00 and prints their factorizations
    """
    with open(file, "r") as nf:
        """
        open the file using py file handling
        """
        for line in nf:
            """
            loop through the numbers
            """
            num = int(line)
            for x in range(2, int(num ** 0.5) + 1):
                """
                find the factorial
                """
                if num % x == 0:
                    """
                    stop when it gets to 0
                    """
                    print(f"{num}={x}*{num//x}")
                    break


if __name__ == "__main__":
    """
    run once
    """
    if len(sys.argv) != 2:
        print("Usage: python factors.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    """
    take file as input
    """
    factors(input_file)
