#Imprtujeme potřebné moduly
from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
import os
# Vytvoříme instanci Tkinteru
win = Tk()
# Nastavíme velikost okna a vlastnosti
win.geometry("250x100")
win.title('Encrypter')
win.resizable(0,0)
win.configure(background="gray")

## Funkce pro zobrazení popupu s informací o úspěšném dokončení
def Succes(path = None):
    global filepath # Nastavíme globální proměnnou filepath
    succpopup = Toplevel(win) # Vytvoříme nové okno
    succpopup.title("Succes") # Nastavíme titulek okna
    succpopup.configure(background="gray") # Nastavíme barvu pozadí okna
    if path != None:
        lbl_succ = Label(succpopup, text=f"Succesfully encrypted file!\n\n Path to file: {filepath}.key",background="gray") # Vytvoříme label s textem při uspesném dokončení
    else:
        lbl_succ = Label(succpopup, text=f"Succesfully decrypted file!",background="gray") # Vytvoříme label s textem při uspesném dešifrování
    btn_ok = Button(succpopup,text="OK",command=lambda: succpopup.destroy()) # Vytvoříme tlačítko pro zavření okna

    # Umístíme widgety do okna
    lbl_succ.pack(padx=10,pady=20)
    btn_ok.pack(padx=10,pady=20)
    btn_encrypt.configure(state="disabled")
    btn_deencrypt.configure(state="disabled")

    lbl_path.configure(text=f"Loaded file: <None!>") # Nastavíme text o nahraném souboru na <None!> protože už žádný není nahraný
    filepath = None

## Funkce pro šifrování souboru
def encrypt():
    global filepath # Nastavíme globální proměnnou filepath
    btn_encrypt.configure(state="disabled") # Vypneme tlačítko pro šifrování a dešifrování
    btn_deencrypt.configure(state="disabled")

    rawkey = Fernet.generate_key() # Vygenerujeme klíč
    with open(filepath+".key", 'wb') as mykey:
        mykey.write(rawkey) # Uložíme klíč do souboru

    f = Fernet(rawkey) # Vytvoříme instanci Fernetu

    with open(filepath, 'rb') as org_file: # Otevřeme soubor který chceme šifrovat
        original = org_file.read()
        org_file.close()

    encrypted = f.encrypt(original) # Zašifrujeme soubor

    with open (filepath, 'wb') as encrypted_file: # Uložíme zašifrovaný soubor
        encrypted_file.write(encrypted)
        encrypted_file.close()
        Succes(filepath) # Zavoláme funkci pro zobrazení popupu s informací o úspěšném dokončení
        filepath = None # Nastavíme filepath na None

## Funkce pro dešifrování souboru
def decrypt():
    btn_encrypt.configure(state="disabled") # Vypneme tlačítko pro šifrování
    with open(filepath+".key", 'rb') as file: # Otevřeme soubor s klíčem
        rawkey = file.read()
        file.close()

    f = Fernet(rawkey) # Vytvoříme instanci Fernetu

    with open(filepath, 'rb') as org_file: # Otevřeme soubor který chceme dešifrovat
        original = org_file.read()
        org_file.close()

    decrypted = f.decrypt(original) # Dešifrujeme soubor

    with open(filepath, 'wb') as encrypted_file: # Uložíme dešifrovaný soubor
        encrypted_file.write(decrypted)
        encrypted_file.close()
        os.remove(filepath+".key") # Smažeme soubor s klíčem
        Succes() # Zavoláme funkci pro zobrazení popupu s informací o úspěšném dokončení

## Funkce pro otevření dialogu pro výběr souboru
def browseFiles():
    global filepath
    filepath = filedialog.askopenfilename(initialdir = "/",title = "Select a File")
      
    # Nastavíme text dialog na otevřený soubor
    if filepath == "":
        lbl_path.configure(text=f"Loaded file: <None!>")
        btn_encrypt.configure(state="disabled")
        btn_deencrypt.configure(state="disabled")
    else:
        lbl_path.configure(text=f"Loaded file: {os.path.basename(filepath)}")
        btn_encrypt.configure(state="normal")
        btn_deencrypt.configure(state="normal")

# Vytvoříme potřebné widgety
lbl_path = Label(win,text = "Loaded file: <None!>",fg = "black") #Text který ukazuje otevřený souábor
btn_getfile = Button(win,text = "Choose File",command = browseFiles) # Tlačítko pro otevření dialogu pro výběr souboru
btn_encrypt = Button(win,text = "Encrypt",command= encrypt,state="disabled") # Tlačítko pro šifrování
btn_deencrypt = Button(win,text = "Decrypt",command= decrypt,state="disabled") # Tlačítko pro dešifrování

# Umístíme widgety do okna
lbl_path.pack()  
btn_getfile.pack(pady=10)
btn_encrypt.pack(side="left",anchor="n",padx=10)
btn_deencrypt.pack(side="right",anchor="n",padx=10)

# Spustíme hlavní smyčku
win.mainloop()