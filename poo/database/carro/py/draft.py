class Carro:
    def __init__(self):
        self.pass_ = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100

    def __str__(self):
        return(f"pass: {self.pass_}, gas: {self.gas}, km: {self.km}")
    
    def show(self):
        print(self)

    def enter(self):
        if self.pass_ < self.passMax:
            self.pass_ += 1
        else:
            print(f"fail: limite de pessoas atingido")
    
    def leave(self):
        if self.pass_ > 0:
            self.pass_ -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, amount):
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, dist):
        if self.pass_ == 0:
            print(f"fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print(f"fail: tanque vazio")
            return
        if dist <= self.gas:
            self.km += dist
            self.gas -= dist
        else:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0



def main(): 
    carro = Carro()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        
        if args[0] == "end":
            break

        elif args[0] == "show":
            carro.show()
        
        elif args[0] == "enter":
            carro.enter()
        
        elif args[0] == "leave":
            carro.leave()

        elif args[0] == "fuel":
            amount = int(args[1])
            carro.fuel(amount)
        
        elif args[0] == "drive":
            dist = int(args[1])
            carro.drive(dist)

        else:
            print("fail: comando inválido")
main()

