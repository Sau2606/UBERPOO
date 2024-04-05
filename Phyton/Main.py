from car import Car
from account import Account
from user import User
from uberX import UberX


if __name__ == "__main__":
    print("Hola mundo")

    print("Car")
    car = Car("AMS125", Account("Jose Dement", "AMD123","josedeme@mgail.com", "asdjasdd"))
    print(vars(car))
    print(vars(car.driver))

    print("UberX: ")
    uberX = UberX("ASE23", Account("Maria Ruiz", "ERT423", "mariar34@gmail.com", "dadadww"),"Chevrolet", "Spark")
    print(vars(uberX))
    print(vars(uberX.driver))

    print("User: ")
    user = User("Pepito perez", "12dffs", "pepito123@gmail.com", "123123")
    print(vars(user))