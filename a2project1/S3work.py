#Jenny&Laurel
import numpy as np
import matplotlib.pyplot as plt
from tkinter import*
from tkinter.messagebox import showinfo
class AskForEquation():
    def __init__(self):
        self.root=Tk()
        self.root.title('Enter your equation')
        self.l=[[]for i in range(6)]
        self.e=[[]for i in range(6)]
        self.text=[[]for i in range(6)]
        self.translatedText=[[]for i in range(6)]
        self.setVariables(0)
        self.equationInfo1=Label(self.root,text='r=a+b*sin(c*θ) or r=a+b*cos(c*θ), or r=a+b+c*θ,')
        self.equationInfo1.grid(row=0,sticky=W)
        self.equationInfo2=Label(self.root,text='d = "sin" or "cos" or "direct"')
        self.equationInfo2.grid(row=1,sticky=W)
        self.equationInfo3=Label(self.root,text='e*pi ≤ θ ≤ f*pi')
        self.equationInfo3.grid(row=2,sticky=W)
        self.doneButton = Button(self.root,text='Done',command=self.submit)
        self.doneButton.grid(row=9,column=1,sticky=E)
    def setVariables(self,k):
        if k>5:
            return
        self.text[k]=StringVar()
        self.l[k]=Label(self.root,text=chr(97+k))
        self.l[k].grid(row=k+3,sticky=W)
        self.e[k]=Entry(self.root,textvariable=self.text[k])
        self.e[k].grid(row=k+3,column=1,sticky=E)
        self.setVariables(k+1)
    def submit(self):
        if self.text[3].get()=="cos" or self.text[3].get()=="sin" or self.text[3].get()=="direct":
            self.translate()
        else:
            showinfo('Wrong',"Invalid Input")
    def translate(self,k=5):
        if k<0:
            draw(self.translatedText)
            return
        try:self.translatedText[k]=int(self.text[k].get())
        except:self.translatedText[k]=self.text[k].get()
        self.translate(k-1)
        

class draw():
    def __init__(self,x):
        self.ax=plt.subplot(111, projection='polar')
        self.defineEquation(x)
        self.draw()
    def defineEquation(self,x):
        self.theta=np.arange(int(x[4])*np.pi,int(x[5])*np.pi,0.001)
        if x[3]=='cos':
            self.r=x[0]+x[1]*np.cos(x[2]*self.theta)
        if x[3]=='sin':
            self.r=x[0]+x[1]*np.sin(x[2]*self.theta)
        if x[3]=='direct':
            self.r=x[0]+x[1]+x[2]*self.theta
    def draw(self):
        self.ax.plot(self.theta, self.r)
        self.ax.grid(True)
        plt.show()

AskForEquation()
