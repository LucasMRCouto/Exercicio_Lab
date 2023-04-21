from classes import Cuidador, Habitat, Animais


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def menu(self):
        while True:
            command = input("Digite um comando: ")
            if command == "quit":
                print("Fim do programa!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido, tente novamente.")


class ZoologicoCLI(SimpleCLI):
    def __init__(self, animal_model):
        super().__init__()
        self.animal_model = animal_model
        self.add_command("create", self.create_animal)
        self.add_command("read", self.read_animal)
        self.add_command("update", self.update_animal)
        self.add_command("delete", self.delete_animal)

    def create_animal(self):

        id = input("Entre com o id do cuidador: ")
        nome = input("Entre com o nome do cuidador: ")
        documento = input("Entre com o documento do cuidador: ")
        cuidador = Cuidador(id, nome, documento)

        id = input("Entre com o id do habitat: ")
        nome = input("Entre com o nome do habitat: ")
        tipoAmbiente = input("Entre com o tipo do ambiente do habitat: ")
        habitat = Habitat(id, nome, tipoAmbiente, cuidador)

        id = input("Entre com o id do animal: ")
        nome = input("Entre com o nome do animal: ")
        especie = input("Entre com a especie do animal: ")
        idade = int(input("Entre com a idade do animal: "))
        animal = Animais(id, nome, especie, idade, habitat)

        self.animal_model.create_animal(animal)

    def read_animal(self):
        id = input("Entre com o id: ")
        animal = self.animal_model.read_animal_by_id(id)

        print(f"ID do animal: {animal.id}")
        print(f"Nome do animal: {animal.nome}")
        print(f"Especie do animal: {animal.especie}")
        print(f"Idade do animal: {animal.idade}")
        print(f"ID do habitat: {animal.habitat.id}")
        print(f"Nome do habitat: {animal.habitat.nome}")
        print(f"Tipo do habitat: {animal.habitat.tipoAmbiente}")
        print(f"ID do cuidador: {animal.habitat.cuidador.id}")
        print(f"Nome do cuidador: {animal.habitat.cuidador.nome}")
        print(f"Documento do cuidador: {animal.habitat.cuidador.documento}")

    def update_animal(self):
        animal_id = input("Enter the id: ")

        id = input("Entre com o id do cuidador: ")
        nome = input("Entre com o nome do cuidador: ")
        documento = input("Entre com o documento do cuidador: ")
        cuidador = Cuidador(id, nome, documento)

        id = input("Entre com o id do habitat: ")
        nome = input("Entre com o nome do habitat: ")
        tipoAmbiente = input("Entre com o tipo do ambiente do habitat: ")
        habitat = Habitat(id, nome, tipoAmbiente, cuidador)

        id = input("Entre com o id do animal: ")
        nome = input("Entre com o nome do animal: ")
        especie = input("Entre com a especie do animal: ")
        idade = int(input("Entre com a idade do animal: "))
        animal = Animais(id, nome, especie, idade, habitat)

        self.animal_model.update_animal(animal_id, animal)

    def delete_animal(self):
        id = input("Entre com o id: ")
        self.animal_model.delete_animal(id)

    def menu(self):
        print("Bem vindo ao ZoologicoCLI!")
        print("Comandos: create, read, update, delete, quit")
        super().menu()
