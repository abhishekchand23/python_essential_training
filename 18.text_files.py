
def main():
    infile = open('lines.txt', 'rt') # rt is read and text mode
    outfile = open('lines_copy.txt', 'wt')

    for line in infile:
        print(line.rstrip(), file=outfile) # or you can use outfile.writelines(line)
        print('.', end ="")
    outfile.close()
    print('n\done.')

if __name__ == "__main__":
    main()