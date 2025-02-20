from tkinter import *
from functools import partial  # To prevent unwanted windows
from datetime import date
import all_constants as c

class Converter:
    """
    Temperature conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.all_calculations_list = ['10.0°F is -12°C', '20.0°F is -7°C', '30.0°F is -1°C', '40.0°F is 4°C', '50.0°F is 10°C', '60.0°F is 16°C', "This is a test"]

        # self.all_calculations_list = ['20.0°F is -7°C', '30.0°F is -1°C', '40.0°F is 4°C', '50.0°F is 10°C', '60.0°F is 16°C']


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
        DisplayHistory(self, self.all_calculations_list)

class DisplayHistory:
    """
    Displays history log box
    """
    def __init__(self, partner, calculations):
        # Background colour and text for calculation area
        if len(calculations) <= c.MAX_CALCS:
            calc_bg = "#d5e8d4"
            calc_amount = "all your"
        else:
            calc_bg = "#ffe6cc"
            calc_amount = ("your recent calculations - "
                          f"showing {c.MAX_CALCS} / {len(calculations)}")

        # Create string from calculations list (newest calculations first)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        # Last item added in outside the for loop to there is not a empty space at the end
        if len(newest_first_list) <= c.MAX_CALCS:
            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"
            newest_first_string += newest_first_list[-1]
        
        # Same as before but if we have more than 5 items
        else:
            for item in newest_first_list[:c.MAX_CALCS-1]:
                newest_first_string += item + "\n"
            newest_first_string += newest_first_list[c.MAX_CALCS-1]

        # Setup dialogue boxes
        history_text = (f"Below are {calc_amount} calculations (to the nearest degree).")
        export_text = ("Please push <Export> to save your calculations in "
                       "file. If the filename already exists it will be ")
        

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
            [newest_first_string, ("Arial", "14"), calc_bg],
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
            ["Export", "#004c99", lambda: self.export_file(calculations), 0, 0],
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


    def export_file(self, calculations):
        # *** Get current date for heading and filename ***
        today = date.today()

        # Get day, month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        file_name = f"temperatures_{year}_{month}_{day}"
        write_to = f"{file_name}.txt"

        success_string = (f"Export Successful! The file is called {file_name}.txt")
        self.export_label.config(fg="#009900", text=success_string, font=("Arial", "12", "bold"))

        with open(write_to, "w", encoding="utf-8") as text_file:
            
            text_file.write(f"***** Temperature Calculations ({len(calculations)}) *****\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculation history (Oldest to Newest)...\n")

            # Write each calculation to file
            for item in calculations:
                text_file.write(item)
                text_file.write("\n")


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