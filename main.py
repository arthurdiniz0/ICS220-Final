import tkinter as tk
from tkinter import messagebox
import pickle

# Define the global variables for the inventory and employees
inventory = None
employees = None

class Car:
    def __init__(self, make, model, year, price, fuel_capacity, max_speed, color):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.fuel_capacity = fuel_capacity
        self.max_speed = max_speed
        self.color = color

class Employee:
    def __init__(self, name, age, dob, passport, emp_id):
        self.name = name
        self.age = age
        self.dob = dob
        self.passport = passport
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, age, dob, passport, emp_id, department, job_title, salespersons):
        super().__init__(name, age, dob, passport, emp_id)
        self.department = department
        self.job_title = job_title
        self.salespersons = salespersons

class Salesperson(Employee):
    def __init__(self, name, age, dob, passport, emp_id, department, job_title):
        super().__init__(name, age, dob, passport, emp_id)
        self.department = department
        self.job_title = job_title

class Inventory:
    def __init__(self, cars=None, quantities=None, prices=None):
        self.cars = cars if cars is not None else []
        self.quantities = quantities if quantities is not None else []
        self.prices = prices if prices is not None else []

class Sales:
    def __init__(self, date, car, price, salesperson):
        self.date = date
        self.car = car
        self.price = price
        self.salesperson = salesperson

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.car_label = tk.Label(self, text="Car details")
        self.car_label.grid(row=0, column=0, padx=10, pady=10)

        self.make_label = tk.Label(self, text="Make")
        self.make_label.grid(row=1, column=0, padx=10, pady=10)

        self.make_entry = tk.Entry(self)
        self.make_entry.grid(row=1, column=1, padx=10, pady=10)

        self.model_label = tk.Label(self, text="Model")
        self.model_label.grid(row=2, column=0, padx=10, pady=10)

        self.model_entry = tk.Entry(self)
        self.model_entry.grid(row=2, column=1, padx=10, pady=10)

        self.year_label = tk.Label(self, text="Year")
        self.year_label.grid(row=3, column=0, padx=10, pady=10)

        self.year_entry = tk.Entry(self)
        self.year_entry.grid(row=3, column=1, padx=10, pady=10)

        self.price_label = tk.Label(self, text="Price")
        self.price_label.grid(row=4, column=0, padx=10, pady=10)

        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=4, column=1, padx=10, pady=10)

        self.fuel_label = tk.Label(self, text="Fuel Capacity")
        self.fuel_label.grid(row=5, column=0, padx=10, pady=10)

        self.fuel_entry = tk.Entry(self)
        self.fuel_entry.grid(row=5, column=1, padx=10, pady=10)

        self.speed_label = tk.Label(self, text="Max Speed")
        self.speed_label.grid(row=6, column=0, padx=10, pady=10)

        self.speed_entry = tk.Entry(self)
        self.speed_entry.grid(row=6, column=1, padx=10, pady=10)

        self.color_label = tk.Label(self, text="Color")
        self.color_label.grid(row=7, column=0, padx=10, pady=10)

        self.color_entry = tk.Entry(self)
        self.color_entry.grid(row=7, column=1, padx=10, pady=10)

        self.add_car_button = tk.Button(self, text="Add Car", command=self.add_car)
        self.add_car_button.grid(row=8, column=1, padx=10, pady=10)

        self.employee_label = tk.Label(self, text="Employee details")
        self.employee_label.grid(row=9, column=0, padx=10, pady=10)

        self.name_label = tk.Label(self, text="Name")
        self.name_label.grid(row=10, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=10, column=1, padx=10, pady=10)

        self.age_label = tk.Label(self, text="Age")
        self.age_label.grid(row=11, column=0, padx=10, pady=10)

        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=11, column=1, padx=10, pady=10)

        self.dob_label = tk.Label(self, text="Date of Birth")
        self.dob_label.grid(row=12, column=0, padx=10, pady=10)

        self.dob_entry = tk.Entry(self)
        self.dob_entry.grid(row=12, column=1, padx=10, pady=10)

        self.passport_label = tk.Label(self, text="Passport")
        self.passport_label.grid(row=13, column=0, padx=10, pady=10)

        self.passport_entry = tk.Entry(self)
        self.passport_entry.grid(row=13, column=1, padx=10, pady=10)

        self.emp_id_label = tk.Label(self, text="Employee ID")
        self.emp_id_label.grid(row=14, column=0, padx=10, pady=10)

        self.emp_id_entry = tk.Entry(self)
        self.emp_id_entry.grid(row=14, column=1, padx=10, pady=10)

        self.department_label = tk.Label(self, text="Department")
        self.department_label.grid(row=15, column=0, padx=10, pady=10)

        self.department_entry = tk.Entry(self)
        self.department_entry.grid(row=15, column=1, padx=10, pady=10)

        self.job_title_label = tk.Label(self, text="Job Title")
        self.job_title_label.grid(row=16, column=0, padx=10, pady=10)

        self.job_title_entry = tk.Entry(self)
        self.job_title_entry.grid(row=16, column=1, padx=10, pady=10)

        self.add_employee_button = tk.Button(self, text="Add Employee", command=self.add_employee)
        self.add_employee_button.grid(row=17, column=1, padx=10, pady=10)

        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.grid(row=18, column=1, padx=10, pady=10)

    def add_car(self):
        global inventory

        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()
        fuel_capacity = self.fuel_entry.get()
        max_speed = self.speed_entry.get()
        color = self.color_entry.get()
        price = self.price_entry.get()

        # Create a new car object with the entered details
        car = Car(make, model, year, price, fuel_capacity, max_speed, color)

        # Load the inventory from the binary file, or create a new inventory object if the file is not found
        try:
            with open("inventory.bin", "rb") as f:
                inventory = pickle.load(f)
        except FileNotFoundError:
            inventory = Inventory()

        # Add the new car to the inventory
        inventory.cars.append(car)
        inventory.quantities.append(1)
        inventory.prices.append(price)

        # Save the updated inventory to the binary file
        with open("inventory.bin", "wb") as f:
            pickle.dump(inventory, f)

        # Display a message to confirm the car was added
        tk.messagebox.showinfo("Car added", "The car has been added to the inventory.")



    def add_employee(self):
        global employees

        name = self.name_entry.get()
        age = self.age_entry.get()
        dob = self.dob_entry.get()
        passport = self.passport_entry.get()
        emp_id = self.emp_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()

        # Determine whether the employee is a manager or salesperson
        if job_title.lower() == "manager":
            # Create a new manager object with the entered details
            salespersons = []
            manager = Manager(name, age, dob, passport, emp_id, department, job_title, salespersons)

            # Initialize the employees list if it hasn't been loaded yet
            if employees is None:
                employees = []

            # Add the new manager to the list of employees
            employees.append(manager)
        elif job_title.lower() == "salesperson":
            # Create a new salesperson object with the entered details
            salesperson = Salesperson(name, age, dob, passport, emp_id, department, job_title)

            # Initialize the employees list if it hasn't been loaded yet
            if employees is None:
                employees = []

            # Add the new salesperson to the list of employees
            employees.append(salesperson)

        # Save the updated list of employees to the binary file
        with open("employees.bin", "wb") as f:
            pickle.dump(employees, f)

        # Display a message to confirm the employee was added
        tk.messagebox.showinfo("Employee added", "The employee has been added to the system.")


# Create the GUI application
root = tk.Tk()
app = Application(master=root)
app.mainloop()
