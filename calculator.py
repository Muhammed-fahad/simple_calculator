from tkinter import *

frame = Tk()
frame.title("calculator")
e = Entry(frame, width=35, borderwidth="5")
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)


# input arranging
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# clear function
def button_clr():
    e.delete(0, END)


# equal function
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addision":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
        print("fahad")
        print("hello")


# addision function
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addision"
    f_num = int(first_number)
    e.delete(0, END)


# sub function
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


# multiplication function
def button_multiplay():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


# division function
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


# creating buttion
button_1 = Button(frame, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(frame, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(frame, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(frame, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(frame, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(frame, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(frame, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(frame, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(frame, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(frame, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_cl = Button(frame, text="Clear", padx=130, pady=20, command=button_clr)
button_eq = Button(frame, text="=", padx=40, pady=20, command=button_equal)

button_ad = Button(frame, text="+", padx=40, pady=20, command=button_add)
button_sub = Button(frame, text="-", padx=41, pady=20, command=button_subtract)
button_mul = Button(frame, text="*", padx=42, pady=20, command=button_multiplay)
button_div = Button(frame, text="/", padx=42, pady=20, command=button_divide)


# put button on screen
button_1.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=0)
button_4.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=0)
button_7.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=0)
button_0.grid(row=4, column=0)

button_eq.grid(row=4, column=2)
button_cl.grid(row=6, column=0, columnspan=3)

button_ad.grid(row=4, column=1)
button_sub.grid(row=5, column=0)
button_div.grid(row=5, column=1)
button_mul.grid(row=5, column=2)

frame.mainloop()
