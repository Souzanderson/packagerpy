from .basicoperations import divide,multiply
import sys

if __name__ == '__main__':
    args = sys.argv
    res = 0
    if 'mult' in args and len(args) == 4:
        res = multiply(float(args[2]), float(args[3]))
    elif 'div' in args and len(args) == 4:
        res = divide(float(args[2]), float(args[3]))
        
    print(res)