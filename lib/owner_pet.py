class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES: 
            raise Exception("Invalid pet_type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        owner_pets = []
        for pet in Pet.all:
            if pet.owner == self:
                owner_pets.append(pet)
        return owner_pets
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            if pet.owner is None:
                pet.owner = self
                print(f"{pet.name} has been added to {self.name}'s pets.")
            else:
                print(f"{pet.name} already has an owner.")
        else:
            raise Exception("Invalid pet type.")
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)