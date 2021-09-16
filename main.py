from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import DataBaser
import verify
import time

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tesseract - Account login")
        self.geometry("325x500")
        self.resizable(0,0)
        self.attributes("-alpha", 0.92)

        self.iconbitmap('.\TesseractICON.ico')
        self.logo = PhotoImage(file=".\Tesseract.png")

        ### Setting window position
        w = 325 # width for the Tk root
        h = 500 # height for the Tk root

        # Get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        # Calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # Set the dimensions of the screen and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        ### Setting background color
        j = 0

        for i in range(60):
            color = str(222240+i)
            self.backgroundFrame = Frame(self, width=30, height=500, bg= '#'+color).place(x=j, y=0)
            j = j+5

        ### MainFrame
        self.mainFrame = Frame(self, width=225, height=400, bg="#d3d9e3").place(x=50, y=50)
        self.WelcomeText = Label(self.mainFrame, text='Welcome\nto', font='Play 14',bg="#d3d9e3", fg="Black")
        self.WelcomeText.place(x=120, y=65)
        self.TesseractText = Label(self.mainFrame, text='Tesseract',font='Play 28 bold',bg="#d3d9e3", fg="Black")
        #self.TesseractText.place(x=70, y=115)
        self.Logo = Label(self.mainFrame,bg="#d3d9e3", image=self.logo)
        #self.Logo.place(x=130, y=160)

        for i in range(10):
            self.TesseractText.place(x=70, y=65+(i*5))#y=65
            self.TesseractText.update()
            self.Logo.place(x=208-(i*8.8), y=160)
            self.Logo.update()
            time.sleep(0.03)

        ### User
        self.UsernameText = Label(self.mainFrame, text='Username:', font='Play 12',bg="#d3d9e3", fg="Black")
        self.UsernameText.place(x=55, y=260)
        self.UsernameEntry = Entry(self.mainFrame, width=20, background="#d3d9e5", border=0)
        self.UsernameEntry.place(x=140, y=263)
        self.underLine1 = Frame(self.mainFrame, width=120, height=1, bg="black")
        self.underLine1.place(x=141, y=280)

        ### Pass
        self.PassEntry = StringVar()
        self.PasswordText = Label(self.mainFrame, text='Password:', font='Play 12',bg="#d3d9e3", fg="Black")
        self.PasswordText.place(x=55, y=300)
        self.PasswordEntry = Entry(self.mainFrame, width=20, textvariable=self.PassEntry,show="*", background="#d3d9e5", border=0)
        self.PasswordEntry.place(x=140, y=303)
        self.underLine2 = Frame(self.mainFrame, width=120, height=1, bg="black")
        self.underLine2.place(x=141, y=320)
        self.PassForgot = Button(self.mainFrame, command=self.passwordForgot, text='Forgot your password?', font='Play 7', background="#d3d9e5", foreground="#222240", border=0)
        self.PassForgot.place(x=162, y=330)

        ### Buttons
        self.bind('<Return>', lambda event:self.loginBnt())
        self.LoginButton = ttk.Button(self.mainFrame, command=self.loginBnt,text='Login', width=15)
        self.LoginButton.place(x=110, y=380)
        self.RegisterButton = ttk.Button(self.mainFrame, command=self.registerBnt,text='Register', width=15)
        self.RegisterButton.place(x=110, y=410)

    def passwordForgot(self):
        if(self.UsernameEntry.get() == ""):
            messagebox.showerror(title="Tesseract - Error", message="Enter your username first")
        else:
            try:
                DataBaser.cursor.execute("""
                SELECT Username FROM Users
                WHERE Username = ?
                """, (self.UsernameEntry.get(),))
                VerifyPasswordForgot = DataBaser.cursor.fetchone()
                
                if(self.UsernameEntry.get() in VerifyPasswordForgot):
                    # Send an email and
                    messagebox.showinfo(title="Tesseract - Forgot your password?", message="A message has been sent to your email")

            except:
                    messagebox.showwarning(title="Tesseract - Warning", message="This username does not exist")

    def loginBnt(self):
        if(self.UsernameEntry.get() == "" or self.PasswordEntry.get() == ""):
            messagebox.showerror(title="Tesseract - Error", message="Username and Password must not be empty")
        else:
            try:
                #print(event.keysym)
                DataBaser.cursor.execute("""
                SELECT Password FROM Users
                WHERE Username = ?
                """, (self.UsernameEntry.get(),))
                VerifyLogin = DataBaser.cursor.fetchone()

                if(self.PasswordEntry.get() in VerifyLogin):
                    self.destroy()
                    self.welcome = Welcome()
                    self.welcome.mainloop()
                else:
                    messagebox.showinfo(title="Tesseract - Login info", message="Incorrect Password!")
            except:
                messagebox.showinfo(title="Tesseract - Login info", message="Access denied!\nUsername or Password incorrect")

    def registerBnt(self):
        # Setting new window...
        self.title("Tesseract - Account Register")
        self.WelcomeText.place(x=999)
        self.Logo.place(x=999)
        self.PassForgot.place(x=999)
        self.LoginButton.place(x=999)
        self.RegisterButton.place(y=999)
        
        for i in range(10):
            self.TesseractText.place(y=115-(i*5))#y=65
            self.TesseractText.update()
            time.sleep(0.03)

        self.RegisterText = Label(self.mainFrame, text="Register your account", font='Play 11',bg="#d3d9e3", fg="Black")
        self.RegisterText.place(x=90, y= 130)

        self.EmailText = Label(self.mainFrame, text='Email:', font='Play 12',bg="#d3d9e3", fg="Black")
        self.EmailText.place(x=70, y=180)
        self.EmailEntry = Entry(self.mainFrame, width=20, background="#d3d9e5", border=0)
        self.EmailEntry.place(x=140, y=183)
        self.underLine3 = Frame(self.mainFrame, width=120, height=1, bg="black")
        self.underLine3.place(x=141, y=200)

        self.BirthText = Label(self.mainFrame, text='Birth date:', font='Play 12',bg="#d3d9e3", fg="Black")
        self.BirthText.place(x=60, y=220)
        self.BirthEntry = Entry(self.mainFrame, width=20, background="#d3d9e5", border=0)
        self.BirthEntry.place(x=140, y=223)
        self.underLine4 = Frame(self.mainFrame, width=120, height=1, bg="black")
        self.underLine4.place(x=141, y=240)

        self.BirthInfo = Label(self.mainFrame, text='(mm/dd/yyyy)', font='Play 7',bg="#d3d9e3", fg="Black")
        self.BirthInfo.place(x=62, y=238)

        #Buttons
        self.RegisterRegisterButton = ttk.Button(self.mainFrame, command=self.registerRegisterBnt,text='Register', width=15)
        self.RegisterRegisterButton.place(x=110, y=380)
        self.Back = ttk.Button(self.mainFrame, command=self.backBnt,text='Back', width=15)
        self.Back.place(x=110, y=410)

    def registerRegisterBnt(self):
        if(not verify.is_any_none(self.EmailEntry.get(), self.BirthEntry.get(), self.UsernameEntry.get(), self.PasswordEntry.get()) and 
        verify.email(self.EmailEntry.get()) and
        verify.birth(self.BirthEntry.get()) and
        not verify.username_inDataBase(self.UsernameEntry.get()) and
        verify.password(self.PasswordEntry.get())):
            try:
                DataBaser.cursor.execute("""
                INSERT INTO Users(Email, Birth, Username, Password) VALUES(?, ?, ?, ?)
                """, (self.EmailEntry.get(), self.BirthEntry.get(), self.UsernameEntry.get(), self.PasswordEntry.get()))
                DataBaser.conn.commit()
                messagebox.showinfo(title="Tesseract - Register info", message="Resgiter confirmed")
            except:
                messagebox.showerror(title="Tesseract - Error", message="Something went wrong, try again")

    def backBnt(self):
        self.title("Tesseract - Account Login")
        #self.Logo.place(x=130)
        self.UsernameText.place(y=260)
        self.UsernameEntry.place(y=263)
        self.underLine1.place(y=280)
        self.PassForgot.place(x=162)
        self.LoginButton.place(x=110)
        self.RegisterButton.place(y=410)
        #
        self.RegisterText.place(x=999)
        self.EmailText.place(x=999)
        self.EmailEntry.place(x=999)
        self.underLine3.place(x=999)
        self.BirthText.place(x=999)
        self.BirthEntry.place(x=999)
        self.underLine4.place(x=999)
        self.BirthInfo.place(x=999)
        self.RegisterRegisterButton.place(x=999)
        self.Back.place(x=999)
        
        for i in range(10):
            self.TesseractText.place(y=65+(i*5))#y=65
            self.TesseractText.update()
            self.Logo.place(x=208-(i*8.8))
            self.Logo.update()
            time.sleep(0.03)

        self.WelcomeText.place(x=120)

class Welcome(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.geometry("500x350")
        self.attributes("-alpha", 0)
        self.wm_attributes('-transparentcolor', 'Black')
        self.overrideredirect(True)

        w = 500 # width for the Tk root
        h = 350 # height for the Tk root

        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        text = "W e l c o m e\nt o\nT e s s e r a c t"
        self.Frame = Frame(self, width=500, height=350, bg="#d3d9e5").place(x=0, y=0)
        self.WelcomeText = Label(self, text=text, font='Play 40 bold', fg="#222280", bg="#d3d9e5")
        self.WelcomeText.place(x=75, y=60)
        self.RegisterButton = Button(self, command=self.fade_out, text='Enter', font='Play 10 bold',width=10, bg="#d3d9e5", borderwidth="0")
        self.RegisterButton.place(x=210, y=280)
        self.fade_in()

    def fade_in(self):
        alpha = self.attributes("-alpha")
        alpha = min(alpha + .01, 1.0)
        self.attributes("-alpha", alpha)
        if alpha < 1.0:
            self.after(10, self.fade_in)
            
    def fade_out(self):
        alpha = self.attributes("-alpha")
        if alpha > 0:
            alpha -= 0.1
            self.attributes("-alpha", alpha)
            self.after(10, self.fade_out)
        else:
            self.destroy()

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
    DataBaser.conn.close()