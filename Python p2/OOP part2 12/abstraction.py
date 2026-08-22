# 🔵 Abstraction — What is it?
# Abstraction means hiding unnecessary implementation details and showing only the essential functionality to the user.
# Think about a car:
# You use:
# steering wheel → to steer
# accelerator → to accelerate
# brake → to stop
# You don't need to know exactly how the engine, fuel injection, transmission, or braking system internally works.
# That's abstraction:
# Show what something does, hide how it does it.
# 🧠 Easy explanation
# Suppose you have a payment system.
# You want your program to say:
# payment.pay(5000)
# You don't want the user to worry about how a credit card processes the payment or how a bank transfer works.
# The internal implementation can be different, but the user works with a simple interface.
# Why use abstraction?
# To hide unnecessary complexity.
# To make programs easier to use and understand.
# To separate what an object must do from how it does it.
# To make large applications easier to maintain.
# To force child classes to implement important functionality.
# When do we use it?
# Use abstraction when your program has a general concept but different classes need to implement the details differently.


from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):

    # Every animal must have an eat() method.
    # But Animal itself doesn't decide HOW it eats.
    @abstractmethod
    def eat(self):
        pass

    # Every animal must have a make_sound() method.
    @abstractmethod
    def make_sound(self):
        pass

    # This is a normal method.
    # All animals can use the same implementation.
    def sleep(self):
        print("Animal is sleeping.")


# Dog provides the actual implementation
class Dog(Animal):

    def eat(self):
        print("Dog eats dog food.")

    def make_sound(self):
        print("Dog says: Woof!")


# Cat provides its own implementation
class Cat(Animal):

    def eat(self):
        print("Cat eats cat food.")

    def make_sound(self):
        print("Cat says: Meow!")


# Create objects
dog = Dog()
cat = Cat()


# Same interface, different implementations
dog.eat()
dog.make_sound()
dog.sleep()

print()

cat.eat()
cat.make_sound()
cat.sleep()

