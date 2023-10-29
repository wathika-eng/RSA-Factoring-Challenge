#!/usr/bin/env python3
"""
python in the env variables
"""

import sys
import time

"""
modules to import
"""


def factors(file):
    """
    Factorizes the numbers from test00 and prints their factorizations
    """
    try:
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
    except FileNotFoundError:
        """
        handle errors
        """
        # print("File not found,ensure tests/test00 is present!")
        print("Usage:factors <input_file>")
    except Exception as e:
        """
        additional errors
        """
        print(f"{e}, failed!")


if __name__ == "__main__":
    """
    run once
    """
    if len(sys.argv) != 2:
        # print("Usage:factors <input_file>")
        time.sleep(5)
        sys.exit(1)
    input_file = sys.argv[1]
    """
    take file as input
    """
    factors(input_file)
