#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    add = 0
    for i in range(1, args):
        add += int(sys.argv[i])
    print(add)
