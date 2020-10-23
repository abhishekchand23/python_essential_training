
def main():
    infile = open('Passport_size_photo.jpg', 'rb')
    outfile = open('Passport_size_copy.jpg', 'wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print(".", end='')
        else:
            break
    outfile.close()
    print('\n done.')

if __name__ == "__main__":
    main()