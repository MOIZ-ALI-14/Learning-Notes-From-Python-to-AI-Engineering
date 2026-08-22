# 🔵 Polymorphism
# Polymorphism means “many forms.”
# It allows the same method or operation to behave differently depending on the object.
# Different classes can have a method with the same name but different implementations.
# The calling code can use the same method without needing to know the object's exact class.
# It makes code more flexible, reusable, and easier to extend.
# In Python, a common example is method overriding.


class Animal:
    def eat(self):
        print("Animal is eating.")

    def sleep(self):
        print("Animal is sleeping.")

    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def eat(self):
        print("Dog is eating dog food.")

    def sleep(self):
        print("Dog is sleeping in its kennel.")

    def make_sound(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def eat(self):
        print("Cat is eating cat food.")

    def sleep(self):
        print("Cat is sleeping on the sofa.")

    def make_sound(self):
        print("Cat says: Meow!")


animals = [Dog(), Cat()]

for animal in animals:
    animal.eat()
    animal.sleep()
    animal.make_sound()
    print()

# 🔵 Polymorphism — Why, When & Where
# Why: To allow the same method/interface to perform different actions depending on the object.
# When: Use it when different objects need to respond to the same operation in different ways.
# Where: Common in systems with different types of objects that share similar behavior.
# It reduces repeated if/elif logic for checking object types.
# It makes code more flexible, reusable, and easier to extend.
# In your animal example, make_sound() is the same interface, but Dog, Cat, and other animals can behave differently.
# Core idea: Same interface → different behavior.
