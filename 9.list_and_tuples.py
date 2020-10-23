def main():
    game = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    print(','.join(game))
    print_list(game)
    

def print_list(o):
    for i in o: 
        print(i, end = " ", flush=True)
        
        

if __name__ == "__main__":
    main()

#tuples are similar to list but they are immutable