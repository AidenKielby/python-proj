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

zlabel = tk.Label(root, text='Z Value Name:', font=('Arial', 12))
zlabel.place(x=410, y=50)
zentry = tk.Entry(root, font=('Arial', 12)) 
zentry.place(x=410, y=70)

def get_data_for_z():
   global zval
   zval = zentry.get()


buttonz = tk.Button(root, text='Press to save Z value', command=get_data_for_z)
buttonz.place(x=410, y=100)

ylabel = tk.Label(root, text='Y Value Name:', font=('Arial', 12))
ylabel.place(x=210, y=140)
yentry = tk.Entry(root, font=('Arial', 12)) 
yentry.place(x=210, y=160)


def get_data_for_y():
   global yval
   yval = yentry.get()

buttony = tk.Button(root, text='Press to save Y value', command=get_data_for_y)
buttony.place(x=210, y=190)

valentryx = tk.Entry(root, font=('Arial', 12)) 
valentryx.place(x=210, y=250)

def get_data_for_thex():

   global thevalx
   thevalx = valentryx.get()


buttonval = tk.Button(root, text='Press to save X value to be inputed', command=get_data_for_thex)
buttonval.place(x=210, y=280)
vallable = tk.Label(root, text=f'X Value is:', font=('Arial', 12))
vallable.place(x=210, y=220)

valentryz = tk.Entry(root, font=('Arial', 12)) 
valentryz.place(x=410, y=250)

def get_data_for_thez():

   global thevalz
   thevalz = valentryz.get()


buttonval = tk.Button(root, text='Press to save Z value to be inputed', command=get_data_for_thez)
buttonval.place(x=410, y=280)
vallable = tk.Label(root, text=f'Z Value is:', font=('Arial', 12))
vallable.place(x=410, y=220)

Var = tk.BooleanVar()

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
            if i.find('z = ') != -1:
                zlist = i.split()
                zlist.remove('z')
                zlist.remove('=')
                zlist = [eval(i) for i in zlist]
                zlist = list(zlist[0])

    #the mean of x and the mean of y
    xmean = sum(xlist) / len(xlist)
    ymean = sum(ylist) / len(ylist)
    zmean = sum(zlist) / len(zlist)
    
    addedlistx = []
    addedlisty = []
    addedlistz = []

    addedlistxy = []
    addedlistzy = []

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

    for i in range(len(zlist)):
        zval1 = zlist[i]
        zsub = zval1-zmean
        zsuared = math.pow(zsub, 2)
        addedlistz.append(zsuared)
    sumedz = sum(addedlistz)
    zdiv = sumedz/(len(zlist)-1)
    suarerootz = math.sqrt(zdiv)

    #cooralation cooeficient for x
    coosumx = sum(addedlistx) * sum(addedlisty)
    coosqrtx = math.sqrt(coosumx)
    
    for i in range(len(xlist)):
        xval1 = xlist[i]
        xsub = xval1-xmean
        yval1 = ylist[i]
        ysub = yval1-ymean
        xysubs = xsub*ysub
        addedlistxy.append(xysubs)
    xysum = sum(addedlistxy)

    correlation_coefficientx = xysum/coosqrtx

    #slope
    slopex = float(correlation_coefficientx) * (float(suarerooty)/float(suarerootx))

    coosumz = sum(addedlistz) * sum(addedlisty)
    coosqrtz = math.sqrt(coosumz)

    for i in range(len(zlist)):
        zval1 = zlist[i]
        zsub = zval1-zmean
        yval1 = ylist[i]
        ysub = yval1-ymean
        zysubs = zsub*ysub
        addedlistzy.append(zysubs)
    zysum = sum(addedlistzy)

    correlation_coefficientz = zysum/coosqrtz

    slopez = float(correlation_coefficientz) * (float(suarerooty)/float(suarerootz))

    #full equation and showing solution
    global fulleq
    if Var.get() == False:
        sx = slopex * xmean
        yintercept = ymean - sx
        fulleq = (float(thevalx)*slopex) + yintercept + (float(thevalz)*slopez)
        
        eqfrac = Fraction(fulleq).limit_denominator()

        output = tk.Label(root, text=f'The {yval} value for the inputed {xval} and {zval} value is: {fulleq}                                                      ', font=('Arial', 12))
        output.place(x=200, y=340)

        slopefracz = Fraction(slopez).limit_denominator()
        slopefracx = Fraction(slopex).limit_denominator()
        yinterceptfrac = Fraction(yintercept).limit_denominator()

        equation = tk.Label(root, text=f'The equation is: Y = X * {slopefracx} + {yinterceptfrac} + z * {slopefracz}                                                          ', font=('Arial', 12))
        equation.place(x=200, y=360)
    
#done button
buttondone = tk.Button(root, text='Finished', command=main_when_done)
buttondone.place(x=20, y=350)


root.mainloop()