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
    def __init__(self, name, dob, passport, emp_id, basic_salary, commission=0):
        self.name = name
        self.dob = dob
        self.passport = passport
        self.emp_id = emp_id
        self.basic_salary = basic_salary
        self.commission = commission
        
class Manager(Employee):
    def __init__(self, name, dob, passport, emp_id, department, job_title, salespersons, basic_salary, commission=0):
        super().__init__(name, dob, passport, emp_id, basic_salary, commission=0)
        self.department = department
        self.job_title = job_title
        self.salespersons = salespersons

class Salesperson(Employee):
    def __init__(self, name, dob, passport, emp_id, department, job_title, basic_salary, commission=0):
        super().__init__(name, dob, passport, emp_id, basic_salary, commission=0)
        self.department = department
        self.job_title = job_title


class Inventory:
    def __init__(self, cars=None, sales=None, quantities=None, prices=None):
        self.cars = cars if cars is not None else []
        self.sales = sales if sales is not None else []
        self.quantities = quantities if quantities is not None else []
        self.prices = prices if prices is not None else []

class Sale:
    def __init__(self, car, salesperson, sale_price):
        self.car = car
        self.salesperson = salesperson
        self.sale_price = sale_price
        self.profit = self.sale_price - self.car.price


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold the buttons
        button_frame = tk.Frame(self)
        button_frame.grid(row=0, column=0, padx=10, pady=10)

        # Add Employee button
        self.add_employee_button = tk.Button(button_frame, text="Add Employee", command=self.show_add_employee_window)
        self.add_employee_button.grid(row=0, column=0, padx=10, pady=10)

        # Add Car button
        self.add_car_button = tk.Button(button_frame, text="Add Car", command=self.show_add_car_window)
        self.add_car_button.grid(row=1, column=0, padx=10, pady=10)

        # Show Employees button
        self.show_employees_button = tk.Button(button_frame, text="Show Employees", command=self.show_employees)
        self.show_employees_button.grid(row=2, column=0, padx=10, pady=10)

        # Show Cars button
        self.show_cars_button = tk.Button(button_frame, text="Show Cars", command=self.show_cars)
        self.show_cars_button.grid(row=3, column=0, padx=10, pady=10)

        # Add Sale button
        add_sale_button = tk.Button(button_frame, text="Add Sale", command=self.show_add_sale_window)
        add_sale_button.grid(row=4, column=0, padx=10, pady=10)

        # Show Sales button
        self.show_sales_button = tk.Button(button_frame, text="Show Sales", command=self.show_sales)
        self.show_sales_button.grid(row=5, column=0, padx=10, pady=10)

        # Quit button
        self.quit_button = tk.Button(button_frame, text="Quit", command=self.master.destroy)
        self.quit_button.grid(row=6, column=0, padx=10, pady=10)

    def show_add_employee_window(self):
        self.add_employee_window = tk.Toplevel(self.master)
        self.add_employee_window.title("Add Employee")

        # Create the widgets for the add employee window
        self.name_label = tk.Label(self.add_employee_window, text="Name")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.add_employee_window)
        self.name_entry.pack()

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

        self.basic_salary_label = tk.Label(self.add_employee_window, text="Basic Salary")
        self.basic_salary_label.pack()

        self.basic_salary_entry = tk.Entry(self.add_employee_window)
        self.basic_salary_entry.pack()

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

    def show_add_sale_window(self):
        self.add_sale_window = tk.Toplevel(self.master)
        self.add_sale_window.title("Register a Sale")

        # Create the widgets for the add sale window
        self.car_id_label = tk.Label(self.add_sale_window, text="Car ID")
        self.car_id_label.pack()

        self.car_id_entry = tk.Entry(self.add_sale_window)
        self.car_id_entry.pack()

        self.salesperson_id_label = tk.Label(self.add_sale_window, text="Salesperson ID")
        self.salesperson_id_label.pack()

        self.salesperson_id_entry = tk.Entry(self.add_sale_window)
        self.salesperson_id_entry.pack()

        self.sale_price_label = tk.Label(self.add_sale_window, text="Sale Price")
        self.sale_price_label.pack()

        self.sale_price_entry = tk.Entry(self.add_sale_window)
        self.sale_price_entry.pack()

        # Create the button to register the sale
        add_sale_button = tk.Button(self.add_sale_window, text="Register Sale", command=self.add_sale)
        add_sale_button.pack()

    def add_sale(self):
        # Get the sale information from the entries in the add sale window
        car_id = self.car_id_entry.get()
        salesperson_id = self.salesperson_id_entry.get()
        sale_price = float(self.sale_price_entry.get())

        # Load the inventory and employees from the binary files
        try:
            with open("inventory.bin", "rb") as f:
                inventory = pickle.load(f)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No inventory found.")
            return

        try:
            with open("employees.bin", "rb") as f:
                employees = pickle.load(f)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No employees found.")
            return

        # Find the car and salesperson with the given IDs
        car = None
        salesperson = None
        for c in inventory.cars:
            if c.car_id == car_id:
                car = c
                break
        for s in employees:
            if s.emp_id == salesperson_id and isinstance(s, Salesperson):
                salesperson = s
                break

        # If the car or salesperson is not found, display an error message
        if car is None:
            tk.messagebox.showerror("Error", "No car found with that ID.")
            return
        elif salesperson is None:
            tk.messagebox.showerror("Error", "No salesperson found with that ID.")
            return

        # Create a Sale object and add it to the inventory
        sale = Sale(car, salesperson, sale_price)
        inventory.sales.append(sale)

        # Update the salesperson's commission and the manager's commission
        profit = sale_price - car.price
        salesperson_amount = profit * 0.065
        manager_amount = profit * 0.035
        company_amount = profit * 0.9
        salesperson.commission += salesperson_amount
        for manager in employees:
            if isinstance(manager, Manager) and salesperson in manager.salespersons:
                manager.commission += manager_amount

        # Update the inventory to reflect the sale
        car_index = inventory.cars.index(car)
        inventory.quantities[car_index] -= 1
        inventory.prices[car_index] = sale_price

        # Save the updated inventory and employee data to the binary files
        with open("inventory.bin", "wb") as f:
            pickle.dump(inventory, f)

        with open("employees.bin", "wb") as f:
            pickle.dump(employees, f)

        # Display a message to confirm the sale was added
        tk.messagebox.showinfo("Sale added", "The sale has been added to the records.")

        # Close the add sale window
        self.add_sale_window.destroy()


    def show_sales(self):
        self.sales_window = tk.Toplevel(self.master)
        self.sales_window.title("Sales List")

        # Load the inventory and employees from the binary files
        try:
            with open("inventory.bin", "rb") as f:
                inventory = pickle.load(f)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No inventory found.")
            return

        try:
            with open("employees.bin", "rb") as f:
                employees = pickle.load(f)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No employees found.")
            return

        # Load the sales from the inventory object
        sales = inventory.sales

        # Create a label and a "Delete Sale" button for each sale in the list of sales
        for i, sale in enumerate(sales):
            sale_frame = tk.Frame(self.sales_window)
            sale_frame.grid(row=i, column=0, padx=10, pady=10)

            tk.Label(sale_frame, text=f"Sale {i+1}").grid(row=0, column=0, padx=10, pady=10)
            tk.Label(sale_frame, text=f"Salesperson: {sale.salesperson.name}").grid(row=1, column=0, padx=10, pady=10)
            #tk.Label(sale_frame, text=f"Manager: {sale.manager.name}").grid(row=2, column=0, padx=10, pady=10)
            tk.Label(sale_frame, text=f"Car: {sale.car.name}").grid(row=3, column=0, padx=10, pady=10)
            tk.Label(sale_frame, text=f"Selling Price: {sale.sale_price}").grid(row=4, column=0, padx=10, pady=10)
            #tk.Label(sale_frame, text=f"Profit: {sale.profit[i]}").grid(row=5, column=0, padx=10, pady=10)

            delete_button = tk.Button(sale_frame, text="Delete Sale", command=lambda i=i: self.delete_sale(i))
            delete_button.grid(row=6, column=0, padx=10, pady=10)


    def add_car(self):
        global inventory

        name = self.name_entry.get()
        car_type = self.type_entry.get()
        ID = self.id_entry.get()
        price = float(self.price_entry.get())
        fuel_capacity = float(self.fuel_entry.get())
        max_speed = float(self.speed_entry.get())
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
        dob = self.dob_entry.get()
        passport = self.passport_entry.get()
        emp_id = self.emp_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()

        # Determine whether the employee is a manager or salesperson
        if job_title.lower() == "manager":
            # Create a new manager object with the entered details
            salespersons = []
            manager = Manager(name, dob, passport, emp_id, department, job_title, salespersons, basic_salary)

            # Add the new manager to the list of employees
            employees.append(manager)
        elif job_title.lower() == "salesperson":
            # Create a new salesperson object with the entered details
            salesperson = Salesperson(name, dob, passport, emp_id, department, job_title, basic_salary)

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
        search_button = tk.Button(search_frame, text="See info", command=self.display_employee_info)
        search_button.pack(side=tk.LEFT)

        # Display the list of employees in the text box
        for employee in employees:
            self.employee_info_text.insert(tk.END, f"Name: {employee.name}\nDate of Birth: {employee.dob}\nPassport: {employee.passport}\nEmployee ID: {employee.emp_id}\nDepartment: {employee.department}\nJob Title: {employee.job_title}\n")
            if isinstance(employee, Manager):
                self.employee_info_text.insert(tk.END, f"Salespersons: {[e.name for e in employee.salespersons]}\n")
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
        for i, employee in enumerate(employees):
            if employee.emp_id == employee_id:
                # Find the employee with the given ID
                for i, employee in enumerate(employees):
                    if employee.emp_id == employee_id:
                        # Display the employee's information in a new window
                        emp_info_window = tk.Toplevel(self.master)
                        emp_info_window.title("Employee Info")

                        if isinstance(employee, Manager):
                            emp_info_label = tk.Label(emp_info_window, text=f"Name: {employee.name}\nDate of Birth: {employee.dob}\nPassport: {employee.passport}\nEmployee ID: {employee.emp_id}\nDepartment: {employee.department}\nJob Title: {employee.job_title}\nSalary: {employee.basic_salary}\nCommissions: {employee.commission}")
                            salesperson_label = tk.Label(emp_info_window, text="Salespersons:")
                            salesperson_label.pack()

                            # Display a list of available salespersons
                            available_salespersons = []
                            for emp in employees:
                                if isinstance(emp, Salesperson) and emp not in employee.salespersons:
                                    available_salespersons.append(emp)
                                    tk.Label(emp_info_window, text=f"{emp.name} ({emp.emp_id})").pack()

                            # Add buttons to assign and remove salespersons
                            for salesperson in available_salespersons:
                                assign_button = tk.Button(emp_info_window, text=f"Assign {salesperson.name}", command=lambda emp=employee, sp=salesperson: self.assign_salesperson(employee_id, sp.emp_id))
                                assign_button.pack()

                            for salesperson in employee.salespersons:
                                remove_button = tk.Button(emp_info_window, text=f"Remove {salesperson.name}", command=lambda emp=employee, sp=salesperson: self.remove_salesperson(employee_id, sp.emp_id))
                                remove_button.pack()
                        else:
                            emp_info_label = tk.Label(emp_info_window, text=f"Name: {employee.name}\nDate of Birth: {employee.dob}\nPassport: {employee.passport}\nEmployee ID: {employee.emp_id}\nDepartment: {employee.department}\nJob Title: {employee.job_title}\nSalary: {employee.basic_salary}\nCommission: {employee.commission}")

                        emp_info_label.pack()
                        
                        # Add a "Delete Employee" button to the new window
                        delete_button = tk.Button(emp_info_window, text="Delete Employee", command=lambda i=i: self.delete_employee(i, employees))
                        delete_button.pack()
                
                return

        # If the employee is not found, display an error message
        tk.messagebox.showerror("Error", "No employee found with that ID.")



    def delete_employee(self, index, employees):
        # Delete the employee from the list
        employees.pop(index)

        # Save the updated employee list to the binary file
        with open("employees.bin", "wb") as f:
            pickle.dump(employees, f)

        # Display a message to confirm the employee was deleted
        tk.messagebox.showinfo("Employee deleted", "The employee has been deleted.")

    def assign_salesperson(self, manager_id, salesperson_id):
        # Load the list of employees from the binary file
        try:
            with open("employees.bin", "rb") as f:
                employees = pickle.load(f)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No employees found.")
            return

        # Find the manager with the given ID
        manager = None
        for emp in employees:
            if emp.emp_id == manager_id and isinstance(emp, Manager):
                manager = emp
                break

        # Find the salesperson with the given ID
        salesperson = None
        for emp in employees:
            if emp.emp_id == salesperson_id and isinstance(emp, Salesperson):
                salesperson = emp
                break

        # If the manager or salesperson is not found, display an error message
        if manager is None:
            tk.messagebox.showerror("Error", "No manager found with that ID.")
            return
        elif salesperson is None:
            tk.messagebox.showerror("Error", "No salesperson found with that ID.")
            return

        # If the salesperson is already assigned to the manager, display a message and return
        if salesperson in manager.salespersons:
            tk.messagebox.showinfo("Already Assigned", "This salesperson is already assigned to this manager.")
            return

        # Add the salesperson to the manager's list of salespersons
        manager.salespersons.append(salesperson)

        # Save the updated employee data to the binary file
        with open("employees.bin", "wb") as f:
            pickle.dump(employees, f)

        # Display a message to confirm the salesperson was assigned to the manager
        tk.messagebox.showinfo("Salesperson Assigned", "The salesperson has been assigned to the manager.")

    def remove_salesperson(self, manager_id, salesperson_id):
        # Load the list of employees from the binary file
        try:
            with open("employees.bin", "rb") as f:
                employees = pickle.load(f)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No employees found.")
            return

        # Find the manager with the given ID
        manager = None
        for emp in employees:
            if emp.emp_id == manager_id and isinstance(emp, Manager):
                manager = emp
                break

        # Find the salesperson with the given ID
        salesperson = None
        for emp in employees:
            if emp.emp_id == salesperson_id and isinstance(emp, Salesperson):
                salesperson = emp
                break

        # If the manager or salesperson is not found, display an error message
        if manager is None:
            tk.messagebox.showerror("Error", "No manager found with that ID.")
            return
        elif salesperson is None:
            tk.messagebox.showerror("Error", "No salesperson found with that ID.")
            return

        # If the salesperson is not assigned to the manager, display a message and return
        if salesperson not in manager.salespersons:
            tk.messagebox.showinfo("Not Assigned", "This salesperson is not assigned to this manager.")
            return

        # Remove the salesperson from the manager's list of salespersons
        manager.salespersons.remove(salesperson)

        # Save the updated employee data to the binary file
        with open("employees.bin", "wb") as f:
            pickle.dump(employees, f)

        # Display a message to confirm the salesperson was removed from the manager's list
        tk.messagebox.showinfo("Salesperson Removed", "The salesperson has been removed from the manager's list.")


    
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

        search_button = tk.Button(self.cars_window, text="See info", command=lambda: self.display_car_info(search_entry.get(), inventory))
        search_button.grid(row=len(inventory.cars), column=2, padx=10, pady=10)

    def display_car_info(self, car_id, inventory):
    # Find the car with the given ID
        for i, car in enumerate(inventory.cars):
            if car.car_id == car_id:
                # Display the car information in a new window
                car_info_window = tk.Toplevel(self.cars_window)
                car_info_window.title("Car Info")
                car_info_label = tk.Label(car_info_window, text=f"Name: {car.name}\nType: {car.car_type}\nPrice: {car.price}\nFuel Capacity: {car.fuel_capacity}\nMax Speed: {car.max_speed}\nColor: {car.color}")
                car_info_label.pack()
                
                # Add a "Delete Car" button to the new window
                delete_button = tk.Button(car_info_window, text="Delete Car", command=lambda i=i: self.delete_car(i, inventory))
                delete_button.pack()

                return

        # If no car was found with the given ID, display an error message
        tk.messagebox.showerror("Car not found", "No car was found with the given ID.")


    def delete_car(self, index, inventory):
        # Delete the car from the inventory
        inventory.cars.pop(index)
        inventory.quantities.pop(index)
        inventory.prices.pop(index)

        # Save the updated inventory to the binary file
        with open("inventory.bin", "wb") as f:
            pickle.dump(inventory, f)

        # Display a message to confirm the car was deleted
        tk.messagebox.showinfo("Car deleted", "The car has been deleted from the inventory.")

    def delete_sale(self, index):
        # Load the sales from the inventory file
        try:
            with open("inventory.bin", "rb") as f:
                inventory = pickle.load(f)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No inventory found.")
            return

        # Remove the sale from the inventory
        sale = inventory.sales.pop(index)

        # Save the updated inventory to the binary file
        with open("inventory.bin", "wb") as f:
            pickle.dump(inventory, f)

        # Display a message to confirm the sale was deleted
        tk.messagebox.showinfo("Sale deleted", "The sale has been deleted from the inventory.")






# Create the GUI application
root = tk.Tk()
root.title('Car Sales Management')
app = Application(master=root)
app.mainloop()