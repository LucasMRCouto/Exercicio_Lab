from pymongo import MongoClient
from classes import Cuidador, Habitat, Animais
from bson.objectid import ObjectId


class ZoologicoDAO:
    def __init__(self, database):
        self.db = database

    def create_animal(self, animal):
        try:
            result = self.db.collection.insert_one(
                {
                    "id": animal.id,
                    "nome": animal.nome,
                    "especie": animal.especie,
                    "idade": animal.idade,
                    "habitat": {
                        "id": animal.habitat.id,
                        "nome": animal.habitat.nome,
                        "tipoAmbiente": animal.habitat.tipoAmbiente,
                        "cuidador": {
                            "id": animal.habitat.cuidador.id,
                            "nome": animal.habitat.cuidador.nome,
                            "documento": animal.habitat.cuidador.documento
                        }
                    }
                }
            )
            print(f"Animal created with id: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"An error occurred while creating animal: {e}")
            return None

    def read_animal_by_id(self, animal_id: str):
        try:
            animal = self.db.collection.find_one({"_id": ObjectId(animal_id)})
            if animal:

                id1 = animal['id']
                nome1 = animal['nome']
                especie1 = animal['especie']
                idade1 = animal['idade']
                habitat_aux = animal['habitat']
                habitat1 = Habitat(habitat_aux['id'], habitat_aux['nome'], habitat_aux['tipoAmbiente'], Cuidador(habitat_aux['cuidador']['id'], habitat_aux['cuidador']['nome'], habitat_aux['cuidador']['documento']))

                print(f"Animal found: {animal}")
                return Animais(id1, nome1, especie1, idade1, habitat1)
            else:
                print(f"No animal found with id {animal_id}")
                return None
        except Exception as e:
            print(f"An error occurred while reading animal: {e}")
            return None

    def update_animal(self, animal_id, animal):
        try:

            result = self.db.collection.update_one({"_id": ObjectId(animal_id)}, {"$set": {
                "id": animal.id,
                "nome": animal.nome,
                "especie": animal.especie,
                "idade": animal.idade,
                "habitat": {
                    "id": animal.habitat.id,
                    "nome": animal.habitat.nome,
                    "tipoAmbiente": animal.habitat.tipoAmbiente,
                    "cuidador": {
                        "id": animal.habitat.cuidador.id,
                        "nome": animal.habitat.cuidador.nome,
                        "documento": animal.habitat.cuidador.documento
                    }
                }
            }})

            if result.modified_count:
                print(f"Animal {animal_id} updated")
            else:
                print(f"No animal found with id {animal_id}")
            return result.modified_count
        except Exception as e:
            print(f"An error occurred while updating animal: {e}")
            return None

    def delete_animal(self, animal_id: str):
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(animal_id)})
            if result.deleted_count:
                print(f"Animal {animal_id} deleted")
            else:
                print(f"No animal found with id {animal_id}")
            return result.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting animal: {e}")
            return None
