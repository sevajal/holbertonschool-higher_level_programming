#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        fct(*args)
    except BaseException as error:
        print("Exception:", error, file=sys.stderr)
