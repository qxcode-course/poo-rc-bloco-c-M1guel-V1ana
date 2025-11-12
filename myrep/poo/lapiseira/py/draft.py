class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int ):
        self.calibre = calibre 
        self.dureza = dureza 
        self.tamanho = tamanho

    def gastarFolha(self) -> int:
        if self.dureza == "HB":
            return 1
        elif self.dureza == "2B":
            return 2 
        elif self.dureza == "4B":
            return 4 
        elif self.dureza == "6B":
            return 6
        else:
            return 0 
        
    def __str__(self) -> str:
        return f"[{self.calibre}:{self.dureza}:{self.tamanho}]"

class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico: Grafite | None = None 
        self.tambor: list[Grafite] = []

    def __str__(self ) :
        bico = str(self.bico) if self.bico else "[]"
        tambor = "".join(str(g) for g in self.tambor)
        tambor = f"<{tambor}>"
        return f"calibre: {self.calibre}, bico: {bico}, tambor: {tambor}"
    
    def inserir(self, grafite: Grafite) -> bool:
        if grafite.calibre != self.calibre:
            return False
        
        self.tambor.append(grafite)
        return True


def main():
    lapinho = None

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapinho)
        elif args[0] == "init":
            q = float(args[1])
            lapinho = Lapiseira(q)
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])

            grafite = Grafite(calibre, dureza, tamanho)

            if lapinho is None:
                print("fail: lapiseira nao iniciada")
            elif not lapinho.inserir(grafite):
                print("fail: calibre incompatível")
        elif args[0] == "pull":
            
main()
