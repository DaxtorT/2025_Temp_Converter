from tkinter import *

class Converter():
    """
    Temperature conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """
        
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        instructions = ("Please enter a temperature below and then press "
                        "one of the button to convert it from Centigrade "
                        "to Fahrenheit.")
        self.temp_heading = Label(self.temp_frame,
                                  text=instructions,
                                  wraplength=250, width=40,
                                  justify="left")
        self.temp_heading.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame,
                                text=error,
                                fg="#9C0000")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # Button List (Button Text | BG Colour | Command | Row | Column)
        button_details_list = [
            ["To Celsius", "#990099", "", 0, 0],
            ["To Fahrenheit", "#009900", "", 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004499", "", 1, 1]
        ]

        # List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#ffffff", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)
            self.button_ref_list.append(self.make_button)

        # Retrieve 'History / Export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)

# Main Routine
if __name__ == "__main__":
    root= Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
