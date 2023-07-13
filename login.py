from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
import requests
from twilio.rest import Client
import keys
client=Client(keys.account_sid,keys.auth_token)

global USERNAME
global PASSWORD
USERNAME=[]
PASSWORD=[]


root = tk.Tk()
root.title("Login")
root.geometry("1000x500")
root.configure(bg="black")

img = PhotoImage(file="Login.png")
Label(root,image=img,bg='black',padx=50,pady=50).place(x=100,y=100)
frame = Frame(root,width=350,height=350,bg='black')
frame.place(x=480,y=70)

heading = Label(frame,text="Sign In",fg="gray", bg="black", font="bold", padx=10, pady=10)
heading.place(x=150,y=5)


def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name==" ":
        user.insert(0,'Username')

user=Entry(frame,width=25,fg="white",border=3,bg="black",font="bold")
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

def on_enter1(e):
    code.delete(0,'end')

def on_leave1(e):
    name=code.get()
    if name==" ":
        code.insert(0,'Password')

code=Entry(frame,width=25,fg="white",border=3,bg="black",font="bold")
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter1)
code.bind('<FocusOut>',on_leave1)

def sign_in():
    username=user.get()
    password=code.get()
    if username in USERNAME and password in PASSWORD:
        print("Welcome")
        screen=Toplevel(root)
        screen.title("Crypto GUI")
        screen.geometry("1300x700")
        screen.configure(bg="white")
        my_label=Label(screen,text="Enter Buy Price",bg="white", fg="green", font=("helevetica",25))
        my_label.place(x=50,y=50)
        buy_price=StringVar()
        inp=Entry(screen,text=buy_price,border=10,width=15,font=("helvetica",25))
        inp.place(x=50,y=120)

        my_label=Label(screen,text="Select the currency",bg="white",fg="green",font=("helvetica",25))
        my_label.place(x=50,y=210)

        def call_back(selection):
            curr=selection
            print(curr)
            return curr
        variable = StringVar(screen)
        variable.set("CURRENCY")
        option= OptionMenu(screen,variable,"USD","INR","EUR",command=call_back)
        option.place(x=50,y=280)

        currency="INR"

        my_label = Label(screen,text="Click the button to check Market price",bg="white",fg="green",font=("helvetica",25))
        my_label.place(x=500,y=50)

        def price_check():
            url=("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={}".format(currency.upper()))
            response=requests.request("GET",url)
            response=json.loads(response.text)
            current_price=response[currency.upper()]
            m_entry = Entry(screen,text="Market Price",bg="white",fg="green",width=15,bd=10,font=("helvetica",25))
            m_entry.place(x=600,y=200)
            m_entry.delete(0,'end')
            m_entry.insert(0,current_price)
            return current_price
        market_price = price_check()

        button=Button(screen,text="Market price",border=10,width=15,font=("helvetica",25),command=price_check)
        button.place(x=600,y=100)

        def check_status():
            x=buy_price.get()
            b=int(x)
            if(b>market_price):
                e.delete(0,'end')
                e.insert(0,"You can buy now")
                message=client.messages.create(body="You can buy now",from_=keys.twilio_account,to=keys.my_number)
            else:
                e.delete(0,'end')
                e.insert(0,"Sell to book profit")
                message=client.messages.create(body="Sell to book profit",from_=keys.twilio_account,to=keys.my_number)
        status_button = Button(screen,text="Check Status",border=10,width=15,font=("helvetica",25),command=check_status)
        status_button.place(x=50,y=450)

        e=Entry(screen,width=25,bg="white",font=("helvetica",25),bd=10)
        e.place(x=500,y=450)  
                       
    else:
        messagebox.showinfo("Info","Incorrect Username or Password")


button = Button(frame,width=10,pady=7,text="Sign In", bg="blue", fg="white",border=10, command = sign_in)
button.place(x=30,y=204)

def register():
    screen=Toplevel(root)
    screen.title("Register GUI")
    screen.geometry("1000x500")
    screen.configure(bg="white")

    user_label=Label(screen,text="Choose Username:",bg="white", fg="black", font=("helevetica",25))
    user_label.place(x=50,y=50)
    code_label=Label(screen,text="Choose Password:",bg="white", fg="black", font=("helevetica",25))
    code_label.place(x=50,y=150)

    user_entry = Entry(screen,bg="white",fg="green",width=15,bd=10,font=("helvetica",25))
    user_entry.place(x=400,y=50)
    code_entry = Entry(screen,bg="white",fg="green",width=15,bd=10,font=("helvetica",25))
    code_entry.place(x=400,y=150)

    
    def change_credentials():
        USERNAME.append(user_entry.get())
        PASSWORD.append(code_entry.get())

    button = Button(screen,width=10,pady=7,text="Save", bg="blue", fg="white",border=3, command=change_credentials)
    button.place(x=300,y=300)
                                                                                                                   

button = Button(frame,width=10,pady=7,text="Register", bg="blue", fg="white",border=10, command = register)
button.place(x=220,y=204)

root.mainloop()























