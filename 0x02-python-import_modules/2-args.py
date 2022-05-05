#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args == 1:
        print(f"{args - 1} arguments.")
    elif args == 2:
        print(f"{args - 1} argument:")
        print(f"{args -1}: {sys.argv[1]}")
    else:
        print(f"{args - 1} arguments:")
        for i in range(1, args):
            print(f"{i}: {sys.argv[i]}")
