class Employee:
    def __init__(self, name, age, dob, passport, id):
        self.name = name
        self.age = age
        self.dob = dob
        self.passport = passport
        self.id = id

class Manager(Employee):
    def __init__(self, name, age, dob, passport, id, department, jobTitle, salespersons):
        super().__init__(name, age, dob, passport, id)
        self.department = department
        self.jobTitle = jobTitle
        self.salespersons = salespersons

class Salesperson(Employee):
    def __init__(self, name, age, dob, passport, id, department, jobTitle):
        super().__init__(name, age, dob, passport, id)
        self.department = department
        self.jobTitle = jobTitle

class Car:
    def __init__(self, make, model, year, price, fuelCapacity, maxSpeed, color):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.fuelCapacity = fuelCapacity
        self.maxSpeed = maxSpeed
        self.color = color


