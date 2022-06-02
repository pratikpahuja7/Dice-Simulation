from tkinter import *
import random

root = Tk()
root.title("Dice Rolling Simulation")
root.geometry("300x400")


# Getting dice number
def get_number(x):
    """Determines the number of each dice"""
    if x == "\u2680":
        return 1
    elif x == "\u2681":
        return 2
    elif x == "\u2682":
        return 3
    elif x == "\u2683":
        return 4
    elif x == "\u2684":
        return 5
    elif x == "\u2685":
        return 6


# Rolling dice function
def roll_dice():
    """Function to roll the dice"""
    # rolling random dice
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)
    # Determine dice number
    sd1 = get_number(d1)
    sd2 = get_number(d2)
    # update labels
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)
    # update sub labels
    sub_dice_label1.config(text=sd1)
    sub_dice_label2.config(text=sd2)
    # Generate and update total
    total = sd1 + sd2
    total_label.config(text="Total : {}".format(total))


# Creating dice list
my_dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

# Create a frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create dice labels
dice_label1 = Label(my_frame, text="", font=("comic sans", 100))
dice_label1.grid(row=0, column=0, padx=5)
sub_dice_label1 = Label(my_frame, text="", font=("comic sans", 18))
sub_dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, text="", font=("comic sans", 100))
dice_label2.grid(row=0, column=1, padx=5)
sub_dice_label2 = Label(my_frame, text="", font=("comic sans", 18))
sub_dice_label2.grid(row=1, column=1)

my_button = Button(root, text="Roll Dice", command=roll_dice)
my_button.pack(pady=10)

total_label = Label(root, text="", font=("comic sans", 25, "bold"))
total_label.pack(pady=20)

root.mainloop()
