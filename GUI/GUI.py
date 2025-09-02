import tkinter as tk

fieldText = ""

def addToField(sth):
    global fieldText
    fieldText = fieldText+str(sth)
    field.delete("1.0","end")
    field.insert("1.0", fieldText)

def calculate():
    global fieldText
    result=str(eval(fieldText))
    field.delete("1.0","end")
    field.insert("1.0", result)
    fieldText = ""
    

def clear():
    global fieldText
    fieldText = ""
    field.delete("1.0","end")



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
btn3.grid(row=3, column = 1, pady = 10)

btn4 = tk.Button(window, text="4", command=lambda: addToField(4), width = 5, font = ("Times New Roman", 14))
btn4.grid(row=3, column = 2, pady = 10)

btn5 = tk.Button(window, text="5", command=lambda: addToField(5), width = 5, font = ("Times New Roman", 14))
btn5.grid(row=3, column = 3, pady = 10)

#Operations Buttons

btnDiv = tk.Button(window, text="/", command=lambda: addToField("/"), width = 5, font = ("Times New Roman", 14))
btnDiv.grid(row=2, column = 4, pady = 10)

btnMult = tk.Button(window, text="*", command=lambda: addToField("*"), width = 5, font = ("Times New Roman", 14))
btnMult.grid(row=3, column = 4, pady = 10)

btnAdd = tk.Button(window, text="+", command=lambda: addToField("+"), width = 5, font = ("Times New Roman", 14))
btnAdd.grid(row=4, column = 4, pady = 10)

btnSub = tk.Button(window, text="-", command=lambda: addToField("-"), width = 5, font = ("Times New Roman", 14))
btnSub.grid(row=5, column = 4, pady = 10)

btnClr = tk.Button(window, text="Clear", command=lambda: clear(), width = 5, font = ("Times New Roman", 14))
btnClr.grid(row=4, column = 3, pady = 10)

btnOpenPar = tk.Button(window, text="(", command=lambda: addToField("("), width = 5, font = ("Times New Roman", 14))
btnOpenPar.grid(row=4, column = 1, pady = 10)

btnClosePar = tk.Button(window, text=")", command=lambda: addToField(")"), width = 5, font = ("Times New Roman", 14))
btnClosePar.grid(row=4, column = 2, pady = 10)

btnEqu = tk.Button(window, text="=", command=lambda: calculate(), width = 20, font = ("Times New Roman", 14))
btnEqu.grid(row=5, column = 1, columnspan=3, pady = 10)

window.mainloop()