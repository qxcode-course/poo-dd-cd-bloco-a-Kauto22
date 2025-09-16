class Towel:
    def __init__(self, color: str, size: str): #Construtor
        self.color = color #Atributos
        self.size = size
        self.wetness = 0

    def __str__(self):
        return f"color:{self.color}, tam:{self.size}, hum:{self.wetness}"

#Variável ou Referência
towel = Towel("green", "G") #Objetos
toalha = Towel("red", "P")
outra = toalha


towel.color = "white"
print(towel.color)
print(towel.size)
print(towel.wetness)

print(towel)