#Import the required Libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("450x250")
win.title('Encrypter')
win.resizable(0,0)
win.configure(background="gray")

lbl_path = Label(win,text = "Path: \"\"",fg = "gray")

def prompt_pass_popup():
    # Create a new window for the pop-up
    popup = Toplevel(win)
    popup.title("Enter passpharse")
    popup.configure(background="gray")

    # Add some content to the pop-up
    lbl_epass = Label(popup, text="Enter passpharse",background="gray")
    fld_pass = Entry(popup,
                        show="*")
    lbl_repass = Label(popup, text="Re-Enter passpharse",background="gray")
    fld_pass_confirm = Entry(popup,
                        show="*")
    btn_check = Button(popup,
                       text="Check")
    lbl_epass.pack()
    fld_pass.pack(padx=10)
    lbl_repass.pack()
    fld_pass_confirm.pack()
    btn_check.pack(padx=10,pady=20)

    # Wait for the pop-up to be closed before continuing
    popup.wait_window()

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",)
      
    # Nastavíme text dialog na otevřený soubor
    lbl_path.configure(text=f"File Opened: {os.path.dirname(filename)}\n{os.path.basename(filename)}")

btn_getfile = Button(win,
                        text = "Choose File",
                        command = browseFiles)
lbl_passinfo = Label(win,
                        text="",
                        pady=5,)

btn_encrypt = Button(win,
                        text = "Encrypt",
                        command= prompt_pass_popup)
btn_deencrypt = Button(win,
                        text = "Decrypt")


#label_file_explorer.grid(column = 1, row = 2,)
#button_explore.grid(column = 1, row = 5,)
#button_test.grid(column=0, row=6, columnspan=2, pady=10)
lbl_path.pack()
btn_getfile.pack()
lbl_passinfo.pack()
btn_encrypt.pack(side="left",anchor="n",padx=80)
btn_deencrypt.pack(side="right",anchor="n",padx=80)

win.mainloop()