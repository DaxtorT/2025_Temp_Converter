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

        self.all_calculations_list = ['5.0°C is 41°F', '1.0°F is -17°C', '1.0°C is 34°F', '56.0°F is 13°C', '273.0°F is 134°C', '273.0°C is 523°F']

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                     text="History / Export",
                                     bg="#0066cc",
                                     fg="#ffffff",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)
    
    def to_history(self):
        """
        Opens history log and disables history button
        (so that users can't create multiple history boxes).
        """
        DisplayHistory(self)

class DisplayHistory:
    """
    Displays history log box
    """
    def __init__(self, partner):
        # Setup dialogue box and background colour
        green_back = "#d5e8d4"
        peach_back = "#ffe6cc"
        history_text = ("Below are your recent calculations - showing "
                        "3 / 3 calculations. All calculations are "
                        "shown to the nearest degree.")
        export_text = ("Please push <Export> to save your calculations in "
                       "file. If the filename already exists it will be ")
        conversions = "Hi I am a conversion"


        # Makes new window seperate to main converter window
        self.history_box = Toplevel()

        # Disable history button when already open
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # History Label List (Label Text | Format | BG Colour)
        label_details_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [history_text, ("Arial", "11"), None],
            ["Calculation List", ("Arial", "14"), green_back],
            [export_text, ("Arial", "11"), None]
        ]

        # List to hold history labels once they have been made
        label_ref_list = []

        for count, item in enumerate(label_details_list):
            make_label = Label(self.history_box,
                                      text=item[0], font=item[1],
                                      bg=item[2],
                                      wraplength=300, justify="left", padx=20, pady=10)
            make_label.grid(row=count)
            label_ref_list.append(make_label)

        # Retrieve export instruction label so we can config it to show
        # the filename if user exports
        self.export_label = label_ref_list[3]

        # Make frame to hold buttons (two columns)
        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        # Button List (Button Text | BG Colour | Command | Row | Column)
        button_details_list = [
            ["Export", "#004c99", "", 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1]
        ]

        # Iterate through each item in list and make a button with corresponding details
        for item in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=item[0], bg=item[1],
                                      fg="#ffffff", width=12,
                                      command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=10, pady=10)

    def close_history(self, partner):
        """
        Closes history log box (and enables history button)
        """
        # Put history button back to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()

# Main Routine
if __name__ == "__main__":
    root =Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()