import tkinter as tk
import re
from logic import core_logic
from math import floor

"""ERROR desc: 
                When going from Decimal to Quinary we get this issue where if we hit operations it reverts the 1st number
                back to Decimal
                
                ISSUE AFFECTS:
                    Division
                    Sqrt
                    Multiplication
                    ...
                    presumably all operations?
                
    STATUS: Resolved
    
    Keep for a bit to see if this issue comes back up?
                """

fieldText = ""

quin = False

def addToField(sth):
    global fieldText
    fieldText = fieldText+str(sth)
    field.delete("1.0","end")
    field.insert("1.0", fieldText)

def calculate():
    global quin
    global fieldText
    result = ""
    if quin:
        tokens = re.findall(r'\d+|\D', fieldText) # regex: raw string that either has a digit or a non-digit, in which case we separate them
        if len(tokens) > 1:
            print(tokens[1])
            if tokens[1] == '*':
                result = str(core_logic.multiply(tokens[0], tokens[2]))
            if tokens[1] == '/': 
                result = str(core_logic.divide(tokens[0], tokens[2]))
            if tokens[1] == '+':
                result = str(core_logic.add(tokens[0], tokens[2]))
            if tokens[1] == '-':
                result = str(core_logic.subtract(tokens[0], tokens[2]))
        else:
            result = fieldText

    else:
        result=str(floor(eval(fieldText))) # Floor handles division, if replaced we get something like 4.0 instead of 4
    field.delete("1.0","end")
    field.insert("1.0", result)
    fieldText = result # Allows continuous operations, could remove if requirements don't demand it?
    

def clear():
    global fieldText
    fieldText = ""
    field.delete("1.0","end")
    
    
def toggle_conversion(): 
    global quin
    global fieldText
    if not fieldText:
        return
    value = int(fieldText)
    if quin:
        new_value = str(core_logic.convert_to_decimal(value))
    else:
        new_value = str(core_logic.convert_to_quinary(value))
        
    # Replace field contents
    field.delete("1.0", "end")
    field.insert("1.0", new_value)
    fieldText = new_value # DON"T TOUCH
    quin = not quin
    
    # Button name change
    btnTog.config(text="Quin" if quin else "Dec")  # update button text
    
def square():
    global quin
    global fieldText
    if quin:
        result = str(core_logic.square(fieldText))
    else:
        result = str(int(fieldText)**2)
        
    # Replace field contents
    field.delete("1.0", "end")
    field.insert("1.0", result)
    fieldText = result # DON"T TOUCH
    
def sqrt():
    global quin
    global fieldText
    if quin:
        result = str(core_logic.sqrt(fieldText))
    else:
        result = str(floor(int(fieldText)**0.5))
        
    # Replace field contents
    field.delete("1.0", "end")
    field.insert("1.0", result)
    fieldText = result # DON"T TOUCH


window =  tk.Tk()
window.geometry("300x300")
window['background'] = "black"
field=tk.Text(window, height=2, width=21, font=("Times New Roman", 20))
field.grid(row=1, column = 1, columnspan=4)


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

btnDiv = tk.Button(window, text="/", command=lambda: addToField("/"), width = 5, font = ("Times New Roman", 14))
btnDiv.grid(row=3, column = 4, pady = 10)

btnMult = tk.Button(window, text="*", command=lambda: addToField("*"), width = 5, font = ("Times New Roman", 14))
btnMult.grid(row=3, column = 3, pady = 10)

btnAdd = tk.Button(window, text="+", command=lambda: addToField("+"), width = 5, font = ("Times New Roman", 14))
btnAdd.grid(row=3, column = 1, pady = 10)

btnSub = tk.Button(window, text="-", command=lambda: addToField("-"), width = 5, font = ("Times New Roman", 14))
btnSub.grid(row=3, column = 2, pady = 10)

btnClr = tk.Button(window, text="Clear", command=lambda: clear(), width = 5, font = ("Times New Roman", 14))
btnClr.grid(row=3, column = 5, pady = 10)

btnTog = tk.Button(window, text=("Quin" if quin else "Dec"), command=lambda: toggle_conversion(), width = 5, font = ("Times New Roman", 14))
btnTog.grid(row=4, column = 1, pady = 10)

btnSqrt = tk.Button(window, text="sqrt", command= lambda: sqrt(), width = 5, font = ("Times New Roman", 14))
btnSqrt.grid(row=4, column = 2, pady = 10)

btnSqr = tk.Button(window, text="sqr", command=lambda: square(), width = 5, font = ("Times New Roman", 14)) 
btnSqr.grid(row = 4, column = 3)

btnEqu = tk.Button(window, text="=", command=lambda: calculate(), width = 20, font = ("Times New Roman", 14))
btnEqu.grid(row=4, column = 4, columnspan=2, pady = 10)

window.mainloop()