class Driver(object):

    def __init__(self, full_name: str, experience: int):
        self.full_name = full_name
        self.experience = experience

    def __str__(self):
        return f"Hello I'm {self.full_name}, my driving experience {self.experience} years "


class Engine(object):

    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

    def __str__(self):
        return f'This engine is manufactured by {self.company} and its power is {self.power}hp '



class Car(object):
    def __init__(self, carClass: str, engine: Engine, driver: Driver, brand: str):
        self.carClass = carClass
        self.engine = engine
        self.driver = driver
        self.brand = brand

    def start(self):
        print("Let's go! ")

    def stop(self):
        print("Stop! ")

    def turnRight(self):
        print("Right turn! ")

    def turnLeft(self):
        print("Left turn! ")

    def __str__(self):
        return f"Hello I'm {self.driver.full_name} and my car driving experience is {self.driver.experience}, This car brand is {self.brand}, car engine is {self.engine.company} have {self.engine.power}hp "


class Lorry(Car.Car):
    def __init__(self, carClass, engine, driver, brand, carrying):
        super().__init__(carClass, engine, driver, brand)
        self.carrying = carrying

    def __str__(self):
        return f"This lorry mark is {self.brand}  body load capacity = {self.carrying} "


class Person(drv.Driver):
    def __init__(self, full_name: str, experience: int, age: int):
        super().__init__(full_name, experience)
        self.age = age


    def __str__(self):
        return f"Hello guys my name is {self.full_name} and i'm {self.age} years old! "

class SportCar(Car.Car):
    def __init__(self, carClass: str, engine: Engine, driver: Driver, brand: str, speed: int):
        super().__init__(carClass, engine, driver, brand)
        self.speed = speed


    def __str__(self):
        return f'This Super Car mark {self.brand}, power of engine equal to {self.speed}'