import sys
sys.stdout.reconfigure(encoding='utf-8')

class Towel:
    def __init__(self, color: str, size: str): #Construtor
        self.color = color #Atributos
        self.size = size
        self.wetness = 0

    def __str__(self): #Transforma em Texto - toString
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

    def dry(self, amount: int) -> None: #Aumenta qnt de água
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def isDry(self) -> bool:
        return self.wetness == 0
    
    def wringOut(self) -> None:
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

def main(): #Execução da função principal
    toalha = Towel("", "") #Objeto Manipulado

    while True: #Loop
        line: str = input() #Entrada de Linhas
        print ("$" + line)
        args: list[str] = line.split(" ") #Lista de Palavras

        if args[0] == "end":
            break
        elif args[0] == "criar": #color, size
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == "mostrar":
            print(toalha)
        elif args[0] == "torcer":
            toalha.wringOut()
        elif args[0] == "seca":
            print("sim" if toalha.isDry() else "nao")
        elif args[0] == "enxugar": #amount
            amount: int = int(args[1])
            toalha.dry(amount)
        else:
            print("fail: comando inválido")


main()
