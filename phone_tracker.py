import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, timezone

class PhoneNumberTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Pakistani Phone Number Tracker")
        self.root.geometry("500x400")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)

        # Title Label
        tk.Label(
            root,
            text="Enter Pakistani Phone Number",
            fg="white",
            bg="#2c3e50",
            font=("Arial", 16, "bold")
        ).place(x=120, y=30)

        # Phone Number Entry
        self.phone_entry = tk.Entry(
            root,
            width=20,
            font=("Arial", 14),
            relief="flat",
            bg="#ecf0f1"
        )
        self.phone_entry.place(x=150, y=80)

        # Track Button
        self.track_button = tk.Button(
            root,
            text="Track Location",
            bg="#3498db",
            fg="white",
            font=("Arial", 12),
            relief="flat",
            command=self.track_location
        )
        self.track_button.place(x=200, y=140)

        # Result Label
        self.result_label = tk.Label(
            root,
            text="Location: Unknown",
            fg="white",
            bg="#2c3e50",
            font=("Arial", 12),
            wraplength=400
        )
        self.result_label.place(x=50, y=200)

    def track_location(self):
        phone_number = self.phone_entry.get().strip()
        if not phone_number:
            messagebox.showerror("Error", "Please enter a phone number!")
            return

        try:
            # Parse phone number
            parsed_number = phonenumbers.parse(phone_number)
            
            # Validate phone number
            if not phonenumbers.is_valid_number(parsed_number):
                messagebox.showerror("Error", "Invalid phone number!")
                return

            # Get location (country/region)
            location = geocoder.description_for_number(parsed_number, "en")
            
            # Get timezone
            time_zones = timezone.time_zones_for_number(parsed_number)
            timezone_info = ", ".join(time_zones) if time_zones else "Unknown"

            # Format result
            result = f"Location: {location}\nTimezone: {timezone_info}"
            if location.lower() == "pakistan":
                result += "\nCountry Code: +92"
            else:
                result += "\nNote: This number is not registered in Pakistan."

            self.result_label.configure(text=result)

        except phonenumbers.NumberParseException:
            messagebox.showerror("Error", "Invalid phone number format! Use +92xxxxxxxxxx")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneNumberTracker(root)
    root.mainloop()