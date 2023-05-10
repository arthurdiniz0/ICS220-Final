import tkinter as tk
from tkinter import messagebox
import pickle

# Define the global variables for the inventory and employees
inventory = None
employees = []

class Car:
    def __init__(self, name, car_type, car_id, price, fuel_capacity, max_speed, color):
        self.name = name
        self.car_type = car_type
        self.car_id = car_id
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
        self.add_employee_button = tk.Button(self, text="Add Employee", command=self.show_add_employee_window)
        self.add_employee_button.grid(row=0, column=0, padx=10, pady=10)

        self.add_car_button = tk.Button(self, text="Add Car", command=self.show_add_car_window)
        self.add_car_button.grid(row=1, column=0, padx=10, pady=10)

        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.grid(row=2, column=0, padx=10, pady=10)

        self.show_employees_button = tk.Button(self, text="Show Employees", command=self.show_employees)
        self.show_employees_button.grid(row=19, column=0, padx=10, pady=10)
        
        self.show_cars_button = tk.Button(self, text="Show Cars", command=self.show_cars)
        self.show_cars_button.grid(row=20, column=0, padx=10, pady=10)

    def show_add_employee_window(self):
        self.add_employee_window = tk.Toplevel(self.master)
        self.add_employee_window.title("Add Employee")

        # Create the widgets for the add employee window
        self.name_label = tk.Label(self.add_employee_window, text="Name")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.add_employee_window)
        self.name_entry.pack()

        self.age_label = tk.Label(self.add_employee_window, text="Age")
        self.age_label.pack()

        self.age_entry = tk.Entry(self.add_employee_window)
        self.age_entry.pack()

        self.dob_label = tk.Label(self.add_employee_window, text="Date of Birth")
        self.dob_label.pack()

        self.dob_entry = tk.Entry(self.add_employee_window)
        self.dob_entry.pack()

        self.passport_label = tk.Label(self.add_employee_window, text="Passport")
        self.passport_label.pack()

        self.passport_entry = tk.Entry(self.add_employee_window)
        self.passport_entry.pack()

        self.emp_id_label = tk.Label(self.add_employee_window, text="Employee ID")
        self.emp_id_label.pack()

        self.emp_id_entry = tk.Entry(self.add_employee_window)
        self.emp_id_entry.pack()

        self.department_label = tk.Label(self.add_employee_window, text="Department")
        self.department_label.pack()

        self.department_entry = tk.Entry(self.add_employee_window)
        self.department_entry.pack()

        self.job_title_label = tk.Label(self.add_employee_window, text="Job Title")
        self.job_title_label.pack()

        self.job_title_entry = tk.Entry(self.add_employee_window)
        self.job_title_entry.pack()

        # Create the button to add the employee
        add_employee_button = tk.Button(self.add_employee_window, text="Add Employee", command=self.add_employee)
        add_employee_button.pack()

    def show_add_car_window(self):
        self.add_car_window = tk.Toplevel(self.master)
        self.add_car_window.title("Add Car")

        # Create the widgets for the add car window
        self.name_label = tk.Label(self.add_car_window, text="Name")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.add_car_window)
        self.name_entry.pack()

        self.type_label = tk.Label(self.add_car_window, text="Type")
        self.type_label.pack()

        self.type_entry = tk.Entry(self.add_car_window)
        self.type_entry.pack()

        self.id_label = tk.Label(self.add_car_window, text="ID")
        self.id_label.pack()

        self.id_entry = tk.Entry(self.add_car_window)
        self.id_entry.pack()

        self.price_label = tk.Label(self.add_car_window, text="Price")
        self.price_label.pack()

        self.price_entry = tk.Entry(self.add_car_window)
        self.price_entry.pack()

        self.fuel_label = tk.Label(self.add_car_window, text="Fuel Capacity")
        self.fuel_label.pack()

        self.fuel_entry = tk.Entry(self.add_car_window)
        self.fuel_entry.pack()

        self.speed_label = tk.Label(self.add_car_window, text="Max Speed")
        self.speed_label.pack()

        self.speed_entry = tk.Entry(self.add_car_window)
        self.speed_entry.pack()

        self.color_label = tk.Label(self.add_car_window, text="Color")
        self.color_label.pack()

        self.color_entry = tk.Entry(self.add_car_window)
        self.color_entry.pack()

        # Create the button to add the car
        add_car_button = tk.Button(self.add_car_window, text="Add Car", command=self.add_car)
        add_car_button.pack()



    def add_car(self):
        global inventory

        name = self.name_entry.get()
        car_type = self.type_entry.get()
        ID = self.id_entry.get()
        price = self.price_entry.get()
        fuel_capacity = self.fuel_entry.get()
        max_speed = self.speed_entry.get()
        color = self.color_entry.get()

        # Create a new car object with the entered details
        car = Car(name, car_type, ID, price, fuel_capacity, max_speed, color)

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

        # Load the existing employees from the binary file, or initialize to an empty list if the file is not found
        try:
            with open("employees.bin", "rb") as f:
                employees = pickle.load(f)
        except FileNotFoundError:
            employees = []

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

            # Add the new manager to the list of employees
            employees.append(manager)
        elif job_title.lower() == "salesperson":
            # Create a new salesperson object with the entered details
            salesperson = Salesperson(name, age, dob, passport, emp_id, department, job_title)

            # Add the new salesperson to the list of employees
            employees.append(salesperson)

        # Save the updated list of employees to the binary file
        with open("employees.bin", "wb") as f:
            pickle.dump(employees, f)

        # Display a message to confirm the employee was added
        tk.messagebox.showinfo("Employee added", "The employee has been added to the system.")


    def search_employee(emp_id):
        # Load the list of employees from the binary file
        with open("employees.bin", "rb") as f:
            employees = pickle.load(f)

        # Search for the employee with the corresponding ID
        for employee in employees:
            if employee.emp_id == emp_id:
                return employee

        # Return None if the employee is not found
        return None

    def show_employees(self):
        # Load the list of employees from the binary file
        with open("employees.bin", "rb") as f:
            employees = pickle.load(f)

        # Create a new window to display the list of employees
        self.employees_window = tk.Toplevel(self.master)
        self.employees_window.title("Employees")

        # Create a label to display the list of employees
        employees_label = tk.Label(self.employees_window, text="List of Employees")
        employees_label.pack()

        # Create a text box to display the information of the selected employee
        self.employee_info_text = tk.Text(self.employees_window, height=10, width=50)
        self.employee_info_text.pack()

        # Create a frame to hold the search box and button
        search_frame = tk.Frame(self.employees_window)
        search_frame.pack()

        # Create a label and entry box for the employee ID search
        search_label = tk.Label(search_frame, text="Search Employee ID:")
        search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT)

        # Create a button to search for the employee
        search_button = tk.Button(search_frame, text="Search", command=self.display_employee_info)
        search_button.pack(side=tk.LEFT)

        # Display the list of employees in the text box
        for employee in employees:
            self.employee_info_text.insert(tk.END, f"Name: {employee.name}\nAge: {employee.age}\nDate of Birth: {employee.dob}\nPassport: {employee.passport}\nEmployee ID: {employee.emp_id}\nDepartment: {employee.department}\nJob Title: {employee.job_title}\n")
            if isinstance(employee, Manager):
                self.employee_info_text.insert(tk.END, f"Salespersons: {employee.salespersons}\n")
            self.employee_info_text.insert(tk.END, "\n")

    def display_employee_info(self):
        employee_id = self.search_entry.get()

        # Load the list of employees from the binary file
        try:
            with open("employees.bin", "rb") as f:
                employees = pickle.load(f)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No employees found.")
            return

        # Find the employee with the given ID
        for employee in employees:
            if employee.emp_id == employee_id:
                # Display the employee's information
                info = f"Name: {employee.name}\nAge: {employee.age}\nDate of Birth: {employee.dob}\nPassport: {employee.passport}\nEmployee ID: {employee.emp_id}\nDepartment: {employee.department}\nJob Title: {employee.job_title}"
                tk.messagebox.showinfo("Employee Info", info)
                return

        # If the employee is not found, display an error message
        tk.messagebox.showerror("Error", "No employee found with that ID.")

    
    def show_cars(self):
        self.cars_window = tk.Toplevel(self.master)
        self.cars_window.title("Cars List")

        # Load the inventory from the binary file, or create a new inventory object if the file is not found
        try:
            with open("inventory.bin", "rb") as f:
                inventory = pickle.load(f)
        except FileNotFoundError:
            inventory = Inventory()

        # Create a label for each car in the inventory
        for i, car in enumerate(inventory.cars):
            tk.Label(self.cars_window, text=f"Car {i+1}").grid(row=i, column=0, padx=10, pady=10)
            tk.Label(self.cars_window, text=f"Name: {car.name}").grid(row=i, column=1, padx=10, pady=10)
            tk.Label(self.cars_window, text=f"Type: {car.car_type}").grid(row=i, column=2, padx=10, pady=10)
            tk.Label(self.cars_window, text=f"ID: {car.car_id}").grid(row=i, column=3, padx=10, pady=10)
            tk.Label(self.cars_window, text=f"Price: {car.price}").grid(row=i, column=4, padx=10, pady=10)
            tk.Label(self.cars_window, text=f"Fuel Capacity: {car.fuel_capacity}").grid(row=i, column=5, padx=10, pady=10)
            tk.Label(self.cars_window, text=f"Max Speed: {car.max_speed}").grid(row=i, column=6, padx=10, pady=10)
            tk.Label(self.cars_window, text=f"Color: {car.color}").grid(row=i, column=7, padx=10, pady=10)

        # Create the widgets for the search box
        search_label = tk.Label(self.cars_window, text="Search car by ID:")
        search_label.grid(row=len(inventory.cars), column=0, padx=10, pady=10)

        search_entry = tk.Entry(self.cars_window)
        search_entry.grid(row=len(inventory.cars), column=1, padx=10, pady=10)

        search_button = tk.Button(self.cars_window, text="Search", command=lambda: self.display_car_info(search_entry.get(), inventory))
        search_button.grid(row=len(inventory.cars), column=2, padx=10, pady=10)

    def display_car_info(self, car_id, inventory):
    # Find the car with the given ID
        for car in inventory.cars:
            if car.car_id == car_id:
                # Display the car information
                tk.messagebox.showinfo("Car Info", f"Name: {car.name}\nType: {car.car_type}\nPrice: {car.price}\nFuel Capacity: {car.fuel_capacity}\nMax Speed: {car.max_speed}\nColor: {car.color}")
                return

        # If no car was found with the given ID, display an error message
        tk.messagebox.showerror("Car not found", "No car was found with the given ID.")




# Create the GUI application
root = tk.Tk()
app = Application(master=root)
app.mainloop()