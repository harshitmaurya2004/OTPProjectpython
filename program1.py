from tkinter import *
from program2 import *
from subprocess import call

class Generate_otp(Tk):
def __init__(self):
super().__init__()
self.geometry("1000x580+200+80")
self.configure(bg = "#FFFFFF")
self.resizable(False, False)

def Labels(self):
self.upper_frame = Frame(self, bg="#4682B4", width=1500, height=130)
self.upper_frame.place(x=0, y=0)
self.picture = PhotoImage(file="password1.png")
self.k = Label(self.upper_frame, image=self.picture, bg="#4682B4").place(x=220, y=35)

self.j = Label(self.upper_frame, text="OTP Verification", font="TimesNewRoman 38 bold", bg="#4682B4", fg="white").place(x=330, y=35)
self.a = Label(self, text="OTP is valid for 10 minutes.", font="TimesNewRoman 14", bg="#4682B4", fg="white").place(x=360, y=290)
self.b = Label(self, text="Click on the Generate OTP button to generate OTP.", font="TimesNewRoman 14", bg="#4682B4", fg="white").place(x=260, y=338)

def Buttons(self):
self.GenerateOTP = PhotoImage(file="Generate_OTP.png")
self.generatebutton = Button(self, image=self.GenerateOTP, command=self.Open, border=0)
self.generatebutton.place(x=390, y=390)

def Open(self):
self.destroy()
call(["python", "program2.py"])

if __name__ == "__main__":
window = Generate_otp()
window.Labels()
window.Buttons()
window.mainloop()
