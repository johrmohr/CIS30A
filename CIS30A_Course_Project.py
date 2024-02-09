''' CIS30A Course Project
    Option 1: Business Program
    Jordan's Tutoring Business'''

from tkinter import *
from tkcalendar import *

# Global variables
appointments = []
services = ["Math", "English", "Computer Science"]

# Class Definitions
class Appointment:
    def __init__(self, service, date):
        self.service = service
        self.date = date

# Function to get user input for service selection
def select_service():
    # Display available tutoring services
    print("\nAvailable tutoring services:")
    for i, service in enumerate(services, start=1):
        print(f"{i} - {service}")
        # Allow user to input their choice of service
    selected_number = int(input("Enter the number of your chosen service: "))
    if 1 <= selected_number <= 3:
        # Return the name of the service
        return services[selected_number - 1]
    else:
        # Recursive call for invalid input
        print("Invalid number. Please enter a valid number 1-3.")
        return select_service()

# Get date from calendar
def select_appointment_date():
    # Create a calendar
    root = Tk()
    root.title("Select appointment date:")
    root.geometry("350x250")
    cal = Calendar(root, selectmode="day", year=2024, month=2, day=8)
    cal.pack()
    # Button to grab the date and return it to save in the program
    def grab_date():
        global selected_date
        selected_date = cal.get_date()
        root.destroy()
    my_button = Button(root, text="Select This Date", command=grab_date)
    my_button.pack()
    root.mainloop()
    return selected_date

# Function to place an appointment
def place_appointment():
    # Prompt user for type of service and date of appointment
    service = select_service()
    date = select_appointment_date()
    # Save service and date into your appointments
    appointment = Appointment(service, date)
    appointments.append(appointment)
    print("Appointment placed successfully!")

# Function to display all appointments
def display_appointments():
    print("\nAll Appointments:")
    for i, appointment in enumerate(appointments, start=1):
        print(f"{i}. Subject: {appointment.service}, Date: {appointment.date}")

# Function to save appointments to a file
def save_appointments_to_file():
    print()
    try:
        # Write appointments to file
        with open("appointments.txt", "w") as file:
            for i, appointment in enumerate(appointments, start=1):
                file.write(f"Service: {appointment.service}, Date: {appointment.date}\n")
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")

# Main program loop
while True:
    try:
        # Print main menu
        print("\n Jordan's Tutoring")
        print("1. Place Appointment")
        print("2. View Appointments")
        print("3. Save Appointments to File")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        
        # Handle user choice and call corresponding function
        if choice == "1":
            place_appointment()
        elif choice == "2":
            display_appointments()
        elif choice == "3":
            save_appointments_to_file()
            print("Appointments saved to 'appointments.txt'.")
        elif choice == "4":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
