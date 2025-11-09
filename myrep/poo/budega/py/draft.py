class Cliente:
    def __init__(self, nome : str):
        self.__nome = nome 

    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f"{self.__nome}"

class Market:
    def __init__(self, n_caixas : int ):
        self.espera : list[Cliente] = []
        self.caixas : list[Cliente | None] = [] 

        for i in range(n_caixas):
            self.caixas.append(None)

    def __str__(self):
        caixas = ", ".join([str(x) if x else "-----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])

        return f"Caixas: [{caixas}]\nEspera:[{espera}]"
    
    def arrive(self, cliente : Cliente):
        self.espera.append(Cliente)

    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("index invalido")
            return
        if self.caixas[index] is not None:
            print("caixa ocupado")
            return
        if len(self.espera) == 0:
            print("ninguem esperando")
            return
        
        self.caixas[index] = self.espera[0]
    
    def finish(self, index: int ) -> Cliente | None:
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa vazio")
            return None
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return None
        aux = self.caixas[index] = None 
        self.caixas[index] = None
        return aux

def main():
    mercado = Market()

    while True:
        line = input()
        print("$" + line)
        args : list[str] = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(mercado)
        if args[0] == "init":
            qtd = int(args[1])
            mercado = Market(qtd)
main()