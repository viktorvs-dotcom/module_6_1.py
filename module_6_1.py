class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name
    
    def eat(self):
        pass


class Mammal(Animal):

    def eat(self, food):
        if food.edible:
            print(f"{self.name} не стал есть {food.name}")
            fed = True
        else:
            print(f"{self.name} съел {food.name}")


class Predator(Animal):

    def eat(self, alive):
        if alive.edible:
            print(f"{self.name} съел {alive.name}")
            fed = True
        else:
            print(f"{self.name} не стал есть {alive.name}")


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a2.fed)
print(a1.alive)
