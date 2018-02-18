#Jenny&Laurel
import numpy as np
import matplotlib.pyplot as plt
from tkinter import*
from tkinter.messagebox import showerror
from matplotlib.ticker import MultipleLocator
class AskForEquation():
    def __init__(self):
        self.modeAsking()
    def modeAsking(self):
        self.root=Tk()
        MODES = [
            ('sin','sin'),
            ('cos','cos'),
            ('direct','direct')]
        self.v = StringVar()
        self.v.set('sin')
        for mode,num in MODES:
            m = Radiobutton(self.root,text=mode,variable=self.v,value=num)
            m.pack(anchor=W)    
        Button(self.root,text='Next',command=self.root.destroy).pack(anchor=W)
        mainloop()
        self.mainFrameSetUp()
    def mainFrameSetUp(self):
        self.root=Tk()
        self.root.title('Enter Your Equation')
        self.coefficientsAsking()
    def coefficientsAsking(self):
        self.mode=self.v.get()
        if self.mode=='direct':
            self.text=[IntVar()for i in range(4)]
            self.translatedText=[[]for i in range(4)]
            Label(self.root,text=' r').grid(row=0,column=0)
            Label(self.root,text=' = ').grid(row=0,column=1)
            Entry(self.root,textvariable=self.text[0],width=4).grid(row=0,column=2)
            Label(self.root,text=' + ').grid(row=0,column=3)
            Entry(self.root,textvariable=self.text[1],width=4).grid(row=0,column=4)
            Label(self.root,text='θ').grid(row=0,column=5,sticky=W)
            Label(self.root,text='(').grid(row=1,column=0,sticky=E)
            Entry(self.root,textvariable=self.text[2],width=4).grid(row=1,column=1)
            Label(self.root,text='π ≤').grid(row=1,column=2)
            Label(self.root,text=' θ ≤').grid(row=1,column=3)
            Entry(self.root,textvariable=self.text[3],width=4).grid(row=1,column=4)
            Label(self.root,text='π)').grid(row=1,column=5,sticky=W)
            Button(self.root,text='Next',command=self.translate,height=2).grid(row=0,column=8,rowspan=2,sticky=E)

        else:         
            self.text=[StringVar()for i in range(5)]
            self.translatedText=[[]for i in range(5)]
            Label(self.root,text=' r').grid(row=0,column=0)
            Label(self.root,text=' = ').grid(row=0,column=1)
            Entry(self.root,textvariable=self.text[0],width=4).grid(row=0,column=2)
            Label(self.root,text=' + ').grid(row=0,column=3)
            Entry(self.root,textvariable=self.text[1],width=4).grid(row=0,column=4)
            Label(self.root,text=' × '+self.mode).grid(row=0,column=5)
            Entry(self.root,textvariable=self.text[2],width=4).grid(row=0,column=6)
            Label(self.root,text='θ').grid(row=0,column=7)
            Label(self.root,text='(').grid(row=1,column=0,sticky=E)
            Entry(self.root,textvariable=self.text[3],width=4).grid(row=1,column=1)
            Label(self.root,text='π ≤').grid(row=1,column=2)
            Label(self.root,text=' θ ≤').grid(row=1,column=3)
            Entry(self.root,textvariable=self.text[4],width=4).grid(row=1,column=4)
            Label(self.root,text='π)').grid(row=1,column=5,sticky=W)
            Button(self.root,text='Next',command=self.translate,height=2).grid(row=0,column=8,rowspan=2,sticky=E)
    def translate(self):
        i=len(self.text)-1
        Error=False
        while i!=-1 and not Error:
            try:       
                self.translatedText[i]=float(self.text[i].get())
                i-=1
            except:
                Error=True
        if Error or (None in self.translatedText):
            showerror('error','Please Enter Numbers')
            self.coefficientsAsking()
        elif self.translatedText[-1]<=self.translatedText[-2]:
            showerror('error','Please Enter Valid Domain')
            self.coefficientsAsking()
        else:
            ploting(self.translatedText,self.mode)


class ploting():
    def __init__(self,coefficientList,mode):
        self.defineEquation(coefficientList,mode)
        self.draw()
    def defineEquation(self,coefficientList,mode):
        self.theta=np.arange(coefficientList[-2]*np.pi,coefficientList[-1]*np.pi,0.001)
        self.tableK=np.arange(coefficientList[-2],coefficientList[-1],(coefficientList[-1]-coefficientList[-2])/6)#kπ
        if mode=='cos':
            self.r=coefficientList[0]+coefficientList[1]*np.cos(coefficientList[2]*self.theta)
            self.tableR=coefficientList[0]+coefficientList[1]*np.cos(coefficientList[2]*self.tableK*np.pi)
            #self.formula='$r='+str(coefficientList[0])+str(coefficientList[1])+'\times cos'+str(coefficientList[2])+'\timesθ$'
        if mode=='sin':
            self.r=coefficientList[0]+coefficientList[1]*np.sin(coefficientList[2]*self.theta)
            self.tableR=coefficientList[0]+coefficientList[1]*np.sin(coefficientList[2]*self.tableK*np.pi)
            #self.formula='$r='+str(coefficientList[0])+str(coefficientList[1])+'\times sin'+str(coefficientList[2])+'\timesθ$'
        if mode=='direct':
            self.r=coefficientList[0]+coefficientList[1]*self.theta
            self.tableR=coefficientList[0]+coefficientList[1]*self.tableK*np.pi
            #self.formula='$r='+str(coefficientList[0])+str(coefficientList[1])+'\timesθ$'
        self.x=self.r*np.cos(self.theta)
        self.y=self.r*np.sin(self.theta)
    def draw(self):
        #Polar
        self.polar=plt.subplot(221, projection='polar')
        plt.plot(self.theta,self.r)
        self.polar.grid(True)
        #Cartesian
        self.cart=plt.subplot(222)
        plt.plot(self.x,self.y)
        self.cart.grid(True)
        self.cart.spines['bottom'].set_position(('data', 0))  
        self.cart.spines['left'].set_position(('data',0))
        self.cart.xaxis.set_minor_locator(MultipleLocator(0.5))
        self.cart.yaxis.set_minor_locator(MultipleLocator(0.5))
        #Table
        self.table=plt.subplot(212)
        self.firstRow=['θ :']
        self.secondRow=['r :']
        self.xp=[0.3,1.3,2.3,3.3,4.3,5.3,6.3]
        for i in self.tableK:
            self.firstRow.append(str(round(i,2))+'π')
        for i in self.tableR:
            self.secondRow.append(str(round(i,2)))
        for i, num in enumerate(self.firstRow):
            plt.text(self.xp[i],1.5,num)
        for i, num in enumerate(self.secondRow):
            plt.text(self.xp[i],0.5,num)
        self.table.grid(True,which='minor')
        self.table.xaxis.set_minor_locator(MultipleLocator(1))
        self.table.set_xticks([])
        self.table.yaxis.set_minor_locator(MultipleLocator(1))
        self.table.set_yticks([])
        plt.axis([0,7,0,2])
        plt.show()
        
if __name__=='__main__':
    AskForEquation()
