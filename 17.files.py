
def main():
    f = open('lines.txt') #default for open function is read "r" mode
    for line in f:
        print(line.rstrip()) #rstrip strips whitespace form eol

if __name__ == "__main__":
    main()