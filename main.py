#import all class and method inside tkinter module

from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
import re
from tkinter import ttk
#functionality part
from db import database
import time
db=database()
def total():
   #cosmetics
   global soapprice
   soapprice=int(bathsoapE.get())*20
   global facecreamprice
   facecreamprice=int(facecreamE.get())*120
   global facewashprice
   facewashprice=int(facewashE.get())*140
   global hairsprayprice
   hairsprayprice=int(hairsprayE.get())*150
   global hairgelprice
   hairgelprice=int(hairgelE.get())*60
   global bodylotionprice
   bodylotionprice=int(bodylotionE.get())*200
   global totalcosmticprice
   totalcosmticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
   #set entryvalue
   cosmeticprice_E.delete(0,END)
   cosmeticprice_E.insert(0,str(totalcosmticprice)+' Rs')
   cosmetictax=totalcosmticprice*0.12
   cosmetictax_E.delete(0,END)
   cosmetictax_E.insert(0,str(cosmetictax)+" Rs")
   #grocery
   global riceprice
   riceprice=int(riceE.get())*70
   global oilprice
   oilprice=int(oilE.get())*120
   global daalprice
   daalprice=int(daalE.get())*236
   global wheatprice
   wheatprice=int(wheatE.get())*52
   global sugarprice
   sugarprice=int(sugarE.get())*46
   global teaprice
   teaprice=int(teaE.get())*165
   # set entryvalue
   totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
   groceryprice_E.delete(0, END)
   groceryprice_E.insert(0,str(totalgroceryprice)+' Rs')
   grocerytax=totalgroceryprice*0.05
   grocerytax_E.delete(0,END)
   grocerytax_E.insert(0,str(grocerytax)+" Rs")
   #coldrink
   global maazaprice
   maazaprice=int(maazaE.get())*90
   global pepsiprice
   pepsiprice=int(pepsiE.get())*80
   global spriteprice
   spriteprice=int(spriteE.get())*85
   global dewprice
   dewprice=int(dewE.get())*50
   global frootiprice
   frootiprice=int(frootiE.get())*99
   global cocprice
   cocprice=int(cocE.get())*65
   # set total entryvalue
   totalcolddrinksprice=maazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cocprice
   colddrinksprice_E.delete(0, END)
   colddrinksprice_E.insert(0,str(totalcolddrinksprice)+' Rs')
   colddirnkstax=totalcolddrinksprice*0.08
   colddrinktax_E.delete(0,END)
   colddrinktax_E.insert(0,str(colddirnkstax)+" Rs")

   #totalbill
   global totalbill
   totalbill=totalcosmticprice+totalgroceryprice+totalcolddrinksprice+cosmetictax+grocerytax+colddirnkstax

#bill btn function
#crate bill folder import os
if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success",f'bill number {billnumber} is saved successfully')
        x = time.localtime()
        t = time.strftime("%d/%m/%Y,%H:%M:%S", x)
        db.insert(nameentry.get(),phoneentry.get(),billnumber,t)
        billnumber=random.randint(500,1000)
billnumber=random.randrange(500,1000)
def bill_area():
    if nameentry.get()=="" or phoneentry.get()=='':
         messagebox.showerror('Error','Customer Details Reqiured')


    elif cosmeticprice_E.get()=='' or groceryprice_E.get()=='' or colddrinksprice_E.get()=='':
        messagebox.showerror('Error', 'No products are selected')
    elif cosmeticprice_E.get()=='0 Rs' and groceryprice_E.get()=='0 Rs' and colddrinksprice_E.get()=='0 Rs':
        messagebox.showerror('Error', 'No products are selected')

    else:
        textarea.delete(1.0,END)


        if re.match("[1-9][0-9]{9}$", phoneentry.get()) and re.match("[A-Za-z]+", nameentry.get()):
         textarea.insert(END, '\t\t**Welcome Customer**\n')
         textarea.insert(END,f'\n Customer Name         : {nameentry.get()}\n')
         textarea.insert(END, f'\n Customer Phone Number : {phoneentry.get()}\n')
         textarea.insert(END, f'\n Bill Number           : {billnumber}\n')
         textarea.insert(END,f'\n ========================================================== \n')
         textarea.insert(END,'  Product\t\t\tQuantity\t\t\tPrice')
         textarea.insert(END, f'\n ========================================================== \n')


         if bathsoapE.get()!='0':
            textarea.insert(END,f'\n Bath Soap  \t\t\t{bathsoapE.get()}\t\t\t{soapprice} Rs\n')
         if facecreamE.get() != '0':
            textarea.insert(END, f' Face Cream \t\t\t{facecreamE.get()}\t\t\t{facecreamprice} Rs\n')
         if facewashE.get() != '0':
            textarea.insert(END, f' Face Wash  \t\t\t{facewashE.get()}\t\t\t{facewashprice} Rs\n')
         if hairsprayE.get() != '0':
            textarea.insert(END, f' Hair Spray \t\t\t{hairsprayE.get()}\t\t\t{hairsprayprice} Rs\n')
         if hairgelE.get() != '0':
            textarea.insert(END, f' Hair Gel   \t\t\t{hairgelE.get()}\t\t\t{hairgelprice} Rs\n')
         if bodylotionE.get() != '0':
            textarea.insert(END, f' Body Lotion\t\t\t{bodylotionE.get()}\t\t\t{bodylotionprice} Rs\n')
       #grocery
         if riceE.get() != '0':
            textarea.insert(END, f' Rice       \t\t\t{riceE.get()}\t\t\t{riceprice} Rs\n')
         if oilE.get() != '0':
            textarea.insert(END, f' Oil        \t\t\t{oilE.get()}\t\t\t{oilprice} Rs\n')
         if daalE.get() != '0':
            textarea.insert(END, f' Dal        \t\t\t{daalE.get()}\t\t\t{daalprice} Rs\n')
         if wheatE.get() != '0':
            textarea.insert(END, f' Wheat      \t\t\t{wheatE.get()}\t\t\t{wheatprice} Rs\n')
         if sugarE.get() != '0':
            textarea.insert(END, f' Sugar      \t\t\t{sugarE.get()}\t\t\t{sugarprice} Rs\n')
         if teaE.get() != '0':
            textarea.insert(END, f' Tea        \t\t\t{teaE.get()}\t\t\t{teaprice} Rs\n')
       #colddrinks
         if maazaE.get() != '0':
            textarea.insert(END, f' Maaza      \t\t\t{maazaE.get()}\t\t\t{maazaprice} Rs\n')
         if pepsiE.get() != '0':
            textarea.insert(END, f' Pepsi      \t\t\t{pepsiE.get()}\t\t\t{pepsiprice} Rs\n')
         if spriteE.get() != '0':
            textarea.insert(END, f' Sprite     \t\t\t{spriteE.get()}\t\t\t{spriteprice} Rs\n')
         if dewE.get() != '0':
            textarea.insert(END, f' Dew        \t\t\t{dewE.get()}\t\t\t{dewprice} Rs\n')
         if frootiE.get() != '0':
             textarea.insert(END, f' Frooti     \t\t\t{frootiE.get()}\t\t\t{frootiprice} Rs\n')
         if cocE.get() != '0':
            textarea.insert(END, f' Coca Cola  \t\t\t{cocE.get()}\t\t\t{cocprice} Rs\n')
         textarea.insert(END, f'\n ---------------------------------------------------------- ')
        #tax
         if cosmetictax_E.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cosmetic Tax \t\t\t\t{cosmetictax_E.get()}')
         if grocerytax_E.get()!='0.0 Rs':
            textarea.insert(END,f'\n Grocery Tax \t\t\t\t{grocerytax_E.get()}')
         if colddrinktax_E.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cold Drinks Tax \t\t\t\t{colddrinktax_E.get()}')

         textarea.insert(END,f'\n\n Total Bill \t\t\t\t{totalbill}')
         textarea.insert(END, f'\n ---------------------------------------------------------- ')
         save_bill()
        else:
            textarea.delete(1.0,END)
            messagebox.showerror("Error","Enter valid user details")
def search_bill():
    for i in os.listdir('bills'):
        if i.split('.')[0]==billnumentry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
            messagebox.showerror('Error','Invalid Bill Number')
#print bill
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file)
#email functionality:
def send_email():
    def send_gmail():
      try:
        ob=smtplib.SMTP('smtp.gmail.com',587)
        ob.starttls()
        ob.login(senderEntry.get(),passwordEntry.get())
        message=email_textarea.get(1.0,END)
        ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
        ob.quit()
        messagebox.showinfo("Success",'bill is successfully sent',parent=root1)
      except:
          messagebox.showerror("Error",'something went wrong, please try again',parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:

        root1=Toplevel()
        root1.title('send gmail')
        root1.config(bg='gray20')

        root1.resizable(0,0)


        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderlabel=Label(senderFrame,text="Sender's Email ",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderlabel.grid(row=0,column=0,padx=10,pady=8,sticky='w')

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8,sticky='w')

        passwordlabel=Label(senderFrame,text="Password ",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordlabel.grid(row=1,column=0,padx=10,pady=8,sticky='w')

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8,sticky='w')


        recipientFrame=LabelFrame(root1,text='RECIPIENT ',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        recieverlabel=Label(recipientFrame,text="Email Address ",font=('arial',14,'bold'),bg='gray20',fg='white')
        recieverlabel.grid(row=0,column=0,padx=10,pady=8,sticky='w')

        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8,sticky='w')

        messagelabel = Label(recipientFrame, text="Message ", font=('arial', 14, 'bold'), bg='gray20',
                              fg='white')
        messagelabel.grid(row=1, column=0, padx=10, pady=8, sticky='w')

        email_textarea=Text(recipientFrame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2,padx=5)
        #email val
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace("=",'').replace('-','')
                              .replace("\t\t\t",'\t\t'))


        #send btn
        sendbtn=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendbtn.grid(row=2,column=0,pady=10)


        root1.mainloop()
def clr():
    #del
    bathsoapE.delete(0,END)
    facecreamE.delete(0,END)
    facewashE.delete(0,END)
    hairgelE.delete(0,END)
    hairsprayE.delete(0,END)
    bodylotionE.delete(0,END)
    riceE.delete(0,END)
    oilE.delete(0,END)
    daalE.delete(0,END)
    wheatE.delete(0,END)
    sugarE.delete(0,END)
    teaE.delete(0,END)
    maazaE.delete(0,END)
    pepsiE.delete(0,END)
    spriteE.delete(0,END)
    dewE.delete(0,END)
    frootiE.delete(0,END)
    cocE.delete(0,END)
    #ins
    bathsoapE.insert(0, 0)
    facecreamE.insert(0, 0)
    facewashE.insert(0, 0)
    hairgelE.insert(0, 0)
    hairsprayE.insert(0, 0)
    bodylotionE.insert(0, 0)
    riceE.insert(0, 0)
    oilE.insert(0, 0)
    daalE.insert(0, 0)
    wheatE.insert(0, 0)
    sugarE.insert(0, 0)
    teaE.insert(0, 0)
    maazaE.insert(0, 0)
    pepsiE.insert(0, 0)
    spriteE.insert(0, 0)
    dewE.insert(0, 0)
    frootiE.insert(0, 0)
    cocE.insert(0, 0)
    #
    cosmeticprice_E.delete(0,END)
    groceryprice_E.delete(0,END)
    colddrinksprice_E.delete(0,END)
    cosmetictax_E.delete(0,END)
    grocerytax_E.delete(0,END)
    colddrinktax_E.delete(0,END)
    #
    nameentry.delete(0,END)
    phoneentry.delete(0,END)
    billnumentry.delete(0,END)
    textarea.delete(1.0,END)



def view():
    root2 = Tk()
    root2.title('Customer Details')
    root2.config(bg='gray20')
    root2.geometry('1366x786+0+0')  # for set width and height
    root2.state('zoomed')

    def search_bill2():
        for i in os.listdir('bills'):
            if i.split('.')[0] == billnumentry.get():
                f = open(f'bills/{i}', 'r')
                textarea.delete(1.0, END)
                for data in f:
                    textarea.insert(END, data)
                f.close()
                break
        else:
            messagebox.showerror('Error', 'Invalid Bill Number', parent=root2)

    def displayAll():
        tv.delete(*tv.get_children())
        for row in db.select():
            tv.insert("", END, values=row)
    def display_cus():
        tv.delete(*tv.get_children())
        for row in db.select_cus(phoneentry.get()):
            tv.insert("", END, values=row)
    wrapper1 = LabelFrame(root2, text="Customer List",bg="gray20",fg="white",font=('times new roman',15,'bold'))
    wrapper3 = LabelFrame(root2, text="Customer Data",bg="gray20",fg="white",font=('times new roman',15,'bold'))

    wrapper1.pack(fill="both", expand="yes", padx=50, pady=50)
    wrapper1.place(x=0, y=0, width=1366, height=300)
    #


    tv=ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5), show="headings", height="12")
    tv.pack(fill=X)
    tv.heading("1", text="Id")
    tv.column("1", width=50)
    tv.heading("2", text="Customer Name")
    tv.column("2", width=100)

    tv.heading("3", text="Customer Number")
    tv.column("3", width=100)
    tv.heading("4", text="Bill Number")
    tv.column("4", width=50)

    tv.heading("5", text="Purchase Date")
    tv.column("5", width=250)
    displayAll()
    productsFrame = Frame(root2)
    productsFrame.pack(fill=X)
    productsFrame.place(x=0, y=300, width=1366, height=390)
    phonel = Label(productsFrame, text="Phone Number :", font=('times new roman', 15, 'bold'))
    phonel.grid(row=0, column=0, padx=20, pady=2)

    phoneentry = Entry(productsFrame, font=("arial", 15), bd=7, width=18)
    phoneentry.grid(row=0, column=1, padx=8)
    searchbtn = Button(productsFrame, text="Search", font=('arial', 12, 'bold'), bd=7, width=10
                       ,command=display_cus)#command=search_bill
    searchbtn.grid(row=0, column=2, padx=20, pady=8)

    billl = Label(productsFrame, text="                                         ", font=('times new roman', 15, 'bold'))
    billl.grid(row=0, column=3, padx=20, pady=2)
    # bill number
    billl = Label(productsFrame, text="Bill Number :", font=('times new roman', 15, 'bold'))
    billl.grid(row=0, column=4, padx=20, pady=2)

    billnumentry = Entry(productsFrame, font=("arial", 15), bd=7, width=15)
    billnumentry.grid(row=0, column=5, padx=5)

    # search button
    searchbtn = Button(productsFrame, text="Search", font=('arial', 12, 'bold'), bd=7, width=10,
                       command=search_bill2)#
    searchbtn.grid(row=0, column=6, padx=10, pady=8)

    wrapper2 = LabelFrame(productsFrame, text="Search",bg="gray20",fg="white",font=('times new roman',15,'bold'))
    wrapper2.grid(row=1, column=0,columnspan=3, padx=10)

    # wrapper2.pack(fill="both", expand="yes", padx=50, pady=50)
    wrapper2.place(x=0, y=100, width=840, height=280)
    tv = ttk.Treeview(wrapper2, columns=(1, 2, 3, 4, 5), show="headings", height="12")
    tv.pack(fill=X)
    tv.heading("1", text="Id")
    tv.column("1", width=50)
    tv.heading("2", text="Customer Name")
    tv.column("2", width=100)

    tv.heading("3", text="Customer Number")
    tv.column("3", width=100)
    tv.heading("4", text="Bill Number")
    tv.column("4", width=50)

    tv.heading("5", text="Purchase Date")
    tv.column("5", width=250)
    # display_cus()

    billframe = Frame(productsFrame, bd=8, relief=GROOVE)
    billframe.grid(row=1, column=4, padx=10)
    bill_area_label = Label(billframe, text='Label Area',bg="gray20",fg="white",font=('times new roman',15,'bold'), bd=7, relief=GROOVE)
    bill_area_label.pack(fill=X)
    billframe.place(x=840, y=100, width=520, height=280)

    # scroll bar
    scrollbar = Scrollbar(billframe, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    # text box
    textarea = Text(billframe, height=18, width=60, yscrollcommand=scrollbar.set)
    textarea.pack()
    scrollbar.config(command=textarea.yview)

    # wrapper3.pack(fill="both", expand="yes",  padx=5, pady=5)
    # wrapper3.place(x=0, y=440, width=1366, height=336)

    root2.mainloop()

#for creating window we have a class Tk()


root=Tk()

root.title("Retail Billing System")

root.geometry('1366x786+0+0')#for set width and height

root.iconbitmap('icon2.ico')#this method used to change widow icon

root.state("zoomed")#for full screen

root.config(bg="gray20")#background
#title
headinglabel=Label(root,text="Retail Billing System",font=("times new roman",30,'bold')
                   ,bg="gray20",fg="gold",bd=12,relief=GROOVE)
#pack
headinglabel.pack(fill=X)

#customer details frame
cus_details_frame=LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold')
                             ,fg='gold',bd=8,relief=GROOVE,bg='gray20')

cus_details_frame.pack(fill=X)

namel=Label(cus_details_frame,text="Name :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
namel.grid(row=0,column=0,padx=20)

nameentry=Entry(cus_details_frame,font=("arial",15),bd=7,width=18)
nameentry.grid(row=0,column=1,padx=8)

#phone number
phonel=Label(cus_details_frame,text="Phone Number :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
phonel.grid(row=0,column=2,padx=20,pady=2)

phoneentry=Entry(cus_details_frame,font=("arial",15),bd=7,width=18)
phoneentry.grid(row=0,column=3,padx=8)

#bill number
billl=Label(cus_details_frame,text="Bill Number :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
billl.grid(row=0,column=4,padx=20,pady=2)

billnumentry=Entry(cus_details_frame,font=("arial",15),bd=7,width=18)
billnumentry.grid(row=0,column=6,padx=8)

#search button
searchbtn=Button(cus_details_frame,text="Search",font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchbtn.grid(row=0,column=7,padx=20,pady=8)

#product details
productsFrame=Frame(root)
productsFrame.pack(fill=X)

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold')
                             ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

#bathsoap
bathsoapL=Label(cosmeticsFrame,text="Bath Soap :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
bathsoapL.grid(row=0,column=0,pady=9,padx=10,sticky="w")

bathsoapE=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapE.grid(row=0,column=1,pady=9,padx=10,sticky="w")
bathsoapE.insert(0,0)
#face cream
facecreamL=Label(cosmeticsFrame,text="Face Cream :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
facecreamL.grid(row=1,column=0,padx=10,sticky="w")

facecreamE=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamE.grid(row=1,column=1,pady=9,padx=10,sticky="w")
facecreamE.insert(0,0)
#face wash
facewashL=Label(cosmeticsFrame,text="Face Wash :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
facewashL.grid(row=2,column=0,padx=10,sticky="w")

facewashE=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashE.grid(row=2,column=1,pady=9,padx=10,sticky="w")
facewashE.insert(0,0)
#hair spray
hairsprayL=Label(cosmeticsFrame,text="Hair Spray :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

hairsprayL.grid(row=3,column=0,padx=10,sticky="w")


hairsprayE=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)

hairsprayE.grid(row=3,column=1,pady=9,padx=10,sticky="w")
hairsprayE.insert(0,0)
#hair gel
hairgelL=Label(cosmeticsFrame,text="Hair Gel :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

hairgelL.grid(row=4,column=0,padx=10,sticky="w")

hairgelE=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)

hairgelE.grid(row=4,column=1,pady=9,padx=10,sticky="w")
hairgelE.insert(0,0)
#body lotion
bodylotionL=Label(cosmeticsFrame,text="Body Lotion :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
bodylotionL.grid(row=5,column=0,padx=10,sticky="w")

bodylotionE=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)

bodylotionE.grid(row=5,column=1,pady=9,padx=10,sticky="w")
bodylotionE.insert(0,0)
#groceryFrame
groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold')
                             ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

#rice
riceL=Label(groceryFrame,text="Rice :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
riceL.grid(row=0,column=0,pady=9,padx=10,sticky="w")

riceE=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceE.grid(row=0,column=1,pady=9,padx=10,sticky="w")
riceE.insert(0,0)
#oil
oilL=Label(groceryFrame,text="Oil :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
oilL.grid(row=1,column=0,padx=10,sticky="w")

oilE=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilE.grid(row=1,column=1,pady=9,padx=10,sticky="w")
oilE.insert(0,0)
#daal
daalL=Label(groceryFrame,text="Dal :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
daalL.grid(row=2,column=0,padx=10,sticky="w")

daalE=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalE.grid(row=2,column=1,pady=9,padx=10,sticky="w")
daalE.insert(0,0)
#Wheat
wheatL=Label(groceryFrame,text="Wheat :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

wheatL.grid(row=3,column=0,padx=10,sticky="w")


wheatE=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)

wheatE.grid(row=3,column=1,pady=9,padx=10,sticky="w")
wheatE.insert(0,0)
#sugar
sugarL=Label(groceryFrame,text="Sugar :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

sugarL.grid(row=4,column=0,padx=10,sticky="w")

sugarE=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)

sugarE.grid(row=4,column=1,pady=9,padx=10,sticky="w")
sugarE.insert(0,0)
#TEA
teaL=Label(groceryFrame,text="Tea :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

teaL.grid(row=5,column=0,padx=10,sticky="w")


teaE=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)

teaE.grid(row=5,column=1,pady=9,padx=10,sticky="w")
teaE.insert(0,0)
#colddrinks frame
colddrinks_Frame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold')
                             ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
colddrinks_Frame.grid(row=0,column=2)

#maaza
maazaL=Label(colddrinks_Frame,text="Maaza :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
maazaL.grid(row=0,column=0,pady=9,padx=10,sticky="w")

maazaE=Entry(colddrinks_Frame,font=('times new roman',15,'bold'),width=10,bd=5)
maazaE.grid(row=0,column=1,pady=9,padx=10,sticky="w")
maazaE.insert(0,0)
#pepsi
pepsiL=Label(colddrinks_Frame,text="Pepsi :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
pepsiL.grid(row=1,column=0,padx=10,sticky="w")

pepsiE=Entry(colddrinks_Frame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiE.grid(row=1,column=1,pady=9,padx=10,sticky="w")
pepsiE.insert(0,0)
#sprite
spriteL=Label(colddrinks_Frame,text="Sprite :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')
spriteL.grid(row=2,column=0,padx=10,sticky="w")

spriteE=Entry(colddrinks_Frame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteE.grid(row=2,column=1,pady=9,padx=10,sticky="w")
spriteE.insert(0,0)
#Dew
dewL=Label(colddrinks_Frame,text="Dew :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

dewL.grid(row=3,column=0,padx=10,sticky="w")


dewE=Entry(colddrinks_Frame,font=('times new roman',15,'bold'),width=10,bd=5)

dewE.grid(row=3,column=1,pady=9,padx=10,sticky="w")
dewE.insert(0,0)
#frooti
frootiL=Label(colddrinks_Frame,text="Frooti :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

frootiL.grid(row=4,column=0,padx=10,sticky="w")

frootiE=Entry(colddrinks_Frame,font=('times new roman',15,'bold'),width=10,bd=5)

frootiE.grid(row=4,column=1,pady=9,padx=10,sticky="w")
frootiE.insert(0,0)
#coca cola
cocL=Label(colddrinks_Frame,text="Coca Cola :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

cocL.grid(row=5,column=0,padx=10,sticky="w")


cocE=Entry(colddrinks_Frame,font=('times new roman',15,'bold'),width=10,bd=5)

cocE.grid(row=5,column=1,pady=9,padx=10,sticky="w")
cocE.insert(0,0)
#bill frame

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)
bill_area_label=Label(billframe,text='Label Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
bill_area_label.pack(fill=X)
  #scroll bar
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

  #text box
textarea=Text(billframe,height=18,width=60,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

#bill menu
billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold')
                             ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack(fill=X)

#cosmetic price
cosmeticprice_L=Label(billmenuFrame,text="Cosmetics Price :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

cosmeticprice_L.grid(row=0,column=0,padx=10,sticky="w")


cosmeticprice_E=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)

cosmeticprice_E.grid(row=0,column=1,pady=6,padx=10,sticky="w")

#grocery price
groceryprice_L=Label(billmenuFrame,text="Grocery Price :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

groceryprice_L.grid(row=1,column=0,padx=10,sticky="w")


groceryprice_E=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)

groceryprice_E.grid(row=1,column=1,pady=6,padx=10,sticky="w")

#colddrinks price
colddrinksprice_L=Label(billmenuFrame,text="Cold Drink Price :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

colddrinksprice_L.grid(row=2,column=0,padx=10,sticky="w")


colddrinksprice_E=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)

colddrinksprice_E.grid(row=2,column=1,pady=6,padx=10,sticky="w")

#cosmetic Tax
cosmetictax_L=Label(billmenuFrame,text="Cosmetic Tax :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

cosmetictax_L.grid(row=0,column=2,padx=10,sticky="w")


cosmetictax_E=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)

cosmetictax_E.grid(row=0,column=3,pady=6,padx=10,sticky="w")

#grocery tax
grocerytax_L=Label(billmenuFrame,text="Grocery Tax :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

grocerytax_L.grid(row=1,column=2,padx=10,sticky="w")


grocerytax_E=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)

grocerytax_E.grid(row=1,column=3,pady=6,padx=10,sticky="w")

#colddrinks tax
colddrinktax_L=Label(billmenuFrame,text="Cold Drink tax :",font=('times new roman',15,'bold'),bg='gray20'
            ,fg='white')

colddrinktax_L.grid(row=2,column=2,padx=10,sticky="w")


colddrinktax_E=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)

colddrinktax_E.grid(row=2,column=3,pady=6,padx=10,sticky="w")
#buttons
buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

#total
totalbtn=Button(buttonFrame,text="Total",font=('arial',16,'bold'),bg="gray20",fg="white"
                ,bd=5,width=7,pady=10,command=total)#command =function name
totalbtn.grid(row=0,column=0,pady=20,padx=5)

#billbtn
billbtn=Button(buttonFrame,text="Bill",font=('arial',16,'bold'),bg="gray20",fg="white"
                ,bd=5,width=7,pady=10,command=bill_area)
billbtn.grid(row=0,column=1,pady=20,padx=5)

#emailbtn
emailbtn=Button(buttonFrame,text="Email",font=('arial',16,'bold'),bg="gray20",fg="white"
                ,bd=5,width=7,pady=10,command=send_email)
emailbtn.grid(row=0,column=2,pady=20,padx=5)

#printbtn
printbtn=Button(buttonFrame,text="Print",font=('arial',16,'bold'),bg="gray20",fg="white"
                ,bd=5,width=7,pady=10,command=print_bill)
printbtn.grid(row=0,column=3,pady=20,padx=5)

#clear
clearbtn=Button(buttonFrame,text="Clear",font=('arial',16,'bold'),bg="gray20",fg="white"
                ,bd=5,width=7,pady=10,command=clr)
clearbtn.grid(row=0,column=4,pady=20,padx=5)
view_btn=Button(buttonFrame,text="Records",font=('arial',16,'bold'),bg="gray20",fg="white"
                ,bd=5,width=7,pady=10,command=view)
view_btn.grid(row=0,column=5,pady=20,padx=5)

root.mainloop()#it helps to viewing window
