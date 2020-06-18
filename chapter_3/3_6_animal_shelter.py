import enum
from queue import Queue


class Animal(enum.Enum):
    cat = 'cat'
    dog = 'dog'


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()
        self.pos = 0

    def enqueue(self, animal: Animal):
        if animal == Animal.cat:
            self.cats.add([animal, self.pos])
        else:
            self.dogs.add([animal, self.pos])

        self.pos += 1

        return self

    def dequeue(self):
        if self.dogs.is_empty() and self.cats.is_empty():
            raise Exception('no animal in shelter')

        if self.dogs.is_empty():
            return self.cats.remove()

        if self.cats.is_empty():
            return self.dogs.remove()

        dog_pos = self.dogs.peek()[1]
        cat_pos = self.cats.peek()[1]

        if cat_pos < dog_pos:
            return self.cats.remove()
        else:
            return self.dogs.remove()

    def dequeueCat(self):
        if self.cats.is_empty():
            raise Exception('no cats in shelter')

        return self.cats.remove()

    def dequeueDog(self):
        if self.dogs.is_empty():
            raise Exception('no dogs in shelter')

        return self.dogs.remove()

    def __str__(self):
        return 'cats: ' + str(self.cats) + '\ndogs: ' + str(self.dogs)


if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue(Animal.cat).enqueue(Animal.dog).enqueue(Animal.cat)
    print(shelter)
    print(shelter.dequeue())
    print(shelter.dequeue())
    print(shelter.dequeue())
    print(shelter.dequeue())
