class Calculadora:
    def __init__(self, batteryMax: int):
        self.batteryMax: int = batteryMax
        self.battery: int = 0
        self.display: float = 0.00

    def __str__(self):
        return(f"display = {self.display:.2f}, battery = {self.battery}")

    def charge(self, increment: int):
        self.battery += increment

        if self.battery > self.batteryMax:
            self.battery = self.batteryMax
            return
        
    def sum(self, a: int, b: int):
        if self.battery <= 0:
            print(f"fail: bateria insuficiente")
            return
        if self.battery > 0:
            self.display = a + b
            self.battery -= 1
            return

    def div(self, den: int, num: int):
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        self.battery -= 1
        if num == 0:  # verificar o divisor!
            print("fail: divisao por zero")
            return
        self.display = den / num
        

def main():
    calculadora = None
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        
        elif args[0] == "init":
            batteryMax = int(args[1])
            calculadora = Calculadora(batteryMax)

        elif args[0] == "show":
            print(calculadora)
        
        elif args[0] == "sum":
            a = int(args[1])
            b = int(args[2])
            calculadora.sum(a, b)
        
        elif args[0] == "div":
            den = int(args[1])
            num = int(args[2])
            calculadora.div(den, num)
        
        elif args[0] == "charge":
            increment =  int(args[1])
            calculadora.charge(increment)

        else:
            print("fail: comando inválido")
        
main()