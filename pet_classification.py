class Pet:
    def __init__(self, name='', animal_type='', age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    my_pet = Pet()

    name = input("Enter pet name: ")
    animal_type = input("Pet's animal type: ")
    age_str = input("Pet's age in integer: ")
    age = int(age_str) \
        if age_str.isdigit() \
        else 0

    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)

    print("\n*** PET INFORMATION ***")
    print(f"Name:        \033[1m\033[33m{my_pet.get_name()}\033[0m")
    print(f"Animal Type: \033[1m\033[33m{my_pet.get_animal_type()}\033[0m")
    print(f"Age:         \033[1m\033[33m{my_pet.get_age()}\033[0m")

if __name__ == "__main__":
    main()
