from Tkinter import *
from tkMessageBox import *
import random
import time;
import datetime

root=Tk()
#================================page1=================================================
def enter():
    root1=Toplevel(root)
#================================page2=================================================
    def nextpage():
        root1=Toplevel(root)
        root1.geometry("1350x750+0+0")
        root1.attributes('-fullscreen',True)
        root1.title("PAGE 1")
        root.configure(background="black")

        f1=Frame(root1,width=1350,height=100,bd=14,relief="raise")
        f1.pack(side=TOP,fill="both",expand="yes")

        f2=Frame(root1,width=900,height=650,bd=8,relief="raise")
        f2.pack(side=LEFT,fill="both",expand="yes")

        f3=Frame(root1,width=440,height=650,bd=8,relief="raise")
        f3.pack(side=RIGHT,fill="both",expand="yes")

        f2a=Frame(f2,width=900,height=330,bd=8,relief="raise")
        f2a.pack(side=TOP,fill="both",expand="yes")
        f2b=Frame(f2,width=900,height=320,bd=6,relief="raise")
        f2b.pack(side=BOTTOM,fill="both",expand="yes")

        f3a=Frame(f3,width=440,height=450,bd=12,relief="raise")
        f3a.pack(side=TOP,fill="both",expand="yes")
        f3b=Frame(f3,width=440,height=250,bd=12,relief="raise")
        f3b.pack(side=BOTTOM,fill="both",expand="yes")

        f2aa=Frame(f2a,width=400,height=330,bd=16,relief="raise")
        f2aa.pack(side=LEFT,fill="both",expand="yes")
        f2bb=Frame(f2a,width=400,height=330,bd=16,relief="raise")
        f2bb.pack(side=RIGHT,fill="both",expand="yes")

        f2aa1=Frame(f2b,width=450,height=330,bd=14,relief="raise")
        f2aa1.pack(side=LEFT,fill="both",expand="yes")
        f2bb1=Frame(f2b,width=450,height=330,bd=14,relief="raise")
        f2bb1.pack(side=RIGHT,fill="both",expand="yes")

        f1.configure(background="black")
        f2.configure(background="black")
        f3.configure(background="black")

        a=IntVar()
        a1=IntVar()
        a2=IntVar()
        a3=IntVar()
        a4=IntVar()
        a5=IntVar()
        a6=IntVar()
        a7=IntVar()
        a8=IntVar()
        a9=IntVar()
        a10=IntVar()
        a11=IntVar()
        a12=IntVar()
        a13=IntVar()
        a14=IntVar()
        a15=IntVar()
        a16=IntVar()
        a17=IntVar()
        a18=IntVar()
        a19=IntVar()
        
        d1=StringVar()
        d2=StringVar()
        d3=StringVar()
        d4=StringVar()
        d5=StringVar()
        d6=StringVar()
        d7=StringVar()
        d8=StringVar()
        d9=StringVar()
        d10=StringVar()
        d11=StringVar()
        d12=StringVar()
        d13=StringVar()
        d14=StringVar()
        d15=StringVar()
        d16=StringVar()
        d17=StringVar()
        d18=StringVar()
        d19=StringVar()
        d20=StringVar()

        def click():
            if a.get()==1:
                e1.configure(state=NORMAL)
            elif a.get()==0:
                e1.configure(state=DISABLED)
            if a1.get()==2:
                e2.configure(state=NORMAL)
            elif a1.get()==0:
                e2.configure(state=DISABLED)
            if a2.get()==3:
                e3.configure(state=NORMAL)
            elif a2.get()==0:
                e3.configure(state=DISABLED)
            if a3.get()==4:
                e4.configure(state=NORMAL)
            elif a3.get()==0:
                e4.configure(state=DISABLED)
            if a4.get()==5:
                e5.configure(state=NORMAL)
            elif a4.get()==0:
                e5.configure(state=DISABLED)
            if a5.get()==6:
                e6.configure(state=NORMAL)
            elif a5.get()==0:
                e6.configure(state=DISABLED)
            if a6.get()==7:
                e7.configure(state=NORMAL)
            elif a6.get()==0:
                e7.configure(state=DISABLED)
            if a7.get()==8: 
                e8.configure(state=NORMAL)
            elif a7.get()==0:
                e8.configure(state=DISABLED)
            if a8.get()==9:
                e9.configure(state=NORMAL)
            elif a8.get()==0:
                e9.configure(state=DISABLED)
            if a9.get()==10:
                e10.configure(state=NORMAL)
            elif a9.get()==0:
                e10.configure(state=DISABLED)
            if a10.get()==11:
                f1.configure(state=NORMAL)
            elif a10.get()==0:
                f1.configure(state=DISABLED)
            if a11.get()==12:
                f2.configure(state=NORMAL)
            elif a11.get==0:
                f2.configure(state=DISABLED)
            if a12.get()==13:
                f3.configure(state=NORMAL)
            elif a12.get==0:
                f3.configure(state=DISABLED)
            if a13.get()==14:
                f4.configure(state=NORMAL)
            elif a13.get==0:
                f4.configure(state=DISABLED)
            if a14.get()==15:
                f5.configure(state=NORMAL)
            elif a14.get==0:
                f5.configure(state=DISABLED)
            if a15.get()==16:
                f6.configure(state=NORMAL)
            elif a15.get()==0:
                f6.configure(state=DISABLED)
            if a16.get()==17:
                f7.configure(state=NORMAL)
            elif a16.get()==0:
                f7.configure(state=DISABLED)
            if a17.get()==18:
                f8.configure(state=NORMAL)
            elif a17.get()==0:
                f8.configure(state=DISABLED)
            if a18.get()==19:
                f9.configure(state=NORMAL)
            elif a18.get()==0:
                f9.configure(state=DISABLED)
            if a19.get()==20:
                f10.configure(state=NORMAL)
            elif a19.get()==0:
                f10.configure(state=DISABLED)

        
        Label(f1,text="BAY LEAF RESTAURANT",font="Arial 70 bold").pack(side=TOP,fill="both",expand="yes")
        Label(f2aa,text="BIRIYANI RICE",font="Arial 20 bold").grid(row=0,column=0,sticky=W)
        c1=Checkbutton(f2aa,font="Arial 18 bold",text="Motia Pulao Imtiazi",command=click,variable=a,onvalue=1).grid(row=1,column=0,sticky=W)
        Label(f2aa,font="Arial 18 bold",text="449").grid(row=1,column=4)
        c2=Checkbutton(f2aa,font="Arial 18 bold",text="Dum Ghost Lucknowi Briyani",command=click,variable=a1,onvalue=2).grid(row=2,column=0,sticky=W)
        Label(f2aa,font="Arial 18 bold",text="549").grid(row=2,column=4)
        c3=Checkbutton(f2aa,font="Arial 18 bold",text="Dum Murgh Lucknowi Briyani",command=click,variable=a2,onvalue=3).grid(row=3,column=0,sticky=W)
        Label(f2aa,font="Arial 18 bold",text="549").grid(row=3,column=4)
        c4=Checkbutton(f2aa,font="Arial 18 bold",text="Dum Rice",variable=a3,command=click,onvalue=4).grid(row=4,column=0,sticky=W)
        Label(f2aa,font="Arial 18 bold",text="349").grid(row=4,column=4)
        c5=Checkbutton(f2aa,font="Arial 18 bold",text="Fragrant Basmati rice",command=click,variable=a4,onvalue=5).grid(row=5,column=0,sticky=W)
        Label(f2aa,font="Arial 18 bold",text="349").grid(row=5,column=4)

        Label(f2bb,text="PIZZA",font="Arial 20 bold").grid(row=0,column=0,sticky=W)
        c6=Checkbutton(f2bb,font="Arial 18 bold",text="Margherita",command=click,variable=a5,onvalue=6).grid(row=1,column=0,sticky=W)
        Label(f2bb,font="Arial 18 bold",text="249").grid(row=1,column=4)
        c7=Checkbutton(f2bb,font="Arial 18 bold",text="Primavera",command=click,variable=a6,onvalue=7).grid(row=2,column=0,sticky=W)
        Label(f2bb,font="Arial 18 bold",text="299").grid(row=2,column=4)
        c8=Checkbutton(f2bb,font="Arial 18 bold",text="Tandoori Paneer",command=click,variable=a7,onvalue=8).grid(row=3,column=0,sticky=W)
        Label(f2bb,font="Arial 18 bold",text="299").grid(row=3,column=4)
        c9=Checkbutton(f2bb,font="Arial 18 bold",text="Paneer Vegorama",command=click,variable=a8,onvalue=9).grid(row=4,column=0,sticky=W)
        Label(f2bb,font="Arial 18 bold",text="299").grid(row=4,column=4)
        c10=Checkbutton(f2bb,font="Arial 18 bold",text="Supreme Veggie",command=click,variable=a9,onvalue=10).grid(row=5,column=0,sticky=W)
        Label(f2bb,font="Arial 18 bold",text="299").grid(row=5,column=4)

        Label(f2aa1,text="INDIAN BREADS",font="Arial 20 bold").grid(row=0,column=0,sticky=W)
        Checkbutton(f2aa1,font="Arial 18 bold",text="Kulcha",command=click,variable=a10,onvalue=11).grid(row=1,column=0,sticky=W)
        Label(f2aa1,font="Arial 18 bold",text="149").grid(row=1,column=4)
        Checkbutton(f2aa1,font="Arial 18 bold",text="Naan",command=click,variable=a11,onvalue=12).grid(row=2,column=0,sticky=W)
        Label(f2aa1,font="Arial 18 bold",text="99").grid(row=2,column=4)
        Checkbutton(f2aa1,font="Arial 18 bold",text="Paratha",command=click,variable=a12,onvalue=13).grid(row=3,column=0,sticky=W)
        Label(f2aa1,font="Arial 18 bold",text="99").grid(row=3,column=4)
        Checkbutton(f2aa1,font="Arial 18 bold",text="Roti",command=click,variable=a13,onvalue=14).grid(row=4,column=0,sticky=W)
        Label(f2aa1,font="Arial 18 bold",text="99").grid(row=4,column=4)
        Checkbutton(f2aa1,font="Arial 18 bold",text="Tandoori Roti",command=click,variable=a14,onvalue=15).grid(row=5,column=0,sticky=W)
        Label(f2aa1,font="Arial 18 bold",text="99").grid(row=5,column=4)

        Label(f2bb1,text="ACCOMPANIMENT",font="Arial 20 bold").grid(row=0,column=0,sticky=W)
        Checkbutton(f2bb1,font="Arial 18 bold",text="Lassi",command=click,variable=a15,onvalue=16).grid(row=1,column=0,sticky=W)
        Label(f2bb1,font="Arial 18 bold",text="199").grid(row=1,column=4)
        Checkbutton(f2bb1,font="Arial 18 bold",text="Raita",command=click,variable=a16,onvalue=17).grid(row=2,column=0,sticky=W)
        Label(f2bb1,font="Arial 18 bold",text="149").grid(row=2,column=4)
        Checkbutton(f2bb1,font="Arial 18 bold",text="Peanut Masala",command=click,variable=a17,onvalue=18).grid(row=3,column=0,sticky=W)
        Label(f2bb1,font="Arial 18 bold",text="199").grid(row=3,column=4)
        Checkbutton(f2bb1,font="Arial 18 bold",text="Papad Masala",command=click,variable=a18,onvalue=19).grid(row=4,column=0,sticky=W)
        Label(f2bb1,font="Arial 18 bold",text="99").grid(row=4,column=4)
        Checkbutton(f2bb1,font="Arial 18 bold",text="Papad",command=click,variable=a19,onvalue=20).grid(row=5,column=0,sticky=W)
        Label(f2bb1,font="Arial 18 bold",text="49").grid(row=5,column=4)

        e1=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d1,state=DISABLED)
        e1.grid(row=1,column=1)
        e2=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d2,state=DISABLED)
        e2.grid(row=2,column=1)
        e3=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d3,state=DISABLED)
        e3.grid(row=3,column=1)
        e4=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d4,state=DISABLED)
        e4.grid(row=4,column=1)
        e5=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d5,state=DISABLED)
        e5.grid(row=5,column=1)

        e6=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d6,state=DISABLED)
        e6.grid(row=1,column=1)
        e7=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d7,state=DISABLED)
        e7.grid(row=2,column=1)
        e8=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d8,state=DISABLED)
        e8.grid(row=3,column=1)
        e9=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d9,state=DISABLED)
        e9.grid(row=4,column=1)
        e10=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d10,state=DISABLED)
        e10.grid(row=5,column=1)

        f1=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d11,state=DISABLED)
        f1.grid(row=1,column=1)
        f2=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d12,state=DISABLED)
        f2.grid(row=2,column=1)
        f3=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d13,state=DISABLED)
        f3.grid(row=3,column=1)
        f4=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d14,state=DISABLED)
        f4.grid(row=4,column=1)
        f5=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d15,state=DISABLED)
        f5.grid(row=5,column=1)

        f6=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d16,state=DISABLED)
        f6.grid(row=1,column=1)
        f7=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d17,state=DISABLED)
        f7.grid(row=2,column=1)
        f8=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d18,state=DISABLED)
        f8.grid(row=3,column=1)
        f9=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d19,state=DISABLED)
        f9.grid(row=4,column=1)
        f10=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d20,state=DISABLED)
        f10.grid(row=5,column=1)

        def reset():
            d1.set("0")
            d2.set("0")
            d3.set("0")
            d4.set("0")
            d5.set("0")
            d6.set("0")
            d7.set("0")
            d8.set("0")
            d9.set("0")
            d10.set("0")
            d11.set("0")
            d12.set("0")
            d13.set("0")
            d14.set("0")
            d15.set("0")
            d16.set("0")
            d17.set("0")
            d18.set("0")
            d19.set("0")
            d20.set("0")

            a.set(0)
            a1.set(0)
            a2.set(0)
            a3.set(0)
            a4.set(0)
            a5.set(0)
            a6.set(0)
            a7.set(0)
            a8.set(0)
            a9.set(0)
            a10.set(0)
            a11.set(0)
            a12.set(0)
            a13.set(0)
            a14.set(0)
            a15.set(0)
            a16.set(0)
            a17.set(0)
            a18.set(0)
            a19.set(0)

            e1.configure(state=DISABLED)
            e2.configure(state=DISABLED)
            e3.configure(state=DISABLED)
            e4.configure(state=DISABLED)
            e5.configure(state=DISABLED)
            e6.configure(state=DISABLED)
            e7.configure(state=DISABLED)
            e8.configure(state=DISABLED)
            e9.configure(state=DISABLED)
            e10.configure(state=DISABLED)
            f1.configure(state=DISABLED)
            f2.configure(state=DISABLED)
            f3.configure(state=DISABLED)
            f4.configure(state=DISABLED)
            f5.configure(state=DISABLED)
            f6.configure(state=DISABLED)
            f7.configure(state=DISABLED)
            f8.configure(state=DISABLED)
            f9.configure(state=DISABLED)
            f10.configure(state=DISABLED)

            l1.destroy()
            l2.destroy()
            l3.destroy()
            l4.destroy()
            l5.destroy()
            l6.destroy()
            l7.destroy()
            l8.destroy()
            l9.destroy()
            l10.destroy()
            l11.destroy()
            l12.destroy()
            l13.destroy()
            l14.destroy()
            l15.destroy()
            l16.destroy()
            l17.destroy()
            l18.destroy()
            l19.destroy()
            l20.destroy()

            t1.destroy()
            t2.destroy()
            t3.destroy()
            t4.destroy()
            t5.destroy()
            t6.destroy()
            t7.destroy()
            t8.destroy()
            t9.destroy()
            t10.destroy()
            t11.destroy()
            t12.destroy()
            t13.destroy()
            t14.destroy()
            t15.destroy()
            t16.destroy()
            t17.destroy()
            t18.destroy()
            t19.destroy()
            t20.destroy()
        def genratebill():
            global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20
            global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20
            v1=StringVar()
            v2=StringVar()
            v3=StringVar()
            v4=StringVar()
            v5=StringVar()
            v6=StringVar()
            v7=StringVar()
            v8=StringVar()
            v9=StringVar()
            v10=StringVar()
            v11=StringVar()
            v12=StringVar()
            v13=StringVar()
            v14=StringVar()
            v15=StringVar()
            v16=StringVar()
            v17=StringVar()
            v18=StringVar()
            v19=StringVar()
            v20=StringVar()
            
            t1=Label(f3a,textvariable=v1)
            t2=Label(f3a,textvariable=v2)
            t3=Label(f3a,textvariable=v3)
            t4=Label(f3a,textvariable=v4)
            t5=Label(f3a,textvariable=v5)
            t6=Label(f3a,textvariable=v6)
            t7=Label(f3a,textvariable=v7)
            t8=Label(f3a,textvariable=v8)
            t9=Label(f3a,textvariable=v9)
            t10=Label(f3a,textvariable=v10)
            t11=Label(f3a,textvariable=v11)
            t12=Label(f3a,textvariable=v12)
            t13=Label(f3a,textvariable=v13)
            t14=Label(f3a,textvariable=v14)
            t15=Label(f3a,textvariable=v15)
            t16=Label(f3a,textvariable=v16)
            t17=Label(f3a,textvariable=v17)
            t18=Label(f3a,textvariable=v18)
            t19=Label(f3a,textvariable=v19)
            t20=Label(f3a,textvariable=v20)

            l1=Label(f3a,text="Motia Pulao Imtiazi")        
            l2=Label(f3a,text="Dum Ghost Lucknowi Briyani")
            l3=Label(f3a,text="Dum Murgh Lucknowi Briyani")
            l4=Label(f3a,text="Dum Rice")
            l5=Label(f3a,text="Fragrant Basmati rice")
            l6=Label(f3a,text="Margherita")
            l7=Label(f3a,text="Primavera")
            l8=Label(f3a,text="Tandoori Paneer")
            l9=Label(f3a,text="Paneer Vegorama")
            l10=Label(f3a,text="Supreme Veggie")
            l11=Label(f3a,text="Kulcha")
            l12=Label(f3a,text="Naan")
            l13=Label(f3a,text="Paratha")
            l14=Label(f3a,text="Roti")
            l15=Label(f3a,text="Tandoori Roti")
            l16=Label(f3a,text="Lassi")
            l17=Label(f3a,text="Raita")
            l18=Label(f3a,text="Peanut Masala")
            l19=Label(f3a,text="Papad Masala")
            l20=Label(f3a,text="Papad")                                                

            Label(f3a,text="Recipt:",font="Arial 16 bold").grid(row=1,column=0,sticky=W)
            if a.get()==1:
                l1.grid(row=16,column=0,sticky=W)
                v1.set((int(e1.get()))*449)
                t1.grid(row=16,column=1,sticky=E)
            if a1.get()==2:
                l2.grid(row=2,column=0,sticky=W)
                v2.set((int(e2.get()))*549)
                t2.grid(row=2,column=1,sticky=E)
            if a2.get()==3:
                l3.grid(row=3,column=0,sticky=W)
                v3.set((int(e3.get()))*549)
                t3.grid(row=3,column=1,sticky=E)
            if a3.get()==4:
                l4.grid(row=4,column=0,sticky=W)
                v4.set((int(e4.get()))*349)
                t4.grid(row=4,column=1,sticky=E)
            if a4.get()==5:
                l5.grid(row=5,column=0,sticky=W)
                v5.set((int(e5.get()))*349)
                t5.grid(row=5,column=1,sticky=E)
            if a5.get()==6:
                l6.grid(row=6,column=0,sticky=W)
                v6.set((int(e6.get()))*249)
                t6.grid(row=6,column=1,sticky=E)
            if a6.get()==7:
                l7.grid(row=7,column=0,sticky=W)
                v7.set((int(e7.get()))*299)
                t7.grid(row=7,column=1,sticky=E)
            if a7.get()==8:
                l8.grid(row=8,column=0,sticky=W)
                v8.set((int(e8.get()))*299)
                t8.grid(row=8,column=1,sticky=E)
            if a8.get()==9:
                l9.grid(row=9,column=0,sticky=W)
                v9.set((int(e9.get()))*299)
                t9.grid(row=9,column=1,sticky=E)
            if a9.get()==10:
                l10.grid(row=10,column=0,sticky=W)
                v10.set((int(e10.get()))*299)
                t10.grid(row=10,column=1,sticky=E)
            if a10.get()==11:
                l11.grid(row=11,column=0,sticky=W)
                v11.set((int(f1.get()))*149)
                t11.grid(row=11,column=1,sticky=E)
            if a11.get()==12:
                l12.grid(row=12,column=0,sticky=W)
                v12.set((int(f2.get()))*99)
                t12.grid(row=12,column=1,sticky=E)
            if a12.get()==13:
                l13.grid(row=13,column=0,sticky=W)
                v13.set((int(f3.get()))*99)
                t13.grid(row=13,column=1,sticky=E)
            if a13.get()==14:
                l14.grid(row=14,column=0,sticky=W)
                v14.set((int(f4.get()))*99)
                t14.grid(row=14,column=1,sticky=E)
            if a14.get()==15:
                l15.grid(row=15,column=0,sticky=W)
                v15.set((int(f5.get()))*99)
                t15.grid(row=15,column=1,sticky=E)
            if a15.get()==16:
                l16.grid(row=21,column=0,sticky=W)
                v16.set((int(f6.get()))*199)
                t16.grid(row=21,column=1,sticky=E)
            if a16.get()==17:
                l17.grid(row=17,column=0,sticky=W)
                v17.set((int(f7.get()))*149)
                t17.grid(row=17,column=1,sticky=E)
            if a17.get()==18:
                l18.grid(row=18,column=0,sticky=W)
                v18.set((int(f8.get()))*199)
                t18.grid(row=18,column=1,sticky=E)
            if a18.get()==19:
                l19.grid(row=19,column=0,sticky=W)
                v19.set((int(f9.get()))*99)
                t19.grid(row=19,column=1,sticky=E)
            if a19.get()==20:
                l20.grid(row=20,column=0,sticky=W)
                v20.set((int(f10.get()))*49)
                t20.grid(row=20,column=1,sticky=E)

        def printbill():
            #root1.withdraw()
            master=Tk()
            #master.geometry('600x800')
            master.attributes('-fullscreen',True)
            
            global num
            num=0
            if a.get()==1:
                num=num+(int(e1.get())*449)
            if a1.get()==2:
                num=num+(int(e2.get())*549)
            if a2.get()==3:
                num=num+(int(e3.get())*549)
            if a3.get()==4:
                num=num+(int(e4.get())*349)
            if a4.get()==5:
                num=num+(int(e5.get())*349)
            if a5.get()==6:
                num=num+(int(e6.get())*249)
            if a6.get()==7:
                num=num+(int(e7.get())*299)
            if a7.get()==8:
                num=num+(int(e8.get())*299)
            if a8.get()==9:
                num=num+(int(e9.get())*299)
            if a9.get()==10:
                num=num+(int(e10.get())*299)
            if a10.get()==11:
                num=num+(int(f1.get())*149)
            if a11.get()==12:
                num=num+(int(f2.get())*99)
            if a12.get()==13:
                num=num+(int(f3.get())*99)
            if a13.get()==14:
                num=num+(int(f4.get())*99)
            if a14.get()==15:
                num=num+(int(f5.get())*99)
            if a15.get()==16:
                num=num+(int(f6.get())*199)
            if a16.get()==17:
                num=num+(int(f7.get())*149)
            if a17.get()==18:
                num=num+(int(f8.get())*199)
            if a18.get()==19:
                num=num+(int(f9.get())*99)
            if a19.get()==200:
                num=num+(int(f10.get())*49)
            Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
            Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
            Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
            Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
            Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
            Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
            Label(master, text='\n\n\n\n\n\n\nYou have to pay ',fg='black',font='jokerman 22').pack(side=TOP,anchor=CENTER)
            Label(master, text='\n'+'Rs'+' '+str(num),fg='black',font='jokerman 24 bold').pack(side=TOP,anchor=CENTER)
            button4=Button(master,padx=16,pady=1,bd=4,fg='black',font="jokerman 12 bold",width=5,text="EXIT",command=master.destroy,relief='flat')
            button4.pack(side=BOTTOM,fill="both")
        

        b1=Button(f3b,padx=14,pady=1,fg='black',font="Arial 10 bold",width=5,text="PREVIOUS PAGE",command=root1.destroy)
        b1.pack(side=TOP,fill="both")

        b2=Button(f3b,padx=14,pady=1,fg='black',font="Arial 10 bold",width=5,text="GENRATE BILL",command=genratebill)
        b2.pack(side=TOP,fill="both")

        b3=Button(f3b,padx=14,pady=1,fg='black',font="Arial 10 bold",width=5,text="EXIT",command=root1.destroy)
        b3.pack(side=TOP,fill="both")

        b4=Button(f3b,padx=14,pady=1,fg='black',font="Arial 10 bold",width=5,text="RESET",command=reset)
        b4.pack(side=TOP,fill="both")

        b5=Button(f3b,padx=14,pady=1,fg='black',font="Arial 10 bold",width=5,text="PRINT BILL",command=printbill)
        b5.pack(side=TOP,fill="both")

        root1.mainloop()
#============================================================page2ends======================================================
        
        
    root1.geometry("1350x750+0+0")
    root1.attributes('-fullscreen',True)
    root1.title("PAGE 1")
    root.configure(background="black")

    f1=Frame(root1,width=1350,height=100,bd=14,relief="raise")
    f1.pack(side=TOP,fill="both",expand="yes")

    f2=Frame(root1,width=900,height=650,bd=8,relief="raise")
    f2.pack(side=LEFT,fill="both",expand="yes")

    f3=Frame(root1,width=440,height=650,bd=8,relief="raise")
    f3.pack(side=RIGHT,fill="both",expand="yes")

    f2a=Frame(f2,width=900,height=330,bd=8,relief="raise")
    f2a.pack(side=TOP,fill="both",expand="yes")
    f2b=Frame(f2,width=900,height=320,bd=6,relief="raise")
    f2b.pack(side=BOTTOM,fill="both",expand="yes")

    f3a=Frame(f3,width=440,height=450,bd=12,relief="raise")
    f3a.pack(side=TOP,fill="both",expand="yes")
    f3b=Frame(f3,width=440,height=250,bd=12,relief="raise")
    f3b.pack(side=BOTTOM,fill="both",expand="yes")

    f2aa=Frame(f2a,width=400,height=330,bd=16,relief="raise")
    f2aa.pack(side=LEFT,fill="both",expand="yes")
    f2bb=Frame(f2a,width=400,height=330,bd=16,relief="raise")
    f2bb.pack(side=RIGHT,fill="both",expand="yes")

    f2aa1=Frame(f2b,width=450,height=330,bd=14,relief="raise")
    f2aa1.pack(side=LEFT,fill="both",expand="yes")
    f2bb1=Frame(f2b,width=450,height=330,bd=14,relief="raise")
    f2bb1.pack(side=RIGHT,fill="both",expand="yes")

    f1.configure(background="black")
    f2.configure(background="black")
    f3.configure(background="black")

    a=IntVar()
    a1=IntVar()
    a2=IntVar()
    a3=IntVar()
    a4=IntVar()
    a5=IntVar()
    a6=IntVar()
    a7=IntVar()
    a8=IntVar()
    a9=IntVar()
    a10=IntVar()
    a11=IntVar()
    a12=IntVar()
    a13=IntVar()
    a14=IntVar()
    a15=IntVar()
    a16=IntVar()
    a17=IntVar()
    a18=IntVar()
    a19=IntVar()

    d1=StringVar()
    d2=StringVar()
    d3=StringVar()
    d4=StringVar()
    d5=StringVar()
    d6=StringVar()
    d7=StringVar()
    d8=StringVar()
    d9=StringVar()
    d10=StringVar()
    d11=StringVar()
    d12=StringVar()
    d13=StringVar()
    d14=StringVar()
    d15=StringVar()
    d16=StringVar()
    d17=StringVar()
    d18=StringVar()
    d19=StringVar()
    d20=StringVar()

    def click():
        if a.get()==1:
            e1.configure(state=NORMAL)
        elif a.get()==0:
            e1.configure(state=DISABLED)
        if a1.get()==2:
            e2.configure(state=NORMAL)
        elif a1.get()==0:
            e2.configure(state=DISABLED)
        if a2.get()==3:
            e3.configure(state=NORMAL)
        elif a2.get()==0:
            e3.configure(state=DISABLED)
        if a3.get()==4:
            e4.configure(state=NORMAL)
        elif a3.get()==0:
            e4.configure(state=DISABLED)
        if a4.get()==5:
            e5.configure(state=NORMAL)
        elif a4.get()==0:
            e5.configure(state=DISABLED)
        if a5.get()==6:
            e6.configure(state=NORMAL)
        elif a5.get()==0:
            e6.configure(state=DISABLED)
        if a6.get()==7:
            e7.configure(state=NORMAL)
        elif a6.get()==0:
            e7.configure(state=DISABLED)
        if a7.get()==8: 
            e8.configure(state=NORMAL)
        elif a7.get()==0:
            e8.configure(state=DISABLED)
        if a8.get()==9:
            e9.configure(state=NORMAL)
        elif a8.get()==0:
            e9.configure(state=DISABLED)
        if a9.get()==10:
            e10.configure(state=NORMAL)
        elif a9.get()==0:
            e10.configure(state=DISABLED)
        if a10.get()==11:
            f1.configure(state=NORMAL)
        elif a10.get()==0:
            f1.configure(state=DISABLED)
        if a11.get()==12:
            f2.configure(state=NORMAL)
        elif a11.get==0:
            f2.configure(state=DISABLED)
        if a12.get()==13:
            f3.configure(state=NORMAL)
        elif a12.get==0:
            f3.configure(state=DISABLED)
        if a13.get()==14:
            f4.configure(state=NORMAL)
        elif a13.get==0:
            f4.configure(state=DISABLED)
        if a14.get()==15:
            f5.configure(state=NORMAL)
        elif a14.get==0:
            f5.configure(state=DISABLED)
        if a15.get()==16:
            f6.configure(state=NORMAL)
        elif a15.get()==0:
            f6.configure(state=DISABLED)
        if a16.get()==17:
            f7.configure(state=NORMAL)
        elif a16.get()==0:
            f7.configure(state=DISABLED)
        if a17.get()==18:
            f8.configure(state=NORMAL)
        elif a17.get()==0:
            f8.configure(state=DISABLED)
        if a18.get()==19:
            f9.configure(state=NORMAL)
        elif a18.get()==0:
            f9.configure(state=DISABLED)
        if a19.get()==20:
            f10.configure(state=NORMAL)
        elif a19.get()==0:
            f10.configure(state=DISABLED)


        
    Label(f1,text="BAY LEAF RESTAURANT",font="Arial 70 bold").pack(side=TOP,fill="both",expand="yes")
    Label(f2aa,text="SOUP",font="Arial 20 bold").grid(row=0,column=0,sticky=W)
    c1=Checkbutton(f2aa,font="Arial 18 bold",text="Dal Tamator Ka Shorba",command=click,variable=a,onvalue=1).grid(row=1,column=0,sticky=W)
    Label(f2aa,font="Arial 18 bold",text="249").grid(row=1,column=4)
    c2=Checkbutton(f2aa,font="Arial 18 bold",text="Yakhni Badami Shorba",command=click,variable=a1,onvalue=2).grid(row=2,column=0,sticky=W)
    Label(f2aa,font="Arial 18 bold",text="269").grid(row=2,column=4)
    c3=Checkbutton(f2aa,font="Arial 18 bold",text="Zaffrani Murgh Shorba",command=click,variable=a2,onvalue=3).grid(row=3,column=0,sticky=W)
    Label(f2aa,font="Arial 18 bold",text="269").grid(row=3,column=4)
    c4=Checkbutton(f2aa,font="Arial 18 bold",text="Tom yum",variable=a3,command=click,onvalue=4).grid(row=4,column=0,sticky=W)
    Label(f2aa,font="Arial 18 bold",text="199").grid(row=4,column=4)
    c5=Checkbutton(f2aa,font="Arial 18 bold",text="Chinese Clear soup",command=click,variable=a4,onvalue=5).grid(row=5,column=0,sticky=W)
    Label(f2aa,font="Arial 18 bold",text="199").grid(row=5,column=4)
    
    Label(f2bb,text="KEBAS",font="Arial 20 bold").grid(row=0,column=0,sticky=W)
    c6=Checkbutton(f2bb,font="Arial 18 bold",text="Peshawari Paneer Tikka",command=click,variable=a5,onvalue=6).grid(row=1,column=0,sticky=W)
    Label(f2bb,font="Arial 18 bold",text="399").grid(row=1,column=4)
    c7=Checkbutton(f2bb,font="Arial 18 bold",text="Paneer Dudhiya Kebab",command=click,variable=a6,onvalue=7).grid(row=2,column=0,sticky=W)
    Label(f2bb,font="Arial 18 bold",text="399").grid(row=2,column=4)
    c8=Checkbutton(f2bb,font="Arial 18 bold",text="Makai Seekh Kebab",command=click,variable=a7,onvalue=8).grid(row=3,column=0,sticky=W)
    Label(f2bb,font="Arial 18 bold",text="399").grid(row=3,column=4)
    c9=Checkbutton(f2bb,font="Arial 18 bold",text="Shahi Khumb Galouti",command=click,variable=a8,onvalue=9).grid(row=4,column=0,sticky=W)
    Label(f2bb,font="Arial 18 bold",text="399").grid(row=4,column=4)
    c10=Checkbutton(f2bb,font="Arial 18 bold",text="Vegetarian Kebab Platter",command=click,variable=a9,onvalue=10).grid(row=5,column=0,sticky=W)
    Label(f2bb,font="Arial 18 bold",text="750").grid(row=5,column=4)

    Label(f2aa1,text="Mains Vegetarian",font="Arial 20 bold").grid(row=0,column=0,sticky=W)
    Checkbutton(f2aa1,font="Arial 18 bold",text="Matter Makhaney",command=click,variable=a10,onvalue=11).grid(row=1,column=0,sticky=W)
    Label(f2aa1,font="Arial 18 bold",text="549").grid(row=1,column=4)
    Checkbutton(f2aa1,font="Arial 18 bold",text="Khada Palak Lehsuni",command=click,variable=a11,onvalue=12).grid(row=2,column=0,sticky=W)
    Label(f2aa1,font="Arial 18 bold",text="569").grid(row=2,column=4)
    Checkbutton(f2aa1,font="Arial 18 bold",text="Malai Kofta",command=click,variable=a12,onvalue=13).grid(row=3,column=0,sticky=W)
    Label(f2aa1,font="Arial 18 bold",text="569").grid(row=3,column=4)
    Checkbutton(f2aa1,font="Arial 18 bold",text="Makhani Paneer",command=click,variable=a13,onvalue=14).grid(row=4,column=0,sticky=W)
    Label(f2aa1,font="Arial 18 bold",text="549").grid(row=4,column=4)
    Checkbutton(f2aa1,font="Arial 18 bold",text="Pindi Chole",command=click,variable=a14,onvalue=15).grid(row=5,column=0,sticky=W)
    Label(f2aa1,font="Arial 18 bold",text="549").grid(row=5,column=4)

    Label(f2bb1,text="Mains Non Vegetarian ",font="Arial 20 bold").grid(row=0,column=0,sticky=W)
    Checkbutton(f2bb1,font="Arial 18 bold",text="Murgh Handi Korma",command=click,variable=a15,onvalue=16).grid(row=1,column=0,sticky=W)
    Label(f2bb1,font="Arial 18 bold",text="599").grid(row=1,column=4)
    Checkbutton(f2bb1,font="Arial 18 bold",text="Lucknowi Nihari",command=click,variable=a16,onvalue=17).grid(row=2,column=0,sticky=W)
    Label(f2bb1,font="Arial 18 bold",text="649").grid(row=2,column=4)
    Checkbutton(f2bb1,font="Arial 18 bold",text="Murgh Makhani",command=click,variable=a17,onvalue=18).grid(row=3,column=0,sticky=W)
    Label(f2bb1,font="Arial 18 bold",text="599").grid(row=3,column=4)
    Checkbutton(f2bb1,font="Arial 18 bold",text="Maahi Kaliyan ",command=click,variable=a18,onvalue=19).grid(row=4,column=0,sticky=W)
    Label(f2bb1,font="Arial 18 bold",text="699").grid(row=4,column=4)
    Checkbutton(f2bb1,font="Arial 18 bold",text="Butter Chicken",command=click,variable=a19,onvalue=20).grid(row=5,column=0,sticky=W)
    Label(f2bb1,font="Arial 18 bold",text="550").grid(row=5,column=4)

    e1=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d1,state=DISABLED)
    e1.grid(row=1,column=1)
    e2=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d2,state=DISABLED)
    e2.grid(row=2,column=1)
    e3=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d3,state=DISABLED)
    e3.grid(row=3,column=1)
    e4=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d4,state=DISABLED)
    e4.grid(row=4,column=1)
    e5=Entry(f2aa,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d5,state=DISABLED)
    e5.grid(row=5,column=1)

    e6=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d6,state=DISABLED)
    e6.grid(row=1,column=1)
    e7=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d7,state=DISABLED)
    e7.grid(row=2,column=1)
    e8=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d8,state=DISABLED)
    e8.grid(row=3,column=1)
    e9=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d9,state=DISABLED)
    e9.grid(row=4,column=1)
    e10=Entry(f2bb,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d10,state=DISABLED)
    e10.grid(row=5,column=1)

    f1=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d11,state=DISABLED)
    f1.grid(row=1,column=1)
    f2=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d12,state=DISABLED)
    f2.grid(row=2,column=1)
    f3=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d13,state=DISABLED)
    f3.grid(row=3,column=1)
    f4=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d14,state=DISABLED)
    f4.grid(row=4,column=1)
    f5=Entry(f2aa1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d15,state=DISABLED)
    f5.grid(row=5,column=1)

    f6=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d16,state=DISABLED)
    f6.grid(row=1,column=1)
    f7=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d17,state=DISABLED)
    f7.grid(row=2,column=1)
    f8=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d18,state=DISABLED)
    f8.grid(row=3,column=1)
    f9=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d19,state=DISABLED)
    f9.grid(row=4,column=1)
    f10=Entry(f2bb1,bd=8,width=6,font="Arial 16 bold",justify='left',textvariable=d20,state=DISABLED)
    f10.grid(row=5,column=1)

    def reset():
        d1.set("0")
        d2.set("0")
        d3.set("0")
        d4.set("0")
        d5.set("0")
        d6.set("0")
        d7.set("0")
        d8.set("0")
        d9.set("0")
        d10.set("0")
        d11.set("0")
        d12.set("0")
        d13.set("0")
        d14.set("0")
        d15.set("0")
        d16.set("0")
        d17.set("0")
        d18.set("0")
        d19.set("0")
        d20.set("0")

        a.set(0)
        a1.set(0)
        a2.set(0)
        a3.set(0)
        a4.set(0)
        a5.set(0)
        a6.set(0)
        a7.set(0)
        a8.set(0)
        a9.set(0)
        a10.set(0)
        a11.set(0)
        a12.set(0)
        a13.set(0)
        a14.set(0)
        a15.set(0)
        a16.set(0)
        a17.set(0)
        a18.set(0)
        a19.set(0)

        e1.configure(state=DISABLED)
        e2.configure(state=DISABLED)
        e3.configure(state=DISABLED)
        e4.configure(state=DISABLED)
        e5.configure(state=DISABLED)
        e6.configure(state=DISABLED)
        e7.configure(state=DISABLED)
        e8.configure(state=DISABLED)
        e9.configure(state=DISABLED)
        e10.configure(state=DISABLED)
        f1.configure(state=DISABLED)
        f2.configure(state=DISABLED)
        f3.configure(state=DISABLED)
        f4.configure(state=DISABLED)
        f5.configure(state=DISABLED)
        f6.configure(state=DISABLED)
        f7.configure(state=DISABLED)
        f8.configure(state=DISABLED)
        f9.configure(state=DISABLED)
        f10.configure(state=DISABLED)

        l1.destroy()
        l2.destroy()
        l3.destroy()
        l4.destroy()
        l5.destroy()
        l6.destroy()
        l7.destroy()
        l8.destroy()
        l9.destroy()
        l10.destroy()
        l11.destroy()
        l12.destroy()
        l13.destroy()
        l14.destroy()
        l15.destroy()
        l16.destroy()
        l17.destroy()
        l18.destroy()
        l19.destroy()
        l20.destroy()

        t1.destroy()
        t2.destroy()
        t3.destroy()
        t4.destroy()
        t5.destroy()
        t6.destroy()
        t7.destroy()
        t8.destroy()
        t9.destroy()
        t10.destroy()
        t11.destroy()
        t12.destroy()
        t13.destroy()
        t14.destroy()
        t15.destroy()
        t16.destroy()
        t17.destroy()
        t18.destroy()
        t19.destroy()
        t20.destroy()
        


    def genratebill():
        global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20
        global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20
        v1=StringVar()
        v2=StringVar()
        v3=StringVar()
        v4=StringVar()
        v5=StringVar()
        v6=StringVar()
        v7=StringVar()
        v8=StringVar()
        v9=StringVar()
        v10=StringVar()
        v11=StringVar()
        v12=StringVar()
        v13=StringVar()
        v14=StringVar()
        v15=StringVar()
        v16=StringVar()
        v17=StringVar()
        v18=StringVar()
        v19=StringVar()
        v20=StringVar()
        
        t1=Label(f3a,font="Arial 16 bold",textvariable=v1)
        t2=Label(f3a,font="Arial 16 bold",textvariable=v2)
        t3=Label(f3a,font="Arial 16 bold",textvariable=v3)
        t4=Label(f3a,font="Arial 16 bold",textvariable=v4)
        t5=Label(f3a,font="Arial 16 bold",textvariable=v5)
        t6=Label(f3a,font="Arial 16 bold",textvariable=v6)
        t7=Label(f3a,font="Arial 16 bold",textvariable=v7)
        t8=Label(f3a,font="Arial 16 bold",textvariable=v8)
        t9=Label(f3a,font="Arial 16 bold",textvariable=v9)
        t10=Label(f3a,font="Arial 16 bold",textvariable=v10)
        t11=Label(f3a,font="Arial 16 bold",textvariable=v11)
        t12=Label(f3a,font="Arial 16 bold",textvariable=v12)
        t13=Label(f3a,font="Arial 16 bold",textvariable=v13)
        t14=Label(f3a,font="Arial 16 bold",textvariable=v14)
        t15=Label(f3a,font="Arial 16 bold",textvariable=v15)
        t16=Label(f3a,font="Arial 16 bold",textvariable=v16)
        t17=Label(f3a,font="Arial 16 bold",textvariable=v17)
        t18=Label(f3a,font="Arial 16 bold",textvariable=v18)
        t19=Label(f3a,font="Arial 16 bold",textvariable=v19)
        t20=Label(f3a,font="Arial 16 bold",textvariable=v20)

        l1=Label(f3a,font="Arial 16 bold",text="Dal Tamator Ka Shorba")        
        l2=Label(f3a,font="Arial 16 bold",text="Yakhni Badami Shorba")
        l3=Label(f3a,font="Arial 16 bold",text="Zaffrani Murgh Shorba")
        l4=Label(f3a,font="Arial 16 bold",text="Tom yum")
        l5=Label(f3a,font="Arial 16 bold",text="Chinese Clear soup")
        l6=Label(f3a,font="Arial 16 bold",text="Peshawari Paneer Tikka")
        l7=Label(f3a,font="Arial 16 bold",text="Paneer Dudhiya Kebab")
        l8=Label(f3a,font="Arial 16 bold",text="Makai Seekh Kebab")
        l9=Label(f3a,font="Arial 16 bold",text="Shahi Khumb Galouti")
        l10=Label(f3a,font="Arial 16 bold",text="Vegetarian Kebab Platter")
        l11=Label(f3a,font="Arial 16 bold",text="Matter Makhaney")
        l12=Label(f3a,font="Arial 16 bold",text="Khada Palak Lehsuni")
        l13=Label(f3a,font="Arial 16 bold",text="Malai Kofta")
        l14=Label(f3a,font="Arial 16 bold",text="Makhani Paneer")
        l15=Label(f3a,font="Arial 16 bold",text="Pindi Chole")
        l16=Label(f3a,font="Arial 16 bold",text="Murgh Handi Korma")
        l17=Label(f3a,font="Arial 16 bold",text="Lucknowi Nihari")
        l18=Label(f3a,font="Arial 16 bold",text="Murgh Makhani")
        l19=Label(f3a,font="Arial 16 bold",text="Maahi Kaliyan")
        l20=Label(f3a,font="Arial 16 bold",text="Butter Chicken")                                                

        Label(f3a,text="Recipt:",font="Arial 16 bold").grid(row=1,column=0,sticky=W)
        if a.get()==1:
            l1.grid(row=16,column=0,sticky=W)
            v1.set((int(e1.get()))*249)
            t1.grid(row=16,column=1,sticky=E)
        if a1.get()==2:
            l2.grid(row=2,column=0,sticky=W)
            v2.set((int(e2.get()))*269)
            t2.grid(row=2,column=1,sticky=E)
        if a2.get()==3:
            l3.grid(row=3,column=0,sticky=W)
            v3.set((int(e3.get()))*269)
            t3.grid(row=3,column=1,sticky=E)
        if a3.get()==4:
            l4.grid(row=4,column=0,sticky=W)
            v4.set((int(e4.get()))*199)
            t4.grid(row=4,column=1,sticky=E)
        if a4.get()==5:
            l5.grid(row=5,column=0,sticky=W)
            v5.set((int(e5.get()))*199)
            t5.grid(row=5,column=1,sticky=E)
        if a5.get()==6:
            l6.grid(row=6,column=0,sticky=W)
            v6.set((int(e6.get()))*399)
            t6.grid(row=6,column=1,sticky=E)
        if a6.get()==7:
            l7.grid(row=7,column=0,sticky=W)
            v7.set((int(e7.get()))*399)
            t7.grid(row=7,column=1,sticky=E)
        if a7.get()==8:
            l8.grid(row=8,column=0,sticky=W)
            v8.set((int(e8.get()))*399)
            t8.grid(row=8,column=1,sticky=E)
        if a8.get()==9:
            l9.grid(row=9,column=0,sticky=W)
            v9.set((int(e9.get()))*399)
            t9.grid(row=9,column=1,sticky=E)
        if a9.get()==10:
            l10.grid(row=10,column=0,sticky=W)
            v10.set((int(e10.get()))*750)
            t10.grid(row=10,column=1,sticky=E)
        if a10.get()==11:
            l11.grid(row=11,column=0,sticky=W)
            v11.set((int(f1.get()))*549)
            t11.grid(row=11,column=1,sticky=E)
        if a11.get()==12:
            l12.grid(row=12,column=0,sticky=W)
            v12.set((int(f2.get()))*569)
            t12.grid(row=12,column=1,sticky=E)
        if a12.get()==13:
            l13.grid(row=13,column=0,sticky=W)
            v13.set((int(f3.get()))*569)
            t13.grid(row=13,column=1,sticky=E)
        if a13.get()==14:
            l14.grid(row=14,column=0,sticky=W)
            v14.set((int(f4.get()))*549)
            t14.grid(row=14,column=1,sticky=E)
        if a14.get()==15:
            l15.grid(row=15,column=0,sticky=W)
            v15.set((int(f5.get()))*549)
            t15.grid(row=15,column=1,sticky=E)
        if a15.get()==16:
            l16.grid(row=21,column=0,sticky=W)
            v16.set((int(f6.get()))*599)
            t16.grid(row=21,column=1,sticky=E)
        if a16.get()==17:
            l17.grid(row=17,column=0,sticky=W)
            v17.set((int(f7.get()))*649)
            t17.grid(row=17,column=1,sticky=E)
        if a17.get()==18:
            l18.grid(row=18,column=0,sticky=W)
            v18.set((int(f8.get()))*599)
            t18.grid(row=18,column=1,sticky=E)
        if a18.get()==19:
            l19.grid(row=19,column=0,sticky=W)
            v19.set((int(f9.get()))*699)
            t19.grid(row=19,column=1,sticky=E)
        if a19.get()==20:
            l20.grid(row=20,column=0,sticky=W)
            v20.set((int(f10.get()))*550)
            t20.grid(row=20,column=1,sticky=E)


    def printbill():
        #root1.withdraw()
        master=Tk()
        #master.geometry('600x800')
        master.attributes('-fullscreen',True)
        
        global num
        num=0
        if a.get()==1:
            num=num+(int(e1.get())*249)
        if a1.get()==2:
            num=num+(int(e2.get())*269)
        if a2.get()==3:
            num=num+(int(e3.get())*269)
        if a3.get()==4:
            num=num+(int(e4.get())*199)
        if a4.get()==5:
            num=num+(int(e5.get())*199)
        if a5.get()==6:
            num=num+(int(e6.get())*399)
        if a6.get()==7:
            num=num+(int(e7.get())*399)
        if a7.get()==8:
            num=num+(int(e8.get())*399)
        if a8.get()==9:
            num=num+(int(e9.get())*399)
        if a9.get()==10:
            num=num+(int(e10.get())*750)
        if a10.get()==11:
            num=num+(int(f1.get())*599)
        if a11.get()==12:
            num=num+(int(f2.get())*649)
        if a12.get()==13:
            num=num+(int(f3.get())*599)
        if a13.get()==14:
            num=num+(int(f4.get())*699)
        if a14.get()==15:
            num=num+(int(f5.get())*550)
        if a15.get()==16:
            num=num+(int(f6.get())*549)
        if a16.get()==17:
            num=num+(int(f7.get())*569)
        if a17.get()==18:
            num=num+(int(f8.get())*569)
        if a18.get()==19:
            num=num+(int(f9.get())*549)
        if a19.get()==200:
            num=num+(int(f10.get())*549)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master, text='\n\n\n\n\n\n\nYou have to pay ',fg='black',font='jokerman 22').pack(side=TOP,anchor=CENTER)
        Label(master, text='\n'+'Rs'+' '+str(num),fg='black',font='jokerman 24 bold').pack(side=TOP,anchor=CENTER)
        button4=Button(master,padx=16,pady=1,bd=4,fg='black',font="jokerman 12 bold",width=5,text="EXIT",command=master.destroy,relief='flat')
        button4.pack(side=BOTTOM,fill="both")

    


    

    b1=Button(f3b,padx=10,pady=1,fg='black',font="Arial 10 bold",width=3,text="NEXT PAGE",command=nextpage)
    b1.pack(side=TOP,fill="both")

    b2=Button(f3b,padx=10,pady=1,fg='black',font="Arial 10 bold",width=3,text="GENRATE BILL",command=genratebill)
    b2.pack(side=TOP,fill="both")

    b3=Button(f3b,padx=10,pady=1,fg='black',font="Arial 10 bold",width=3,text="EXIT",command=root1.destroy)
    b3.pack(side=TOP,fill="both")

    b4=Button(f3b,padx=10,pady=1,fg='black',font="Arial 10 bold",width=3,text="RESET",command=reset)
    b4.pack(side=TOP,fill="both")

    b5=Button(f3b,padx=10,pady=1,fg='black',font="Arial 10 bold",width=3,text="PRINT BILL",command=printbill)
    b5.pack(side=TOP,fill="both")

    root1.mainloop()

#==================================================page1ends=======================================================    
    
root.geometry("1350x750+0+0")
root.title("Courtyard Marriott")
root.attributes('-fullscreen',True)
root.configure(background="black")

i1=PhotoImage(file="21.gif")
l1=Label(root,image=i1,font="Arial 70 bold",text="      The Courtyard Marriott     ",compound=CENTER,bd=10,fg='khaki')
def aboutus():
        master=Tk()
        
        master.attributes('-fullscreen',True)

        shortcutbar = Frame(master, height=30, bg='light green')
        Button(shortcutbar,justify=CENTER,text='CLOSE',activeforeground='khaki',overrelief=SOLID,relief=GROOVE,command=master.destroy,bg='red',activebackground='#00A0A0').pack(side=RIGHT,anchor=NE,fill=Y)
        toolbar = Label(shortcutbar, text='THE COURTYARD MARRIOTT',bg='light green',fg='dark green',font='CalibriLight 25 bold')
        toolbar1=Label(shortcutbar, text='DB City Hall, K-2, Hoshangabad Rd, Opposite Hypercity, Zone-I, Arera Hills, Bhopal, Madhya Pradesh 462011',bg='light green',fg='dark green',font='CalibriLight 15 bold')
        toolbar.pack(side=TOP,fill=X)
        toolbar1.pack(side=TOP,fill=X)
        shortcutbar.pack(side=TOP,fill=X)
        
        Label(master, text='').pack(side=TOP,fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master, text='\n\n\n\n\nYOU CAN CONTACT US ON',fg='black',font='Constantia 18 bold').pack(side=TOP,anchor=CENTER)
        
        Label(master, text='ARPIT SAXENA\n(7773080961 or 9584567841 ) ',fg='blue',font='castellar 20 bold').pack(side=TOP,anchor=CENTER)

        Label(master, text='Email : arpit.saxena591@gmail.com@gmail.com',fg='#00A0A0',font='Rockwell 15 bold',relief=RAISED,width=50).pack(side=BOTTOM,anchor=CENTER,fill=X)
        Label(master,text='Project designed by :ARPIT SAXENA',justify=CENTER,relief=RIDGE,fg='brown',font='Georgia 18 bold',bg='khaki').pack(side=BOTTOM,fill=X)
def forhelp():
        master=Tk()
        
        master.attributes('-fullscreen',True)

        shortcutbar = Frame(master, height=30, bg='light green')
        Button(shortcutbar,justify=CENTER,text='CLOSE',activeforeground='khaki',overrelief=SOLID,relief=GROOVE,command=master.destroy,bg='red',activebackground='#00A0A0').pack(side=RIGHT,anchor=NE,fill=Y)
        toolbar = Label(shortcutbar, text='THE COURTYARD MARRIOTT',bg='light green',fg='dark green',font='CalibriLight 25 bold')
        toolbar1=Label(shortcutbar, text='DB City Hall, K-2, Hoshangabad Rd, Opposite Hypercity, Zone-I, Arera Hills, Bhopal, Madhya Pradesh 462011',bg='light green',fg='dark green',font='CalibriLight 15 bold')
        toolbar.pack(side=TOP,fill=X)
        toolbar1.pack(side=TOP,fill=X)
        shortcutbar.pack(side=TOP,fill=X)
        
        Label(master, text='').pack(side=TOP,fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master, text='\n\n\n\n\nFOR ANY HELP YOU CAN CONTACT',fg='black',font='Constantia 18 bold').pack(side=TOP,anchor=CENTER)
        
        Label(master, text='Dr. MAHESH KUMAR SIR\nYour Subject Co-ordinator ',fg='blue',font='castellar 20 bold').pack(side=TOP,anchor=CENTER)

        Label(master, text='Email : mahesh.kumar[AT]juet.ac.in',fg='#00A0A0',font='Rockwell 15 bold',relief=RAISED,width=50).pack(side=BOTTOM,anchor=CENTER,fill=X)
        Label(master,text='Project designed by :ARPIT SAXENA',justify=CENTER,relief=RIDGE,fg='brown',font='Georgia 18 bold',bg='khaki').pack(side=BOTTOM,fill=X)
    
Button(l1,padx=16,pady=1,bd=4,fg='black',font="BatmanForeverAlternate 16 bold",width=5,text="EXIT",command=root.destroy).pack(side=BOTTOM,anchor=S)
Button(l1,padx=16,pady=1,bd=4,fg='black',font="Arial 16 bold",width=5,text="ENTER",command=enter).pack(anchor=CENTER)
Button(l1,padx=16,pady=1,bd=4,fg='black',font="Arial 16 bold",width=7,text="ABOUT US",command=aboutus).pack(side=RIGHT)
Button(l1,padx=16,pady=1,bd=4,fg='black',font="Arial 16 bold",width=7,text="HELP",command=forhelp).pack(side=LEFT)


l1.pack(side=TOP,fill="both",expand="yes")

root.mainloop()


