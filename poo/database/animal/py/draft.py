class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"

    def grow(self, amount: int):
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            return
        self.age += amount
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")

    def makeSound(self) -> str:
        if self.age == 0: #filhote
            return "---"
        if self.age == 4: #morreu
            return "RIP"
        return self.sound

def main():
    animal: Animal = Animal("", "")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)

        elif args[0] == "grow":
            amount = int(args[1])
            animal.grow(amount)

        elif args[0] == "noise":
            print(animal.makeSound())
            
        elif args[0] == "show":
            print(animal)
    else:
        print("fail: comando inválido")
main()