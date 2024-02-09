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
    selection_window = Toplevel()
    selection_window.title("Jordan's Tutoring")
    main_frame = Frame(selection_window)
    main_frame.pack()

    my_label = Label(selection_window, text="")
    my_label.pack(pady=5)
    my_label.config(text="Available tutoring services:")
    
    # Function to handle button click
    def service_button(action):
        if action == "math":
            selection_window.destroy()
            return'Math'
        elif action == "english":
            selection_window.destroy()
            return 'English'
        elif action == "cs":
            selection_window.destroy()
            return 'Computer Science'
            
    # Buttons
    math_button = Button(main_frame, text="Math", command=lambda: service_button("math"))
    math_button.pack(pady=5)
    english_button = Button(main_frame, text="English", command=lambda: service_button("english"))
    english_button.pack(pady=5)
    cs_button = Button(main_frame, text="Computer Science", command=lambda: service_button("cs"))
    cs_button.pack(pady=5)
    
# Get date from calendar
def select_appointment_date():
    root = Tk()
    root.title("Select appointment date:")
    root.geometry("350x250")
    cal = Calendar(root, selectmode="day", year=2024, month=2, day=7)
    cal.pack()
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
    print(service)
    date = select_appointment_date()
    print(date)
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
    try:
        with open("appointments.txt", "w") as file:
            for i, appointment in enumerate(appointments, start=1):
                file.write(f"Service: {appointment.service}, Date: {appointment.date}\n")
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")

# Main program loop
def main():
    root = Tk()
    root.title("Jordan's Tutoring")
    main_frame = Frame(root)
    main_frame.pack(pady=5)
    root.geometry("260x150")
            
    # Function to handle button click
    def button_click(action):
        if action == "place_appointment":
            place_appointment()
        elif action == "view_appointments":
            display_appointments()
        elif action == "save_to_file":
            save_appointments_to_file()
                    
    # Buttons
    place_button = Button(main_frame, text="Place Appointment", command=lambda: button_click("place_appointment"))
    place_button.pack(pady=5)
    view_button = Button(main_frame, text="View Appointments", command=lambda: button_click("view_appointments"))
    view_button.pack(pady=5)
    save_button = Button(main_frame, text="Save to File", command=lambda: button_click("save_to_file"))
    save_button.pack(pady=5)
    exit_button = Button(main_frame, text="Exit", command=root.destroy)
    exit_button.pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    main()

