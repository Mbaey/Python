class Turtle:
    name = ''

    def __init__(self, name):
        self.name = name


class Fish:
    name = ''

    def __init__(self, name):
        self.name = name


class Pool:


    def __init__(self):
        self.fish = Fish('草鱼')
        self.turtle = Turtle('乌龟')

    def printf(self):
        print("池塘里有%s , %s"%(self.fish.name, self.turtle.name))

pool = Pool()
pool.printf()