import sys 

def main():
    try:
        x = 5/0
    
    except ValueError:
        print('i caught a value error')
    except :
        print(f'unknown error: {sys.exc_info()[1]}')
    else: 
        print('good job')
        print(x)

if __name__ == "__main__":
    main()