from modules.customer import *
from modules.pet_shop import *
from modules.pet import *

customer01 = Customer("Alice", 1000)
customer02 = Customer("Bob", 50)
customer03 = Customer("Jack", 100)

pet01 = Pet("Bors the Younger", "cat", "Cornish Rex", 100)
pet02 = Pet("Sir Percy", "cat", "British Shorthair", 500)
pet03 = Pet("Sir Lancelot", "dog", "Pomsky", 1000)
pet04 = Pet("Arthur", "dog", "Husky", 900)

pet_shop01 = PetShop("Camelot of Pets", 1000)

print(pet_shop01.get_pet_count())
pet_shop01.add_pet(pet01)
pet_shop01.add_pet(pet02)
pet_shop01.add_pet(pet03)
pet_shop01.add_pet(pet04)
print(pet_shop01.get_pet_count())
pet_shop01.remove_pet(pet02)
print(pet_shop01.get_pet_count())
pet_shop01.sell_pet(pet01, customer01)
print(pet_shop01.get_pet_count())
print(pet_shop01.get_cash())
print(customer01.get_pets_count())
