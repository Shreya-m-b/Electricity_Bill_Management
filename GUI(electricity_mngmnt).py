from tkinter import*

from tkinter import messagebox as mb
root=Tk()

def request():
    if mb.askyesno("accept","We would request you to go through the terms and conditions before proceeding further."):
        mb.showinfo("confirmation","Thank you for your great generosity!\n You get lessons from the worst days, and memories from the best days.\n\t TODAY WILL BE A GOOD DAY!!!!")
    else:
        mb.showinfo("confirmation","HAVE A GOOD DAY!!")
        
def callback():
    if mb.askyesno("Verify","Do u really want to quit?"):
        mb.showinfo("Quit","Thank you!")
    else:
        mb.showinfo("No","good choice")
        
l1=Label(root,text="Our Community is enjoying uninterrupted 24/7 power supply due to highly dedicated service rendered by the BESCOM employees.\nThere are many lineman workers,elctritians who have lost lives due to accidents during working hours. \nThough their precious lives are irreplacable their dependents are given compensation.\n\nWe would hereby request you to contritube Rs.1 towards the accident relief fund",bg="white",fg="black").pack()
b1=Button(root,text="accept",command=request).pack(fill=X)
b2=Button(root,text="Quit",command=callback).pack(fill=X)

def feed():
    l1=Label(root,text="please give your feedback").pack()
    e=Entry(root,width=100).pack(fill=X)
    b24=Button(root,text='submit feedback',command=submit2).pack()
    
def submit2():
    mb.showinfo('feedback','We have recieved ur feed back.Thank You!!!!')
b3=Button(root,text="Feedback section",command=feed).pack()

def submit():
    msg='You have rated us'+str(scale.get())+".Thank you"
    mb.showinfo("Submission of rating",message=msg)
scale=Scale(root,from_=0,to=5,orient=HORIZONTAL,tickinterval=0.5,length=800,resolution=0.5)
scale.pack()
b3=Button(root,text="submit",command=submit).pack()

def openfile():
    mb.showinfo('Open','No files exist!')
def save():
    mb.showinfo('Save','You bill and related data is saved')

menubar=Menu(root)
root.config(menu=menubar)
fileMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openfile)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root.geometry('300x200')
root.title('Combobox Widget')

label = ttk.Label(text="Please choose your bank:")
label.pack(fill=tk.X, padx=5, pady=5)

selected_bank = tk.StringVar()
BANK = ttk.Combobox(root, textvariable=selected_bank)

BANK['values'] = [' HDFC Bank','ICICI Bank','Axis Bank','Indian Bank']

BANK['state'] = 'readonly'
BANK.pack(fill=tk.X, padx=5, pady=5)

def bankinfo(event):
    if mb.askyesno("proceed",f"You have selected {selected_bank.get()}!"):
        mb.showinfo('OTP','Login to official BESCOM website with valid credentials. Your One Time Password/OTP is 12385')
    else:
        mb.showinfo('Cancelletion',"PERMISSION DENIED! OTP generation request cancelled")
   # showinfo(title='Result', message=f'You selected {selected_bank.get()}!')

BANK.bind('<<ComboboxSelected>>', bankinfo)
root.mainloop()

root.mainloop()