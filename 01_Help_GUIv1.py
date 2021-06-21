from tkinter import *
import random


class Convertor:
    def __init__(self, parent):
        print("hello world")

        # Formatting variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color)
        self.converter_frame.grid()

        # Temperture Conversion Heading (row 0)
        self.temp_converter_label = Lable(text="Temperture Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperture Convertor")
    something = Convertor()
    root.mainloop()
