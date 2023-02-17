# ------ Imports ------
import random as r
import string
# string.ascii_letters => from a-z upper and lower
# string.digits => from 0 to 9
# string.punctuation => simbols, ex: @!,.
from tkinter import *
# ------ EndImports ------

# ------ Functions ------
def generatepassword():
    # len from the entry (string)
    len_str = asklen.get()

    if len_str:
        # if there is a character, then convert it into interger
        length = int(len_str)

        # determine the password requirements
        if (addnumbers()):
            if (addsimbols()):
                # strongest
                characters = string.ascii_letters + string.digits + string.punctuation
                pswd = ''.join(r.choice(characters) for i in range(length))
            else:
                characters = string.ascii_letters + string.digits
                pswd = ''.join(r.choice(characters) for i in range(length))
        else:
            if (addsimbols()):
                characters = string.ascii_letters + string.punctuation
                pswd = ''.join(r.choice(characters) for i in range(length))
            else:
                characters = string.ascii_letters
                pswd = ''.join(r.choice(characters) for i in range(length))

        # reset the CheckButtons
        numbers.set(0)
        simbols.set(0)
        asklen.delete(0, "end")

        # show the password
        password.config(text="Your password is: " + pswd)

    else:
        # reset the CheckButtons
        numbers.set(0)
        simbols.set(0)
        asklen.delete(0, "end")

        # else, print(error)
        password.config(text="Error: type a valid length => *must be interger*")

def addnumbers():
    if(numbers.get()):
        return True
    else:
        return False

def addsimbols():
    if (simbols.get()):
        return True
    else:
        return False

# ------ EndFunctions ------

# ------ Root ------
root = Tk()
root.geometry("480x250")
root.title("password generator")
root.iconbitmap("key.ico")
root.resizable(True, False)
# ------ EndRoot ------

# ------ Frame ------
frame = Frame(root)
frame.pack(fill="both", expand=1)
# ------ EndFrame ------

# ------ Welcome ------
Label(frame, text="Welcome to the password generator!").pack(anchor="w")
Label(frame, text="").pack(anchor="w")
# ------ EndWelcome ------

# ------ ask for length ------
Label(frame, text="Digit the length of the password").pack(anchor="w")
asklen = Entry(frame, justify="left")
asklen.pack(anchor="w")
# ------ End ask for length ------

# ------ CheckButtons ------
# variables
numbers = IntVar()  # 1 = yes, 0 = no
simbols = IntVar()  # 1 = yes, 0 = no

# checkbutton
Label(frame, text="Check the options you want").pack(anchor="w")
Checkbutton(frame,  text="Numbers", variable=numbers, onvalue=1, offvalue=0, command=addnumbers).pack(anchor="w")
Checkbutton(frame,  text="Simbols", variable=simbols, onvalue=1, offvalue=0, command=addsimbols).pack(anchor="w")
Label(frame, text="Note: Letters are selected by default").pack(anchor="w")
Label(frame, text="").pack(anchor="w")
# ------ EndCheckButtons ------

# ------ Button ------
btn = Button(root, text="Create password", command=generatepassword)
btn.pack(anchor="w")
btn.config(bg='lightgray')
# ---- EndButton ----

# ------ Label ------
password = Label(frame)
password.pack(anchor="w")
# ------ EndLabel ------

# mainloop
root.mainloop()