"""
*********************************RCC_GUI_ver1.0*************************************
RCCC_GUI stands for Resistor Colour Code Calculator Graphical User Interface.
This project is now under General Public License.
By using this app you are agreeing the terms and conditions of TRA Softwares LTD.
If you get any bug contact the authority @ email: nmuatasin2005@gmail.com
"""


#This app is python2 and python3 compatible now

"""
The library 'calcResistance' is under the copyright act 2020.
Copyright 2020 Nur Mahmud Ul Alam Tasin

The library 'tkinter' in Python 3 or 'Tkinter' in Python 2 is a library designed and developed by the Python Organization

Making copy of this application may strike the copyright act.
Be careful.


This Application Helps you to detect the resistance of any resistor by just clicking on the colour of the
perticular band.


"""
"""
This whole app is under copyright of TRA Softwares LTD.
Best wishes for users of this app.
"""
"""
This app is featured to Guido van Rossum , the developer of Python Programming Language, for whome I was able to create the app comfortably.
"""
#Last edited on 21 Febuary 2020.

import calcResistance
try:
	import tkinter.messagebox
	from tkinter import *
	from tkinter import ttk
	global mbox
	mbox=tkinter.messagebox
except ImportError:
	import tkMessageBox
	from Tkinter import *
	import ttk
	mbox=tkMessageBox
class Resistor:

    def __init__(self,root):
        self.root = root
        self.root.title("RCCC by Tasin")
        self.root.geometry("1332x652+0+0")
        self.root.configure(background="light green")

        #----------------------vars--------------------
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=StringVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)

        #----------------------Functions----------------
        def Band1_Black():
            var1.set(0)
        def Band1_Brown():
            var1.set(1)
        def Band1_Red():
            var1.set(2)
        def Band1_Orange():
            var1.set(3)
        def Band1_Yellow():
            var1.set(4)
        def Band1_Green():
            var1.set(5)
        def Band1_Blue():
            var1.set(6)
        def Band1_Violet():
            var1.set(7)
        def Band1_Gray():
            var1.set(8)
        def Band1_White():
            var1.set(9)
        #-----------------------Second band func--------------------------

        def Band2_Black():
            var2.set(0)
        def Band2_Brown():
            var2.set(1)
        def Band2_Red():
            var2.set(2)
        def Band2_Orange():
            var2.set(3)
        def Band2_Yellow():
            var2.set(4)
        def Band2_Green():
            var2.set(5)
        def Band2_Blue():
            var2.set(6)
        def Band2_Violet():
            var2.set(7)
        def Band2_Gray():
            var2.set(8)
        def Band2_White():
            var2.set(9)

        #-----------------------Multiplier band func--------------------------

        def Multiplier_Black():
            var3.set(1)
        def Multiplier_Brown():
            var3.set(10)
        def Multiplier_Red():
            var3.set(100)
        def Multiplier_Orange():
            var3.set(1000)
        def Multiplier_Yellow():
            var3.set(10000)
        def Multiplier_Green():
            var3.set(100000)
        def Multiplier_Blue():
            var3.set(1000000)
        def Multiplier_Violet():
            var3.set(10000000)
        def Multiplier_Gray():
            var3.set(100000000)
        def Multiplier_White():
            var3.set(1000000000)
        def Multiplier_Gold():
            var3.set(0.1)
        def Multiplier_Silver():
            var3.set(0.01)

        #-----------------------Tolerance band func--------------------------

        def Tolerance_Brown():
            var4.set(0.02)
        def Tolerance_Gold():
            var4.set(0.05)
        def Tolerance_Silver():
            var4.set(0.1)
        def Tolerance_None():
            var4.set(0.2)

        #-----------------------Exit_Func---------------

        def iExit():
            iExit= mbox.askyesno("RCCC","Do you want to exit?")
            if iExit>0:
                root.destroy()
                return
        #------------------------Reset_Func--------------------
        def iReset():
            iReset=mbox.askyesno("RCCC","Do you want to reset?")
            if iReset>0:
                var1.set(0)
                var2.set(0)
                var3.set(0)
                var4.set(0)
                var5.set(0)
                var6.set(0)
                var7.set(0)
                var8.set(0)
                var9.set(0)
                return

        def CalculateResistor():
            (ohm,ohmMax,ohmMin,devide)=calcResistance.calcRes(self.txtFirst.get(),self.txtSecond.get(),self.txtMultiplier.get(),self.txtTolerance.get())
            var5.set(devide)
            var6.set(ohm)
            var7.set(ohmMin)
            var8.set(ohmMax)
            
            

        

        
        mainFrame=Frame(self.root,bg='light green')
        mainFrame.grid()


        TitleFrame = Frame(mainFrame, bd=10, width=1350,padx=20,bg='light green',relief = RIDGE)
        TitleFrame.grid(row=0,column=0,columnspan=2)
        self.lblTitle = Label(TitleFrame ,bg='light green' , font=('arial',50,'bold'),text="Resistor Colour Code Calculator",padx=100)
        self.lblTitle.grid()

        ResistorFrame = Frame(mainFrame, bd=10, width=1350,padx=20,bg='light green',relief = RIDGE)
        ResistorFrame.grid(row=1,column=0,sticky=W)

        IndicatorFrame = Frame(mainFrame, bd=10, width=1350,padx=20,bg='light green',relief = RIDGE)
        IndicatorFrame.grid(row=1,column=1,sticky=W)



        self.lblTitle = Label(ResistorFrame ,bg='light green', font=('arial',13,'bold'),text="First Band")
        self.lblTitle.grid(row=0,column=0,pady=20)
        
        self.lblTitle = Label(ResistorFrame ,bg='light green', font=('arial',13,'bold'),text="Second Band")
        self.lblTitle.grid(row=0,column=1,pady=20)

        self.lblTitle = Label(ResistorFrame ,bg='light green', font=('arial',13,'bold'),text="Multiplier")
        self.lblTitle.grid(row=0,column=2,pady=20)

        self.lblTitle = Label(ResistorFrame ,bg='light green', font=('arial',13,'bold'),text="Tolerance")
        self.lblTitle.grid(row=0,column=3,pady=20)

        self.black1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Black',fg='white',
                           command=Band1_Black,bg='black')
        self.black1.grid(row=1,column=0)
        self.black2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='0',fg='white',
                           command=Band2_Black,bg='black')
        self.black2.grid(row=1,column=1)
        self.black3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='1',fg='white',
                           command=Multiplier_Black,bg='black')
        self.black3.grid(row=1,column=2)
        self.black4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),fg='white',bg='black')
        self.black4.grid(row=1,column=3)


        #-------------------------------------------------------------------------------


        self.brown1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Brown',fg='white',
                           command=Band1_Brown,bg='brown')
        self.brown1.grid(row=2,column=0)
        self.brown2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='1',fg='white',
                           command=Band2_Brown,bg='brown')
        self.brown2.grid(row=2,column=1)
        self.brown3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='10',fg='white',
                           command=Multiplier_Brown,bg='brown')
        self.brown3.grid(row=2,column=2)
        self.brown4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='2%',fg='white',
                           command=Tolerance_Brown,bg='brown')
        self.brown4.grid(row=2,column=3)


        #-------------------------------------------------------------------------------


        self.red1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Red',fg='white',
                         command=Band1_Red,bg='red')
        self.red1.grid(row=3,column=0)
        self.red2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='2',fg='white',
                         command=Band2_Red,bg='red')
        self.red2.grid(row=3,column=1)
        self.red3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='100',fg='white',
                         command=Multiplier_Red,bg='red')
        self.red3.grid(row=3,column=2)
        self.red4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),fg='white',bg='red')
        self.red4.grid(row=3,column=3)
        

        #---------------------------------------------------------------------------------------


        self.orange1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Orange',fg='white',
                            command=Band1_Orange,bg='orange')
        self.orange1.grid(row=4,column=0)
        self.orange2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='3',fg='white',
                            command=Band2_Orange,bg='orange')
        self.orange2.grid(row=4,column=1)
        self.orange3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='1000',fg='white',
                            command=Multiplier_Orange,bg='orange')
        self.orange3.grid(row=4,column=2)
        self.orange4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),fg='white',bg='orange')
        self.orange4.grid(row=4,column=3)


        #-------------------------------------------------------------------------------------------

        self.yellow1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Yellow',fg='white',
                            command=Band1_Yellow,bg='yellow')
        self.yellow1.grid(row=5,column=0)
        self.yellow2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='4',fg='white',
                            command=Band2_Yellow,bg='yellow')
        self.yellow2.grid(row=5,column=1)
        self.yellow3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='10000',fg='white',
                            command=Multiplier_Yellow,bg='yellow')
        self.yellow3.grid(row=5,column=2)
        self.yellow4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),fg='white',bg='yellow')
        self.yellow4.grid(row=5,column=3)

        #-----------------------------------------------------------------------------------------------

        self.green1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Green',fg='white',
                           command=Band1_Green,bg='green')
        self.green1.grid(row=6,column=0)
        self.green2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='5',fg='white',
                           command=Band2_Green,bg='green')
        self.green2.grid(row=6,column=1)
        self.green3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='100000',fg='white',
                           command=Multiplier_Green,bg='green')
        self.green3.grid(row=6,column=2)
        self.green4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),fg='white',bg='green')
        self.green4.grid(row=6,column=3)

        #-------------------------------------------------------------------------------------------------------

        self.blue1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Blue',fg='white',
                          command=Band1_Blue,bg='blue')
        self.blue1.grid(row=7,column=0)
        self.blue2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='6',fg='white',
                          command=Band2_Blue,bg='blue')
        self.blue2.grid(row=7,column=1)
        self.blue3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='1000000',fg='white',
                          command=Multiplier_Blue,bg='blue')
        self.blue3.grid(row=7,column=2)
        self.blue4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),fg='white',bg='blue')
        self.blue4.grid(row=7,column=3)

        #------------------------------------------------------------------------------------------------------

        self.violet1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Violet',fg='white',
                            command=Band1_Violet,bg='violet')
        self.violet1.grid(row=8,column=0)
        self.violet2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='7',fg='white',
                            command=Band2_Violet,bg='violet')
        self.violet2.grid(row=8,column=1)
        self.violet3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='10000000',fg='white',
                            command=Multiplier_Violet,bg='violet')
        self.violet3.grid(row=8,column=2)
        self.violet4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),fg='white',bg='violet')
        self.violet4.grid(row=8,column=3)

        #-------------------------------------------------------------------------------------------------------

        self.gray1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Gray',fg='white',
                          command=Band1_Gray,bg='gray')
        self.gray1.grid(row=9,column=0)
        self.gray2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='8',fg='white',
                          command=Band2_Gray,bg='gray')
        self.gray2.grid(row=9,column=1)
        self.gray3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='100000000',fg='white',
                          command=Multiplier_Gray,bg='gray')
        self.gray3.grid(row=9,column=2)
        self.gray4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),fg='white',bg='gray')
        self.gray4.grid(row=9,column=3)

        #-----------------------------------------------------------------------------------------------------

        self.white1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='White',fg='black',
                           command=Band1_White,bg='white')
        self.white1.grid(row=10,column=0)
        self.white2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='9',fg='black',
                           command=Band2_White,bg='white')
        self.white2.grid(row=10,column=1)
        self.white3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='1000000000',fg='black',
                           command=Multiplier_White,bg='white')
        self.white3.grid(row=10,column=2)
        self.white4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),fg='black',bg='white')
        self.white4.grid(row=10,column=3)

        #-------------------------------------------------------------------------------------------------------

        self.gold1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Gold',fg='white',bg='gold')
        self.gold1.grid(row=11,column=0)
        self.gold2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='',fg='white',bg='gold')
        self.gold2.grid(row=11,column=1)
        self.gold3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='0.1',fg='white',
                          command=Multiplier_Gold,bg='gold')
        self.gold3.grid(row=11,column=2)
        self.gold4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='5%',fg='white',
                          command=Tolerance_Gold, bg='gold')
        self.gold4.grid(row=11,column=3)

        #-------------------------------------------------------------------------------------------------------

        self.silver1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='Silver',fg='white',bg='silver')
        self.silver1.grid(row=12,column=0)
        self.silver2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='',fg='white',bg='silver')
        self.silver2.grid(row=12,column=1)
        self.silver3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='0.01',fg='white',
                            command=Multiplier_Silver,bg='silver')
        self.silver3.grid(row=12,column=2)
        self.silver4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='10%',fg='white',
                            command=Tolerance_Silver,bg='silver')
        self.silver4.grid(row=12,column=3)

        #---------------------------------------------------------------------------------------------------------

        self.none1=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='None',fg='black',bg='white')
        self.none1.grid(row=13,column=0)
        self.none2=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='',fg='white',bg='white')
        self.none2.grid(row=13,column=1)
        self.none3=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='',fg='white',bg='white')
        self.none3.grid(row=13,column=2)
        self.none4=Button(ResistorFrame, width = 13,font=('arial',14,'bold'),text='20%',fg='black',
                          command=Tolerance_None,bg='white')
        self.none4.grid(row=13,column=3)

        #-------------------------------------Indicator Frame---------------------------------------------

        self.lblFirst = Label(IndicatorFrame , bg='light green',font=('arial',13,'bold'),text="First Band")
        self.lblFirst.grid(row=0,column=0,sticky=W,pady=10,padx=75)

        self.txtFirst=Entry(IndicatorFrame , font=('arial',13,'bold'),width=24,textvariable=var1)
        self.txtFirst.grid(row=0,column=1,pady=10,columnspan=3,padx=4)
        
        self.lblSecond = Label(IndicatorFrame ,bg='light green', font=('arial',13,'bold'),text="Second Band")
        self.lblSecond.grid(row=1,column=0,sticky=W,pady=10,padx=75)
        
        self.txtSecond=Entry(IndicatorFrame , font=('arial',13,'bold'),width=24,textvariable=var2)
        self.txtSecond.grid(row=1,column=1,pady=10,columnspan=3,padx=4)

        self.lblMultiplier = Label(IndicatorFrame ,bg='light green', font=('arial',13,'bold'),text="Multiplier")
        self.lblMultiplier.grid(row=2,column=0,sticky=W,pady=10,padx=75)

        self.txtMultiplier=Entry(IndicatorFrame , font=('arial',13,'bold'),width=24,textvariable=var3)
        self.txtMultiplier.grid(row=2,column=1,pady=10,columnspan=3,padx=4)

        self.lblTolerance = Label(IndicatorFrame ,bg='light green' , font=('arial',13,'bold'),text="Tolerance")
        self.lblTolerance.grid(row=3,column=0,sticky=W,pady=10,padx=75)

        self.txtTolerance=Entry(IndicatorFrame , font=('arial',13,'bold'),width=24,textvariable=var4)
        self.txtTolerance.grid(row=3,column=1,pady=10,columnspan=3,padx=4)
        
        self.lblDivideBy1000 = Label(IndicatorFrame ,bg='light green', font=('arial',13,'bold'),text="Divide By 1000")
        self.lblDivideBy1000.grid(row=4,column=0,sticky=W,pady=10,padx=75)
        
        self.txtDivideBy1000=Entry(IndicatorFrame , font=('arial',13,'bold'),width=24,textvariable=var5)
        self.txtDivideBy1000.grid(row=4,column=1,pady=10,columnspan=3,padx=4)

        
        self.lblResistorValue = Label(IndicatorFrame ,bg='light green' , font=('arial',13,'bold'),text="Resistor Value")
        self.lblResistorValue.grid(row=5,column=0,sticky=W,pady=10,padx=75)
        
        self.txtResistorValue=Entry(IndicatorFrame , font=('arial',13,'bold'),width=24,textvariable=var6)
        self.txtResistorValue.grid(row=5,column=1,pady=10,columnspan=3,padx=4)

        self.lblMinRange = Label(IndicatorFrame ,bg='light green' , font=('arial',13,'bold'),text="Minimum Value")
        self.lblMinRange.grid(row=6,column=0,sticky=W,pady=10,padx=75)

        self.txtMinRange=Entry(IndicatorFrame , font=('arial',13,'bold'),width=24,textvariable=var7)
        self.txtMinRange.grid(row=6,column=1,pady=10,columnspan=3,padx=4)
        
        self.lblMaxRange = Label(IndicatorFrame ,bg='light green' , font=('arial',13,'bold'),text="Maximum Value")
        self.lblMaxRange.grid(row=7,column=0,sticky=W,pady=10,padx=75)
        
        self.txtMaxRange=Entry(IndicatorFrame , font=('arial',13,'bold'),width=24,textvariable=var8)
        self.txtMaxRange.grid(row=7,column=1,pady=10,columnspan=3,padx=4)

        #=------------------------Buttons---------------------------------

        btnCalculate=Button(IndicatorFrame , font=('arial',13,'bold'),text="Calculate",width=8,height=3,command=CalculateResistor)
        btnCalculate.grid(row=8,column=0,pady=10)
        btnReset=Button(IndicatorFrame , font=('arial',13,'bold'),text="Reset",width=8,height=3,command=iReset)
        btnReset.grid(row=8,column=1,pady=10)
        btnExit=Button(IndicatorFrame , font=('arial',13,'bold'),text="Exit",width=8,height=3,command=iExit)
        btnExit.grid(row=8,column=3,pady=10)
        self.lblCredit = Label(IndicatorFrame ,bg='light green' , font=('arial',9,'bold'),text="Created by Nur Mahmud Ul Alam \n[Feat. Guido van Rossum] ")
        self.lblCredit.grid(row=9,column=0,sticky=W,pady=2)
        self.lblCredit = Label(IndicatorFrame ,bg='light green' , font=('arial',9,'bold'),text="Version 1.0")
        self.lblCredit.grid(row=10,column=0,sticky=W,pady=2)
        


if __name__=='__main__':
    root = Tk()
    application = Resistor(root)
    root.mainloop()
