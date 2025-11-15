class Cliente:
    def __init__(self, id: str, phone: int):
        self.id = id 
        self.phone = phone 

    def __str__(self):
        return f"{self.id}:{self.phone}"
    
    def getID(self):
        return self.id
    def getPhone(self):
        return self.phone 
    
    def setID(self, id: str):
        self.id = id 
    def setPhone(self, fone: int):
        self.phone = fone 


class Theather:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__seats: list[Cliente | None] = [None] * capacity

    def search(self, id: int) -> int:
        for i, c in enumerate(self.__seats):
            if c is not None and c.getID() == id:
                return i 
        
        return -i
    
    def verifyIndex(self, index : int) -> bool:
        return 0 <= index < self.__capacity
    




    def reserve(self, id: str, phone: int, index: int ) -> bool:
        if not self.verifyIndex(index):
            print("fail: indice inválido")
            return False
        if self.__seats[index] is not None:
            print("fail: assento ocupado")
            return False
        
        self.__seats[index] = Cliente(id, phone)
        return True
    

def main():
    cine = Theather(0)

    while True:

        line = input(" ")
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        if args[0] == "show":
            print(cine)