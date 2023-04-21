class Cuidador:
    def __init__(self, id: str, nome: str, documento: str):
        self.id = id
        self.nome = nome
        self.documento = documento


class Habitat:
    def __init__(self, id: str, nome: str, tipoAmbiente: str, cuidador: Cuidador):
        self.id = id
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador


class Animais:
    def __init__(self, id: str, nome: str, especie: str, idade: int, habitat: Habitat):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat
