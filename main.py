#!/usr/bin/env python3
#py in env varibles

import sys
"""
module to import
"""

def factors(file):
    """
    Factorizes the numbers from test00 and prints their factorizations
    """
    with open(file, "r") as nf:
        for line in nf:
            num = int(line)
            for x in range(2, int(num**0.5) + 1):
                if num % x == 0:
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
    factors(input_file)
