import base64
from tkinter import *
from tkinter import messagebox

FONT = ("Comic Sans MS", 12)
WHITE = "white"
DENIM = "#151E3D"
PERIWINKLE = "#CCCCFF"

def encrypt():
    password=code.get()
    if password == "1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg=PERIWINKLE)

        message = text1.get(1.0,END)
        encrypted_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encrypted_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text="Plaintext has been encrypted!", font=FONT, fg=PERIWINKLE).place(x=5,y=6)
        text2 = Text(screen1, font="30", bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)

    elif (password == ""):
        messagebox.showerror("ERROR!", "Please enter the secret key")
    elif (password != "1234"):
        messagebox.showerror("DENIED!", "Invalid secret key")

def decrypt():
    password=code.get()
    if password == "1234":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x250")
        screen2.configure(bg=PERIWINKLE)

        message = text1.get(1.0,END)
        encrypted_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encrypted_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2,text="Plaintext has been decrypted!", font=FONT, fg=PERIWINKLE).place(x=5,y=6)
        text2 = Text(screen2, font="30", bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)

    elif (password == ""):
        messagebox.showerror("ERROR!", "Please enter the secret key")
    elif (password != "1234"):
        messagebox.showerror("DENIED!", "Invalid secret key")
    else:
        pass

def clear():
    text1.delete(1.0,END)
    code.set("")

screen = Tk() # Window
screen.geometry("420x420")
screen.title("Encryption and Decryption Application")
screen.configure(bg="black")

Label(screen, text="Enter Plaintext", font=FONT, bg=WHITE).place(x=5,y=8)
text1 = Text(screen,font="20")
text1.place(x=5, y=45, width=410, height= 150)

Label(screen,text="Enter Secret Key", font=FONT).place(x=155,y=210)

code=StringVar()
Entry(textvariable=code,bd=4,font="28",show="•").place(x=120,y=250)

Button(screen,text="ENCRYPT",font=FONT, bg=DENIM, fg=WHITE, command=encrypt).place(x=65,y=300,width=150)
Button(screen,text="DECRYPT",font=FONT, bg=DENIM, fg=WHITE, command=decrypt).place(x=225,y=300,width=150)
Button(screen,text="CLEAR",font=FONT, bg=DENIM, fg=WHITE, command=clear).place(x=145,y=350,width=150)

mainloop()
