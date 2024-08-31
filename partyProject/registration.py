# registration.py

import csv
import re
from tkinter import messagebox
import os


CSV_FILE = 'user_data.csv'

# Function to validate email format
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

# Function to check if the CSV file exists
def check_csv_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Surname", "Email", "Gender", "Age", "Address", "Password"])

# Function to register a new user
def register_user(first_name, surname, email, gender, age, address, password, conf_password):
    check_csv_file()
    
    if password != conf_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return False
    
    if not is_valid_email(email):
        messagebox.showerror("Error", "Invalid email format.")
        return False

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, surname, email, gender, age, address, password])
    
    messagebox.showinfo("Success", "User registered successfully.")
    return True

# Function to authenticate a returning user
def authenticate_user(email, password):
    check_csv_file()
    
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Email'] == email and row['Password'] == password:
                return True
    return False
