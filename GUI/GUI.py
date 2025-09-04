import tkinter as tk
from logic import logic

global fieldText
global symbol
global num1
global num2
global quin

fieldText = ""
symbol = ""
num1 = ""
num2 = ""
quin = True

def addToField(sth):
    global fieldText
    field.config(state='normal')
    fieldText = fieldText+str(sth)
    field.delete("1.0","end")
    field.insert("1.0", fieldText)
    field.config(state='disabled')

def calculate():
    global fieldText
    global num2
    result = ""
    num2 = fieldText
    field.delete("1.0","end")
    fieldText = ""
    if(symbol == "+"):
        addToField(logic.add(int(num1), int(num2)))
        print(result)
    elif(symbol == "-"):
        addToField(logic.subtract(int(num1), int(num2)))
        print(result)
    elif(symbol == "/"):
        addToField(logic.divide(int(num1), int(num2)))
        print(result)
    elif(symbol == "*"):
        addToField(str(logic.multiply(int(num1), int(num2))))
        print(result)

def clear():
    global fieldText
    global num1
    global num2
    global symbol
    num1 = ""
    num2 = ""
    symbol = ""

    field.config(state='normal')
    fieldText = ""
    field.delete("1.0","end")
    field.config(state='disabled')

def buttonPressAdd():
    global fieldText
    global num1
    global symbol
    symbol += "+"
    num1 = fieldText
    print(symbol + num1)
    field.delete("1.0","end")
    fieldText = ""

def buttonPressSub():
    global fieldText
    global num1
    global symbol
    symbol += "-"
    num1 = fieldText
    field.delete("1.0","end")
    fieldText = ""

def buttonPressDiv():
    global fieldText
    global num1
    global symbol
    symbol += "/"
    num1 = fieldText
    field.delete("1.0","end")
    fieldText = ""

def buttonPressMult():
    global fieldText
    global num1
    global symbol
    symbol += "*"
    num1 = fieldText
    field.delete("1.0","end")
    fieldText = ""

def buttonPressSqu():
    global fieldText
    global num1
    num1 = fieldText
    field.delete("1.0","end")
    fieldText = ""
    addToField(str(logic.square(int(num1))))

def buttonPressSqrt():
    global fieldText
    global num1
    num1 = fieldText
    field.delete("1.0","end")
    fieldText = ""
    addToField(str(logic.sqrt(int(num1))))

def buttonPressToggle():
    global num1
    global fieldText
    global quin
    num1 = fieldText
    field.delete("1.0","end")
    fieldText = ""
    if quin == True:
        addToField(str(logic.convert_to_decimal(int(num1))))
        quin = False
    elif quin == False:
        addToField(str(logic.convert_to_quinary(int(num1))))
        quin = True

def run():
    global field
    window =  tk.Tk()
    window.geometry("400x300")
    window['background'] = "black"
    field=tk.Text(window, height=2, width=21, font=("Times New Roman", 20))
    field.grid(row=1, column = 1, columnspan=5)

    #Number Buttons
    btn0 = tk.Button(window, text="0", command=lambda: addToField(0), width = 5, font = ("Times New Roman", 14))
    btn0.grid(row=2, column = 1, pady = 10)

    btn1 = tk.Button(window, text="1", command=lambda: addToField(1), width = 5, font = ("Times New Roman", 14))
    btn1.grid(row=2, column = 2, pady = 10)

    btn2 = tk.Button(window, text="2", command=lambda: addToField(2), width = 5, font = ("Times New Roman", 14))
    btn2.grid(row=2, column = 3, pady = 10)

    btn3 = tk.Button(window, text="3", command=lambda: addToField(3), width = 5, font = ("Times New Roman", 14))
    btn3.grid(row=2, column = 4, pady = 10)

    btn4 = tk.Button(window, text="4", command=lambda: addToField(4), width = 5, font = ("Times New Roman", 14))
    btn4.grid(row=2, column = 5, pady = 10)

    #Operations Buttons
    btnDiv = tk.Button(window, text="/", command=lambda: buttonPressDiv(), width = 5, font = ("Times New Roman", 14))
    btnDiv.grid(row=3, column = 4, pady = 10)

    btnMult = tk.Button(window, text="*", command=lambda: buttonPressMult(), width = 5, font = ("Times New Roman", 14))
    btnMult.grid(row=3, column = 3, pady = 10)

    btnAdd = tk.Button(window, text="+", command=lambda: buttonPressAdd(), width = 5, font = ("Times New Roman", 14))
    btnAdd.grid(row=3, column = 1, pady = 10)

    btnSub = tk.Button(window, text="-", command=lambda: buttonPressSub(), width = 5, font = ("Times New Roman", 14))
    btnSub.grid(row=3, column = 2, pady = 10)

    btnClr = tk.Button(window, text="Clear", command=lambda: clear(), width = 5, font = ("Times New Roman", 14))
    btnClr.grid(row=3, column = 5, pady = 10)

    btnTog = tk.Button(window, text="Tog", command=lambda: buttonPressToggle() , width = 5, font = ("Times New Roman", 14))
    btnTog.grid(row=4, column = 3, pady = 10)

    btnSqrt = tk.Button(window, text="sqrt", command=lambda: buttonPressSqrt(), width = 5, font = ("Times New Roman", 14))
    btnSqrt.grid(row=4, column = 4, pady = 10)

    btnSqr = tk.Button(window, text="sqr", command=lambda: buttonPressSqu() , width = 5, font = ("Times New Roman", 14))
    btnSqr.grid(row = 4, column = 5, pady = 10)

    btnEqu = tk.Button(window, text="=", command=lambda: calculate(), width = 20, font = ("Times New Roman", 14))
    btnEqu.grid(row=4, column = 1, columnspan=2, pady = 10)

    window.mainloop()