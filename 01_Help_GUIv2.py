from tkinter import *


class Convertor:
    def __init__(self, parent):

        # Formatting variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300,
                                     bg=background_color, pady = 10)
        self.converter_frame.grid()

        # Temperture Conversion Heading (row 0)
        self.temp_converter_label = Lable(self.converter_frame,
                                          text="Temperture Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # help button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperture Convertor")
    something = Convertor()
    root.mainloop()
