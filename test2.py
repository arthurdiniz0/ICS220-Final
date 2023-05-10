import pickle
with open("employees.bin", "rb") as f:
        employees = pickle.load(f)
        print(employees) # Print the loaded employees list
