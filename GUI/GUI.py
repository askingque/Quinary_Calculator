import tkinter as tk
from logic import logic

global fieldText
global symbol
global num1
global num2
global quin
global equals

fieldText = ""
symbol = ""
num1 = ""
num2 = ""
quin = True
equals = False

def run():
    def addToField(sth):
        global fieldText
        field.config(state='normal')
        fieldText = fieldText+str(sth)
        field.delete("1.0","end")
        field.insert("1.0", fieldText)
        field.config(state='disabled')

    def calculate():
        global fieldText
        global num1
        global num2
        global symbol
        global equals
        if equals == False:
            result = ""
            num2 = fieldText
            field.delete("1.0","end")
            fieldText = ""
            if(symbol == "+"):
                addToField(logic.add(int(num1), int(num2)))
            elif(symbol == "-"):
                addToField(logic.subtract(int(num1), int(num2)))
            elif(symbol == "/"):
                addToField(logic.divide(int(num1), int(num2)))
            elif(symbol == "*"):
                addToField(str(logic.multiply(int(num1), int(num2))))
            symbol = ""
            equals = True
            num1 = result
        else:
            return

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
        global equals
        if quin == False:
            buttonPressToggle()
        symbol += "+"
        if fieldText == "Cannot divide by zero" or fieldText == "No root":
            fieldText = "0"
        num1 = fieldText
        field.delete("1.0","end")
        fieldText = ""
        equals = False
        

    def buttonPressSub():
        global fieldText
        global num1
        global symbol
        global equals
        if quin == False:
            buttonPressToggle()
        symbol += "-"
        if fieldText == "Cannot divide by zero" or fieldText == "No root":
            fieldText = "0"
        num1 = fieldText
        field.delete("1.0","end")
        fieldText = ""
        equals = False

    def buttonPressDiv():
        global fieldText
        global num1
        global symbol
        global equals
        if quin == False:
            buttonPressToggle()
        symbol += "/"
        if fieldText == "Cannot divide by zero" or fieldText == "No root":
            fieldText = "0"
        num1 = fieldText
        field.delete("1.0","end")
        fieldText = ""
        equals = False

    def buttonPressMult():
        global fieldText
        global num1
        global symbol
        global equals
        if quin == False:
            buttonPressToggle()
        symbol += "*"
        if fieldText == "Cannot divide by zero" or fieldText == "No root":
            fieldText = "0"
        num1 = fieldText
        field.delete("1.0","end")
        fieldText = ""
        equals = False

    def buttonPressSqu():
        global fieldText
        global num1
        if quin == False:
            buttonPressToggle()
        if fieldText == "Cannot divide by zero" or fieldText == "No root":
            fieldText = "0"
        num1 = fieldText
        field.delete("1.0","end")
        fieldText = ""
        addToField(str(logic.square(int(num1))))

    def buttonPressSqrt():
        global fieldText
        global num1
        if quin == False:
            buttonPressToggle()
        if fieldText == "Cannot divide by zero" or fieldText == "No root":
            fieldText = "0"
        num1 = fieldText
        field.delete("1.0","end")
        fieldText = ""
        addToField(str(logic.sqrt(int(num1))))

    def buttonPressToggle():
        global num1
        global fieldText
        global quin
        if fieldText == "" or fieldText == "Cannot divide by zero" or fieldText == "No root":
            return
        num1 = fieldText
        field.delete("1.0","end")
        fieldText = ""
        if quin == True:
            addToField(str(logic.convert_to_decimal(int(num1))))
            quin = False
        elif quin == False:
            addToField(str(logic.convert_to_quinary(int(num1))))
            quin = True
        btnTog.config(text="b5" if quin else "b10")

    global field
    window =  tk.Tk()
    window.title("Quinary Calculator")
    window.geometry("300x280")
    window.resizable(False, False)
    window['background'] = "black"
    field=tk.Text(window, height=2, width=21, font=("Times New Roman", 20))
    field.grid(row=1, column = 1, columnspan=5)
    field.config(state='disabled')

    #Number Buttons
    btn0 = tk.Button(window, text="0", command=lambda: addToField(0), width = 5, height= 2, font = ("Times New Roman", 14))
    btn0.grid(row=2, column = 1, pady = 5)

    btn1 = tk.Button(window, text="1", command=lambda: addToField(1), width = 5, height= 2, font = ("Times New Roman", 14))
    btn1.grid(row=2, column = 2, pady = 5)

    btn2 = tk.Button(window, text="2", command=lambda: addToField(2), width = 5, height= 2, font = ("Times New Roman", 14))
    btn2.grid(row=2, column = 3, pady = 5)

    btn3 = tk.Button(window, text="3", command=lambda: addToField(3), width = 5, height= 2, font = ("Times New Roman", 14))
    btn3.grid(row=2, column = 4, pady = 5)

    btn4 = tk.Button(window, text="4", command=lambda: addToField(4), width = 5, height= 2, font = ("Times New Roman", 14))
    btn4.grid(row=2, column = 5, pady = 5)

    #Operations Buttons
    btnAdd = tk.Button(window, text="+",command=lambda: buttonPressAdd(), width = 5, height= 2, font = ("Times New Roman", 14))
    btnAdd.grid(row=3, column = 1, pady = 5)

    btnSub = tk.Button(window, text="-", command=lambda: buttonPressSub(), width = 5, height= 2, font = ("Times New Roman", 14))
    btnSub.grid(row=3, column = 2, pady = 5)

    btnMult = tk.Button(window, text="x", command=lambda: buttonPressMult(), width = 5, height= 2, font = ("Times New Roman", 14))
    btnMult.grid(row=3, column = 3, pady = 5)

    btnDiv = tk.Button(window, text="/", command=lambda: buttonPressDiv(), width = 5, height= 2, font = ("Times New Roman", 14))
    btnDiv.grid(row=3, column = 4, pady = 5)

    btnClr = tk.Button(window, text="Clear", command=lambda: clear(), width = 5, height= 2, font = ("Times New Roman", 14))
    btnClr.grid(row=3, column = 5, pady = 5)

    btnEqu = tk.Button(window, text="=", command=lambda: calculate(), width = 11, height= 2, font = ("Times New Roman", 14))
    btnEqu.grid(row=4, column = 1, columnspan = 2, pady = 5)

    btnTog = tk.Button(window, text="b5" if quin else "b10", command=lambda: buttonPressToggle() , width = 5, height= 2, font = ("Times New Roman", 14))
    btnTog.grid(row=4, column = 3, pady = 5)

    btnSqrt = tk.Button(window, text="sqrt", command=lambda: buttonPressSqrt(), width = 5, height= 2, font = ("Times New Roman", 14))
    btnSqrt.grid(row=4, column = 4, pady = 5)

    btnSqr = tk.Button(window, text="sqr", command=lambda: buttonPressSqu() , width = 5, height= 2, font = ("Times New Roman", 14))
    btnSqr.grid(row=4, column = 5, pady = 5)

    window.mainloop()
