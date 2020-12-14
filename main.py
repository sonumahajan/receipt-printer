from tkinter import *
from num2words import num2words    # pip3 install num2words
import tempfile
import os
from datetime import date
import time


root = Tk()
root.geometry('500x500')
root.title("Sonu")

srno = 0
today = date.today().strftime('%d/%m/%Y')
ttime = time.strftime("%H:%M")

def reciept():
    try:
        top = Toplevel()
        top.geometry("500x300")
        top.config(background='white')
        print("i am sonu.")
        name = entry_1.get().upper() 
        bank = entry_2.get().upper() 
        account = entry_3.get()
        amount = entry_4.get()
        amountword = num2words(amount).upper()
        mobile = entry_5.get()

        l = Label(top, text="============RECIEPT============")
        l.pack()
        l.place(x = 30, y = 10)
        l.config(background="white")

        ll = Label(top, text=f"Sr.No.: {str(srno)}")
        ll.pack()
        ll.place(x = 40, y = 30)
        ll.config(background="white")

        lll = Label(top, text=f"Date: {today} {ttime}")
        lll.pack()
        lll.place(x = 200, y = 30)
        lll.config(background="white")

        item1 = Label(top, text='Receiver Name :')
        item1.pack()
        item1.place(x = 40, y = 60)
        item1.config(background="white")
        item10 = Label(top, text=name)
        item10.pack()
        item10.place(x = 200, y = 60)
        item10.config(background="white")

        item2 = Label(top, text='Bank Name :')
        item2.pack()
        item2.place(x = 40, y = 100)
        item2.config(background="white")
        item20 = Label(top, text=bank)
        item20.pack()
        item20.place(x = 200, y = 100)
        item20.config(background="white")

        item3 = Label(top, text='Account No. :')
        item3.pack()
        item3.place(x = 40, y = 140)
        item3.config(background="white")
        item30 = Label(top, text=account)
        item30.pack()
        item30.place(x = 200, y = 140)
        item30.config(background="white")

        item4 = Label(top, text='Amount :')
        item4.pack()
        item4.place(x = 40, y = 180)
        item4.config(background="white")
        item40 = Label(top, text=f"{amount}.0")
        item40.pack()
        item40.place(x = 200, y = 180)
        item40.config(background="white")

        item5 = Label(top, text='Amount in words :')
        item5.pack()
        item5.place(x = 40, y = 220)
        item5.config(background="white")
        item50 = Label(top, text= f"{amountword} RUPEE(s)(s)")
        item50.pack()
        item50.place(x = 200, y = 220)
        item50.config(background="white")

        item6 = Label(top, text='Mobile :')
        item6.pack()
        item6.place(x = 40, y = 260)
        item6.config(background="white")
        item10 = Label(top, text=mobile)
        item10.pack()
        item10.place(x = 200, y = 260)
        item10.config(background="white")
    except:
        print("no input")

def iprint():
    try:
        global srno
        name = entry_1.get().upper()  
        bank = entry_2.get().upper() 
        account = entry_3.get()
        amount = entry_4.get()
        amountword = num2words(amount).upper() 
        mobile = entry_5.get()
        filename = tempfile.mktemp(".txt")
        filename = "temp5.txt"
        with open (filename, "w") as fl:
            fl.writelines("        GUPTA MONEY TRANSFER\n")
            fl.writelines("  Vishakha Coloney, Dhandarai Khurd\n")
            fl.writelines("            M.- 8054851992 \n")
            fl.writelines("================RECEIPT================\n")
            fl.writelines(f"Sr.No.: {str(srno)}      Date: {today} {ttime}\n")
            fl.writelines(f"Receiver Name :    {name}\n")
            fl.writelines(f"Bank Name :        {bank}\n")
            fl.writelines(f"Account No. :      {account}\n")
            fl.writelines(f"Amount :           {amount}.0\n")
            fl.writelines(f"Amount in words :  {amountword} RUPEE(s)\n")
            fl.writelines(f"Mobile :           {mobile}\n")
            fl.writelines("\n")
            fl.writelines("NOTE- In Case of wrong Account No. or Name\n")
            fl.writelines("Custemer will be responsible.\n")
        srno += 1
        os.startfile(filename, "print")      #for windows
    except:
        print("no input")


label_0 = Label(root, text="Money Transfer",width=20,font=("bold", 20))
label_0.place(x=90,y=50)


label_1 = Label(root, text="Receiver Name",width=20,font=("bold", 10))
label_1.place(x=80,y=100)
entry_1 = Entry(root)
entry_1.place(x=240,y=100)

label_2 = Label(root, text="Bank Name",width=20,font=("bold", 10))
label_2.place(x=68,y=150)
entry_2 = Entry(root)
entry_2.place(x=240,y=150)

label_3 = Label(root, text="Account No.",width=20,font=("bold", 10))
label_3.place(x=70,y=200)
entry_3 = Entry(root)
entry_3.place(x=240,y=200)

label_4 = Label(root, text="Amount",width=20,font=("bold", 10))
label_4.place(x=70,y=250)
entry_4 = Entry(root)
entry_4.place(x=240,y=250)

label_5 = Label(root, text="Mobile",width=20,font=("bold", 10))
label_5.place(x=70,y=300)
entry_5 = Entry(root)
entry_5.place(x=240,y=300)


Button(root, text='Show',width=15,bg='brown',fg='white',command=reciept).place(x=100,y=380)
Button(root, text='Print',width=15,bg='brown',fg='white',command=iprint).place(x=280,y=380)


root.mainloop()