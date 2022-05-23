#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        import sys

        print("{:d}".format(value))
        return(True)
    except (ValueError, TypeError) as error:
        print("Exception:", error, file=sys.stderr)
        return(False)
