class Customer:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pets = []

    def get_cash(self):
        return self.cash
    
    def get_pets_count(self):
        return len(self.pets)
    
    def can_afford(self, amount):
        return self.cash >= amount
    
    # def remove_from_cash(self, amount):
    #     if self.can_afford(amount):
    #         self.cash -= amount
    #     else:
    #         print("Not enough cash")

    def remove_from_cash(self, amount):
        try:
            if self.can_afford(amount):
                self.cash -= amount
            else:
                raise ValueError("Not enough cash.Cash cannot be negative.")
        except ValueError as e:
            print(e)

    def add_pet(self, pet):
        self.pets.append(pet)