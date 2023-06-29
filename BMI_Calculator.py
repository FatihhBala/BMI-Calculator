from tkinter import *

# Screen
window = Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=250)


def bmi_calculate():
    try:
        user_kg = entry_kg.get()
        user_cm = entry_cm.get()
        user_kg = float(user_kg)
        user_cm = float(user_cm)/100
        BMI = user_kg / (user_cm ** 2)
        BMI = round(BMI, 2)

        if user_kg == "" or user_cm =="":
            BMI_result.config(text="Enter both weight and height")
        elif BMI < 18.5:
            BMI_result.config(text="Your BMI is {} \nYou are underweight".format(BMI))
        elif BMI < 25:
            BMI_result.config(text="Your BMI is {} \nYou are normal".format(BMI))
        elif BMI < 30:
            BMI_result.config(text="Your BMI is {} \nYou are overweight".format(BMI))
        elif BMI < 40:
            BMI_result.config(text="Your BMI is {} \nYou are obese".format(BMI))
        else:
            BMI_result.config(text="Your BMI is {} \nYou are extreme obese".format(BMI))
    except ValueError:
        BMI_result.config(text="Enter a valid number")


# Labels
label_1 = Label(text="Enter Your Weight (kg)", fg="black")
label_1.place(x=30, y=35)
label_2 = Label(text="Enter Your Height (cm)", fg="black")
label_2.place(x=28, y=100)
BMI_result = Label()
BMI_result.config(padx=17, pady=17)
BMI_result.pack(side="bottom")

# Entries
entry_kg = Entry(width=10, fg="black", bg="white")
entry_kg.place(x=50, y=55)
entry_kg.focus()
entry_cm = Entry(width=10, fg="black", bg="white")
entry_cm.place(x=50, y=120)

# Button
button = Button(text="BMI Calculate", width=7, command=bmi_calculate)
button.place(x=50, y=150)

window.mainloop()