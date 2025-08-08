class Artista:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero

    def __str__(self):
        return f"Artista: {self.nome}, Gênero: {self.genero}"

    def __eq__(self, other):
        if isinstance(other, Artista):
            return self.nome == other.nome and self.genero == other.genero
        return False

    def __hash__(self):
        return hash((self.nome, self.genero))