import tkinter
from tkinter import *
from tkinter import messagebox




#Reset button def

def reset_entry():

    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')

#def for Caltulating the BMI

def calculate_bmi():

    mass = int(weight_tf.get())
    height = int(height_tf.get()) / 100
    bmi = mass / (height * height)
    bmi = round(bmi, 1)
    bmi_index(bmi)

#def for caltulating the ideal BMI
def ideal_bmi():
    mass = int(weight_tf.get())
    height = int(height_tf.get())/100
    age = int(age_tf.get())
    if var.get() == 1:
        ideal = 0.5 * mass / (height)**2 + 11.5
        ideal = round(ideal, 1)
        ideal_index(ideal)
    else:
        ideal = ((0.5 * mass) / ((height)**2)) + (0.03 * age) + 11
        ideal = round(ideal, 1)
        ideal_index(ideal)

#Def for displaying massage box for the results for both BMI and Ideal BMI
def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('BMI', 'something went wrong!')

def ideal_index(ideal):
    if ideal < 18.5:
        messagebox.showinfo('BMI', f'BMI = {ideal} is Underweight')
    elif (ideal > 18.5) and (ideal < 24.9):
        messagebox.showinfo('BMI', f'BMI = {ideal} is Normal')
    elif (ideal > 24.9) and (ideal < 29.9):
        messagebox.showinfo('BMI', f'BMI = {ideal} is Overweight')
    elif (ideal > 29.9):
        messagebox.showinfo('BMI', f'BMI = {ideal} is Obesity')
    else:
        messagebox.showerror('BMI', 'something went wrong!')


# Display and positioning of labels, entry and Buttons

window = Tk()
window.title('BMI Calculator')
window.geometry('400x300')
window.config(bg='#8dc63f')

var = IntVar()

frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)

age_lb = Label(frame, text="Enter Age (2 - 120)")
age_lb.grid(row=1, column=1)

age_tf = Entry(frame,)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(frame, text='Select Gender')
gen_lb.grid(row=2, column=1)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(frame2, text='Male', variable=var, value=1)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(frame2, text='Female', variable=var, value=2)
female_rb.pack(side=RIGHT)

height_lb = Label(frame, text="Enter Height (cm)  ")
height_lb.grid(row=3, column=1)

weight_lb = Label(frame, text="Enter Weight (kg)  ")
weight_lb.grid(row=4, column=1)

height_tf = Entry(frame)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(frame,)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3, text='Calculate', bg='#8dc63f', command=calculate_bmi)
cal_btn.pack(side=LEFT)

cal_ideal = Button(frame3, text='Calculate Ideal', bg='#8dc63f', command=ideal_bmi)
cal_ideal.pack(side=LEFT)

reset_btn = Button(frame3, text='Reset', bg='#8dc63f', command=reset_entry)
reset_btn.pack(side=LEFT)

exit_btn = Button(frame3, text='Exit', bg='#8dc63f', command=lambda: window.destroy())
exit_btn.pack(side=RIGHT)

window.mainloop()

