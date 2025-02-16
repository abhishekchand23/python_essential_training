
class Animal:
    def __init__(self, **kwargs): #constructor
        self._type = kwargs["type"] if 'type' in kwargs else 'kitten' 
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'

    def type(self): #method .. getter
        return self._type
    
    def name(self):
        return self._name

    def sound(self):
        return self._sound
    
def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animals(): requires an Animal')
    print('The {} is named "{}"and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type = 'velicraptor', name = 'veronica', sound = 'hello'))
    print_animal(Animal())

if __name__ == "__main__":
    main()
