class PetShop:
    def __init__(self, name, total_cash):
        self.name = name
        self.total_cash = total_cash
        self.pets = []
        self.pets_sold = 0

    def get_pet_count(self):
        return len(self.pets)
    
    def get_cash(self):
        return self.total_cash

    def add_to_cash(self, amount):
        self.total_cash += amount

    def remove_from_cash(self, amount):
        try:
            temporary_cash = self.total_cash - amount
            if temporary_cash < 0:
                raise ValueError("Not enough cash. Cash cannot be negative.")
            else:
                self.total_cash = temporary_cash
        except ValueError as e:
            print(e)

    def add_pet(self, pet):
        self.pets.append(pet)

    def remove_pet(self, pet):
        self.pets.remove(pet)

    def does_pet_exist(self, current_pet):
        try:
            for pet in self.pets:
                if pet == current_pet:
                    return True
                else:
                    raise ValueError(f"{current_pet["name"]} is not in {self.name}'s shop database.")
        except ValueError as e:
            print(e)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def sell_pet(self, pet, customer):
        try:
            if customer.can_afford(pet.price):
                customer.remove_from_cash(pet.price)
                self.add_to_cash(pet.price)
                self.pets.remove(pet)
                self.increase_pets_sold()
                customer.add_pet(pet)
            else:
                raise ValueError("Problem selling pet")
        except ValueError as e:
            print(e)
