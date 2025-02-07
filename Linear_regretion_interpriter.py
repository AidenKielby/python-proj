import math
from math import * 
import statistics
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from fractions import Fraction

root = tk.Tk()
root.title('Linear Regretion')
root.iconphoto(False, tk.PhotoImage(file="logo.png"))

path = 'none rn'

findval = ''

root.geometry("800x500")

label = tk.Label(root, text="Linear Regretion Calculator", font=('Arial', 18))
label.pack()

entrylabel = tk.Label(root, text='File Path:', font=('Arial', 12))
entrylabel.place(x=20, y=50)
entry = tk.Entry(root, font=('Arial', 12)) 
entry.place(x=20, y=70)

def get_data():
   global path
   path = entry.get()

button = tk.Button(root, text='Press to save file path', command=get_data)
button.place(x=20, y=100)

xlabel = tk.Label(root, text='X Value Name:', font=('Arial', 12))
xlabel.place(x=210, y=50)
xentry = tk.Entry(root, font=('Arial', 12)) 
xentry.place(x=210, y=70)

def get_data_for_x():
   global xval
   xval = xentry.get()


buttonx = tk.Button(root, text='Press to save X value', command=get_data_for_x)
buttonx.place(x=210, y=100)

ylabel = tk.Label(root, text='Y Value Name:', font=('Arial', 12))
ylabel.place(x=210, y=140)
yentry = tk.Entry(root, font=('Arial', 12)) 
yentry.place(x=210, y=160)


def get_data_for_y():
   global yval
   yval = yentry.get()

buttony = tk.Button(root, text='Press to save Y value', command=get_data_for_y)
buttony.place(x=210, y=190)

valentry = tk.Entry(root, font=('Arial', 12)) 
valentry.place(x=210, y=250)

def get_data_for_the():

   global theval
   theval = valentry.get()


buttonval = tk.Button(root, text='Press to save X value to be inputed', command=get_data_for_the)
buttonval.place(x=210, y=280)
vallable = tk.Label(root, text=f'X Value is:', font=('Arial', 12))
vallable.place(x=210, y=220)

Var = tk.BooleanVar()

def change():
    if Var.get() == False:
        buttonval = tk.Button(root, text='Press to save X value to be inputed    ', command=get_data_for_the)
        buttonval.place(x=210, y=280)
        vallable = tk.Label(root, text=f'X Value is:    ', font=('Arial', 12))
        vallable.place(x=210, y=220)
    elif Var.get() == True:
        buttonval = tk.Button(root, text='Press to save Y value to be inputed    ', command=get_data_for_the)
        buttonval.place(x=210, y=280)
        vallable = tk.Label(root, text=f'Y Value is:    ', font=('Arial', 12))
        vallable.place(x=210, y=220)

check = tk.Checkbutton(root, text="Check this box to find X value instaed of Y", variable=Var, command=change)
check.place(x=210, y=450)



def main_when_done():
    global slope
    global yintercept
    #finding the x and y values and making them into list
    with open((path), 'r') as fp:
        lines = fp.readlines()
        for i in lines:
            if i.find('x = ') != -1:
                xlist = i.split()
                xlist.remove('x')
                xlist.remove('=')
                xlist = [eval(i) for i in xlist]
                xlist = list(xlist[0])
            if i.find('y = ') != -1:
                ylist = i.split()
                ylist.remove('y')
                ylist.remove('=')
                ylist = [eval(i) for i in ylist]
                ylist = list(ylist[0])

    #the mean of x and the mean of y
    xmean = sum(xlist) / len(xlist)
    ymean = sum(ylist) / len(ylist)
    
    addedlistx = []
    addedlisty = []

    addedlistxy = []

    #standard deviation x
    for i in range(len(xlist)):
        xval1 = xlist[i]
        xsub = xval1-xmean
        xsuared = math.pow(xsub, 2)
        addedlistx.append(xsuared)
    sumedx = sum(addedlistx)
    xdiv = sumedx/(len(xlist)-1)
    suarerootx = math.sqrt(xdiv)

    #standard deviation y
    for i in range(len(ylist)):
        yval1 = ylist[i]
        ysub = yval1-ymean
        ysuared = math.pow(ysub, 2)
        addedlisty.append(ysuared)
    sumedy = sum(addedlisty)
    ydiv = sumedy/(len(ylist)-1)
    suarerooty = math.sqrt(ydiv)

    #cooralation cooeficient
    coosum = sum(addedlistx) * sum(addedlisty)
    coosqrt = math.sqrt(coosum)
    
    for i in range(len(xlist)):
        xval1 = xlist[i]
        xsub = xval1-xmean
        yval1 = ylist[i]
        ysub = yval1-ymean
        xysubs = xsub*ysub
        addedlistxy.append(xysubs)
    xysum = sum(addedlistxy)

    correlation_coefficient = xysum/coosqrt

    #slope
    slope = float(correlation_coefficient) * (float(suarerooty)/float(suarerootx))

    #full equation and showing solution
    global fulleq
    if Var.get() == False:
        sx = slope * xmean
        yintercept = ymean - sx
        fulleq = float(theval)*slope + yintercept
        
        eqfrac = Fraction(fulleq).limit_denominator()

        output = tk.Label(root, text=f'The {yval} value for the inputed {xval} value is: {fulleq}                                                      ', font=('Arial', 12))
        output.place(x=300, y=340)

        slopefrac = Fraction(slope).limit_denominator()
        yinterceptfrac = Fraction(yintercept).limit_denominator()

        equation = tk.Label(root, text=f'The equation is: Y = X * {slopefrac} + {yinterceptfrac}                                                           ', font=('Arial', 12))
        equation.place(x=300, y=360)
    elif Var.get() == True:
        sx = slope * xmean
        yintercept = ymean - sx
        fulleq = (float(theval)-yintercept)/slope

        eqfrac = Fraction(fulleq).limit_denominator()

        output = tk.Label(root, text=f'The {xval} value for the inputed {yval} value is: {fulleq}                                                                                       ', font=('Arial', 12))
        output.place(x=300, y=340)

        slopefrac = Fraction(slope).limit_denominator()
        yinterceptfrac = Fraction(yintercept).limit_denominator()

        equation = tk.Label(root, text=f'The equation is: Y = X * {slopefrac} + {yinterceptfrac}                                                                                     ', font=('Arial', 12))
        equation.place(x=300, y=360)
    
#done button
buttondone = tk.Button(root, text='Finished', command=main_when_done)
buttondone.place(x=20, y=350)


root.mainloop()