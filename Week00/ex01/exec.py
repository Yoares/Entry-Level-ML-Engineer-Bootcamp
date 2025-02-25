import sys

def rev_swap():
    if len(sys.argv) == 1:
        return
    print(" ".join(sys.argv[1:])[::-1].swapcase())

rev_swap()