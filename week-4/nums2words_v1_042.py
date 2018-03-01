import sys

def words():
    d = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten"
    }
    return d

def main():
    for line in sys.stdin:
        num = line.split()
        d = words()
        s = ""
        for c in num:
            s += "{} ".format(d[int(c)])
        print(s.strip())

if __name__ == '__main__':
    main()