
class Animal:
    def __init__(self, **kwargs): #constructor
        self._type = kwargs["type"] if 'type' in kwargs else 'kitten' 
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'

    def type(self, t= None): #method .. setter and getter
        if t: self._type = t
        return self._type
    
    def name(self, n= None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'
    

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)
    print(Animal(type = 'velicraptor', name = 'veronica', sound = 'hello'))
    print(Animal())
    a0.sound('bark')
    print(a0)

if __name__ == "__main__":
    main()
