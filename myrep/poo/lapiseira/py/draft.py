class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho 

    def __str__(self):
        return f"{self.calibre}: {self.dureza}: {self.calibre}"
class Lapseira:
    def __init__(self, calibre : float):
        self.calibre = calibre 
        self.ponta: Grafite| None = None 
        self.tambor: list[Grafite] = []

    def __str__(self):
        bico = str(self.calibre) if self.ponta else "vazio"
        tambor = ", ".join(str(g) for g in self.tambor)
        return f"calibre: {self.}"


