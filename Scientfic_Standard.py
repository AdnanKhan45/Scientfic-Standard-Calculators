from tkinter import *
import math 
import parser
import tkinter.messagebox

root=Tk()
root.title("Standard Calculator")
root.configure(bg="lavender")
root.resizable(height=FALSE,width=FALSE)
root.geometry("421x448")

calc = Frame(root)
calc.grid()

class Calculator :
    
# Let's initialize fuction.
    
    def __init__(self):
        self.total = 0
        self.current = ""
        self.inputValue = True
        self.checkSum = False
        self.op = ""
        self.result = False
    
    def enterNumber(self, num):
        self.result = False
        firstNum = txtdisplay.get()
        secondNum = str(num)
        if self.inputValue:
            self.current = secondNum
            self.inputValue = False
        else :
            if secondNum == ".":
                if secondNum in firstNum:
                    return
            self.current = firstNum + secondNum
        self.display(self.current)
        
# This is our equal function.
    
    def sumOfTotal(self):
        self.result = True
        self.current = float(self.current)
        if self.checkSum == True:
            self.valid_Function()
        else :
            self.total = float(txtdisplay.get())
    
    def valid_Function(self):
        if self.op == "add" :
            self.total += self.current
        if self.op == "sub" :
            self.total -= self.current
        if self.op == "multi" :
            self.total *= self.current
        if self.op == "divide" :
            self.total /= self.current
        if self.op == "mod" :
            self.total %= self.current
        self.inputValue = True
        self.checkSum = False
        self.display(self.total)
        
    def operation(self, op):
        self.current = float(self.current)
        if self.checkSum:
            self.valid_Function()
        elif not self.result:
            self.total = self.current
            self.inputValue = True
        self.checkSum = True
        self.op = op
        self.result = False
        
    def clearEntry(self): # Clearing entry
        self.result = False
        self.current = ""
        self.display(0)
        self.inputValue = True

    def clear_All_Entry(self):
        self.clearEntry()
        self.total = 0
        
    def display(self, value):
        txtdisplay.delete(0, END)
        txtdisplay.insert(0, value)
        
    #-------------->Scientfic Functions<--------------#
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current) 
        
    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)  
        
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
        
    def log(self):
        self.result = False
        self.current = math.log(float(txtdisplay.get()))
        self.display(self.current)
        
    def log2(self):
        self.result = False
        self.current = math.log2(float(txtdisplay.get()))
        self.display(self.current)
        
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtdisplay.get()))
        self.display(self.current)
    
    def tan(self):
        self.result = False
        self.current = math.tan(float(txtdisplay.get()))
        self.display(self.current)
        
    def tanh(self):
        self.result = False
        self.current = math.tanh(float(txtdisplay.get()))
        self.display(self.current)
    
    def sin(self):
        self.result = False
        self.current = math.sin(float(txtdisplay.get()))
        self.display(self.current)
    
    def sinh(self):
        self.result = False
        self.current = math.sinh(float(txtdisplay.get()))
        self.display(self.current)
        
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtdisplay.get()))
        self.display(self.current)
        
    def cosh(self):
        self.result = False
        self.current = math.cosh(float(txtdisplay.get()))
        self.display(self.current)
        
    def cos(self):
        self.result = False
        self.current = math.cos(float(txtdisplay.get()))
        self.display(self.current)
        
    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtdisplay.get()))
        self.display(self.current)
        
    def mathsPM(self):
        self.result = False
        self.current = -(float(txtdisplay.get()))
        self.display(self.current)
        
    def lgamma(self):
        self.result = False
        self.current = math.gamma(float(txtdisplay.get()))
        self.display(self.current)
        
    def deg(self):
        self.result = False
        self.current = math.degrees(float(txtdisplay.get()))
        self.display(self.current)
        
    def mod(self):
        self.result = False
        self.current = math.modf(float(txtdisplay.get()))
        self.display(self.current)
        
    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtdisplay.get()))
        self.display(self.current)
    
    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtdisplay.get()))
        self.display(self.current)
        
    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtdisplay.get()))
        self.display(self.current)
        
    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtdisplay.get()))
        self.display(self.current)
    
addedValue = Calculator()

txtdisplay = Entry(calc, font=("ariel",20,"bold"), bg="black", width=25,fg="red", justify=CENTER, bd=22)
txtdisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtdisplay.insert(0, "0")

buttonPad = "789456123" #Numbers...
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=10, height=3,bg="lemon chiffon", font=("ariel",11,"bold"), bd=4, text=buttonPad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i] ["command"] = lambda x = buttonPad [i]:addedValue.enterNumber(x) 
        i+=1
        
#-------------------------->Standard Calculator<----------------------------#               
    
buttonClear = Button(calc, text=chr(67), width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",fg="red",command=addedValue.clearEntry).grid(row=1,column=0)

buttonClearAll = Button(calc, text=chr(67) + chr(69), width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",fg="red",command=addedValue.clear_All_Entry).grid(row=1,column=1)

buttonSqrt = Button(calc, text="√", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.squared).grid(row=1,column=2)

buttonAdditon = Button(calc, text="+", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=lambda: addedValue.operation("add")).grid(row=1,column=3)

buttonSubraction = Button(calc, text="-", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=lambda: addedValue.operation("sub")).grid(row=2,column=3)

buttonMultiplication = Button(calc, text="×", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=lambda: addedValue.operation("multi")).grid(row=3,column=3)

buttonDivision = Button(calc, text="÷", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=lambda: addedValue.operation("divide")).grid(row=4,column=3)

buttonZero = Button(calc, text="0", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=lambda: addedValue.enterNumber(0)).grid(row=5,column=0)

buttonDot = Button(calc, text=".", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=lambda: addedValue.enterNumber(".")).grid(row=5,column=1)

buttonPM = Button(calc, text="±", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.mathsPM).grid(row=5,column=2)

buttonEqual = Button(calc, text="=", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="pale green",command=addedValue.sumOfTotal).grid(row=5,column=3)

#---------------------------->Scientfic Calculator<-----------------------------------#

buttonPi = Button(calc, text="π", width=10, height=3, font=("ariel",11,"bold"), bd=4,bg="LightSkyBlue1",
command=addedValue.pi).grid(row=1,column=4)

button_Cos = Button(calc, text="cos", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.cos).grid(row=1,column=5)

buttonTan = Button(calc, text="tan", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.tan).grid(row=1,column=6)

buttonSin = Button(calc, text="sin", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.sin).grid(row=1,column=7)

#------------------------------->2nd Scientfic<--------------------------------#

buttonPi2 = Button(calc, text="2π", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.tau).grid(row=2,column=4)

buttonCosh = Button(calc, text="cosh", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="lemon chiffon",command=addedValue.cosh).grid(row=2,column=5)

buttonTanh = Button(calc, text="tanh", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="lemon chiffon",command=addedValue.tanh).grid(row=2,column=6)

buttonSinh = Button(calc, text="sinh", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="lemon chiffon",command=addedValue.sinh).grid(row=2,column=7)

#-------------------------------->3rd Scientfic<--------------------------------#

buttonLog = Button(calc, text="log", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.log).grid(row=3,column=4)

buttonExp = Button(calc, text="Exp", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="lemon chiffon",command=addedValue.exp).grid(row=3,column=5)

buttonMod = Button(calc, text="Mod", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="lemon chiffon",command=addedValue.mod).grid(row=3,column=6)

buttonE = Button(calc, text="e", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="lemon chiffon",command=addedValue.e).grid(row=3,column=7)

#------------------------------->4th Scientfic<-----------------------------------#

buttonLog2 = Button(calc, text="log2", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.log2).grid(row=4,column=4)

buttonDeg = Button(calc, text="deg", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="lemon chiffon",command=addedValue.deg).grid(row=4,column=5)

buttonAcosh = Button(calc, text="acosh", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="lemon chiffon",command=addedValue.acosh).grid(row=4,column=6)

buttonAsinh = Button(calc, text="asinh", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="lemon chiffon",command=addedValue.asinh).grid(row=4,column=7)

#--------------------------------5th Scientfic<--------------------------------------#

buttonLog10 = Button(calc, text="log10", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.log10).grid(row=5,column=4)

buttonLog1p = Button(calc, text="log1p", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.log1p).grid(row=5,column=5)

buttonExpml = Button(calc, text="expml", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.expm1).grid(row=5,column=6)

buttonGamma = Button(calc, text="lgamma", width=10, height=3, font=("ariel",11,"bold"), bd=4,
bg="LightSkyBlue1",command=addedValue.lgamma).grid(row=5,column=7)

lblDisplay = Label(calc, text="Scientfic Calculator", font=("ariel",30,"bold"), justify=CENTER)
lblDisplay.grid(row=0,column=4,columnspan=4)

#--------------------------->MENU and Fucntions<--------------------------------------#

def Exit():
    Exit = tkinter.messagebox.askyesno("Scientfic Calculator","Are you sure, You want to quit?")
    if Exit > 0:
        root.destroy()
        return
def Scientfic():
    root.title("Scientfic Calculator")
    root.resizable(height=FALSE,width=FALSE)
    root.geometry("838x448")
def Standard():
    root.title("Standard Calculator")
    root.resizable(height=FALSE,width=FALSE)
    root.geometry("421x448")

menuBar = Menu(calc)
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Standard",command=Standard)
fileMenu.add_command(label="Scientfic",command=Scientfic)
fileMenu.add_separator()
fileMenu.add_command(label="Quit",command=Exit)

editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_separator()
editMenu.add_command(label="Paste")

helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="View Help")

root.config(menu=menuBar)

root.mainloop()
