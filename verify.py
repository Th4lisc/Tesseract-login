from tkinter import messagebox
import DataBaser
import datetime

def is_any_none(Email, Birth, Username, Password):
    if(Email == "" or Birth == "" or Username == "" or Password == ""):
        messagebox.showerror(title="Tesseract - Error", message="Don't leave any blank empty")
        return True
    else:
        return False

def email(Email):
    if('@' in Email):
        return True
    else:
        messagebox.showinfo(title="Tesseract - Register Info", message="Wrong email format")
        return False

def birth(Birth):
    try:
        date = datetime.datetime.strptime(Birth, '%m/%d/%Y')
        return True
    except:
        messagebox.showinfo(title="Tesseract - Register Info", message="Wrong date format, use mm/dd/yyyy")
        return False

def username_inDataBase(Username):
    try:
        DataBaser.cursor.execute("""
        SELECT Username FROM Users
        WHERE Username = ?
        """, (Username,))
        VerifyUsername = DataBaser.cursor.fetchone()

        if(Username in VerifyUsername):
            messagebox.showinfo(title="Tesseract - Register info", message="Your username already exist")
            return True
    except:
        return False

def password(Password):
    if(len(Password) < 4):
        messagebox.showinfo(title="Tesseract - Register Info", message="Your password is too short")
        return False
    else:
        return True
