from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from hashlib import blake2b


root = Tk()
root.title('Security login')
root.geometry("400x400")
root.configure(background='sea green')
frame1 = Frame(root,bg="sea green")
frame1.grid(row=0,column=0,padx=10, pady=20, sticky=(E, W), columnspan=2)
txt_infologin = 'Logowanie z użyciem klucza zabezpieczającego'
label_info = Label(frame1,text = txt_infologin,bg="sea green",fg='white',font=("Calibri", 14,'bold'))
label_info.grid(row=0,column=0)
btn_select_file = Button(frame1, text = 'Wybierz plik z kluczem',font=("Calibri", 10), command = lambda:select_key_file())
btn_select_file.grid(row=1,column=0,pady=20)

password_in_usb =[]

def select_key_file():
    root.filename = filedialog.askopenfilename(initialdir = "~/",title = "Wybierz plik z kluczem",filetypes =(("Text File", "*.txt"),("All Files","*.*")))
    if root.filename:
        try:
            global plik
            plik = open(root.filename, "r")
            password_in_usb.append(str(plik.read()))
            add_login_form()
        except: pass

def koder_input(haslo):
    blake = blake2b(digest_size=45)
    blake.update(haslo.encode())
    kod_input = blake.hexdigest()
    return kod_input

def add_login_form():
    try:
        frame2 = Frame(root, bg="sea green")
        frame2.grid(row=1, column=0, padx=10, pady=20, sticky=N, columnspan=2)
        label_login = Label(frame2, text='Nazwa użytkownika',font=("Calibri", 12),bg="sea green",fg='white')
        label_login.grid(padx=5, pady=5, sticky=(E, W))
        entry_login= Entry(frame2, font=("Calibri", 11,), width=20)
        entry_login.grid(padx=5, pady=5, sticky=N)
        label_pswd = Label(frame2, text='Hasło', font=("Calibri", 12),bg="sea green",fg='white')
        label_pswd.grid(padx=5, pady=5, sticky=(E, W))
        global entry_pswd
        entry_pswd = Entry(frame2, show="*", font=("Calibri", 11,), width=20)
        entry_pswd.grid(padx=5, pady=5, sticky=N)
        ok_btn = Button(frame2, text='Zaloguj',font=("Calibri", 10),command = lambda: compare_pswd())
        ok_btn.grid(padx=5, pady=45, sticky=N)
        root.bind('<Return>',func=compare_pswd)
    except: pass

def compare_pswd(*args):
    password_input = koder_input(entry_pswd.get())
    if str(password_input) == password_in_usb[0] :
        messagebox.showinfo(title='Login',message='Login succes')
    else: messagebox.showwarning(title='Login', message='Acces denied')

root.mainloop()