# multiple Inheritence
# class Animal:
#     def __init__(self):
#         self.color = input("Enter color: ")
#         self.eat = input("Enter food: ")

#     def Show_animal_info(self):
#         print(f"Color: {self.color} \n Eat{self.eat}")

# class Pet:
#     def __init__(self):
#         self.owner = input("Enter owner name: ")

#     def Show_pet_info(self):
#         print(f"Owner: {self.owner}")

# class Dog(Pet,Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         Pet.__init__(self)
#         self.name = input("Enter dog name: ")

#     def Show_dog_info(self):
#         print(f"Dog Name: {self.name}")
#         Animal.Show_animal_info(self)
#         Pet.Show_pet_info(self)
        

# dog1 = Dog()
# dog1.Show_dog_info()


#grandparent
#    |
# parent
#    |
# child

#     Animal
    #    /     \
    #  Dog     Cat
    #    \      
    #     HybridAnimal
    #        |
    #       Pet

#hybrid inheritance


from class5_11_06_26 import Animal



class Animal:
    def __init__(self,c):
        self.color = c

    def Show_info(self):
        print(f"Color : {self.color}")    

        

class Dog(Animal):

    def __init__(self,n, c):

        super().__init__(c)

        self.name = n

 

    def Show_info(self):

        super().Show_info()

        print(f"Dog name : {self.name}")           

 

class Cat(Animal):

    def __init__(self,s, c):

        super().__init__(c)

        self.sound = c

 

class Pet:

    def __init__(self,o):

        self.owner = o

 

    def Show_info(self):

        print(f"Owner name : {self.owner}")    

 

class PetDog(Dog,Pet):

    def __init__(self, n, c,a,o):

        Dog.__init__(self,n, c)

        Pet.__init__(self,o)

        self.age = a

 

    def Show_info(self):

        Dog.Show_info(self)

        Pet.Show_info(self)  

        print(f"Dog age: {self.age}") 

    

Petdog1 = PetDog("Tommy",'white','6month','momo') 

Petdog1.Show_info()