
class Duck:
    sound = 'Quack Quack'  #data 
    movement = 'Walks like a duck'

    def quack(self):
        print(self.sound)
    
    def move(self):
        print(self.movement)
    
def main():
    donald = Duck() #object instantiation
    donald.quack() # call a method of the class
    donald.move()

if __name__ == "__main__":
    main()