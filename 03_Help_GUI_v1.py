from tkinter import *
from functools import partial  # To prevent unwanted windows

class Converter:
    """
    Temperature conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame,
                                     text="Help / Info",
                                     bg="#cc6600",
                                     fg="#ffffff",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, padx=5, pady=5)
    
    def to_help(self):
        """
        Opens help dialogue and disables help button
        (so that users can't create multiple help boxes).
        """
        DisplayHelp(self)

class DisplayHelp:
    """
    Displays help dialogue box
    """
    def __init__(self, partner):
        # Setup dialogue box and background colour
        background = "#ffe6cc"
        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose to convert " \
                    "to either degrees Celsius (Centigrade) or " \
                    "Fahrenheit.. \n\n" \
                    "Note that -273.15 Degrees C " \
                    "(-459.67 F) is absolute zero (the coldest possible " \
                    "temperature). If you try to convert a " \
                    "temperature that is less than -273 Degrees C, " \
                    "you will get an error message. \n\n" \
                    "To see your " \
                    "calculation history and export it to a text " \
                    "file, please click the 'History / Export' button."

        # Makes new window seperate to main converter window
        self.help_box = Toplevel()

        # Disable help button when already open
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box,
                                width=300, height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=( "Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "14", "bold"),
                                     text="Dismiss", 
                                     bg="#cc6600", fg="#ffffff", 
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)


        # List and loop to set the background colour on everything except the buttons
        recolour_list = [self.help_frame, self.help_heading_label, self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialogue box (and enables help button)
        """
        # Put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()

# Main Routine
if __name__ == "__main__":
    root =Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()