import customtkinter

dict={"Chinmay Verma":"Chunwar1234@","skdon":"skdon1234@"}

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def show_password():
    password_window=customtkinter.CTk()
    x=dropdown.get()
    word=dict.get(x)
    frame=customtkinter.CTkFrame(master=password_window)
    frame.pack(padx=60,pady=20,fill="both",expand=True)
    label=customtkinter.CTkLabel(master=frame, text=word, font=("Arial",18))
    label.pack(padx=20,pady=20)
    password_window.mainloop()

def submit_button():
    dict[username.get()]=password.get()
    create_window.destroy()
    print(dict)

def create():
    global create_window
    create_window=customtkinter.CTk()
    create_window.title("Create Account")
    create_window.geometry("500x350")
    create_window.minsize(500,350)
    create_window.maxsize(500,350)

    frame=customtkinter.CTkFrame(master=create_window)
    frame.pack(padx=60,pady=20,fill="both",expand=True)

    label=customtkinter.CTkLabel(master=frame,text="Account", font=("Arial", 24))
    label.pack(padx=20,pady=20)
    global username
    username=customtkinter.CTkEntry(master=frame, placeholder_text="Username",font=("Arial",18))
    username.pack(padx=20,pady=20)
    global password
    password=customtkinter.CTkEntry(master=frame, placeholder_text="Password",show="•",font=("Aria;",18))
    password.pack(padx=20,pady=20)
    submit=customtkinter.CTkButton(master=frame,text="Submit",font=("Arial",18),command=submit_button)
    submit.pack(padx=20,pady=20)

    create_window.mainloop()

def look():
    look_window=customtkinter.CTk()
    look_window.title("Show Password Window")
    look_window.geometry("500x350")
    look_window.minsize(500,350)
    look_window.maxsize(500,350)
    frame=customtkinter.CTkFrame(master=look_window)
    frame.pack(padx=60,pady=20,fill="both",expand=True)
    label=customtkinter.CTkLabel(master=frame,text="Choose Username", font=("Arial",18))
    label.pack(padx=20,pady=20)
    global dropdown
    dropdown=customtkinter.CTkComboBox(master=frame)
    dropdown.set("")
    options=dict.keys()
    dropdown.configure(values=options)
    dropdown.pack(padx=20,pady=20)      
    button=customtkinter.CTkButton(master=frame,text="Submit Username", font=("Arial",18),command=show_password)
    button.pack(padx=20,pady=20)
    look_window.mainloop()


def check():
    if master_password.get()=="Chunwar1234@":
        look()
    else:
        look_window=customtkinter.CTk()
        look_window.title("Show Password Window")
        look_window.geometry("500x350")
        look_window.minsize(500,350)
        look_window.maxsize(500,350)
        frame=customtkinter.CTkFrame(master=look_window)
        frame.pack(padx=60,pady=20,fill="both",expand=True)
        test=customtkinter.CTkLabel(text="Wrong password enter password again",font=("Arial",18))
        test.pack(padx=20,pady=20)
        look_window.mainloop()


def master_password():
    look_window=customtkinter.CTk()
    look_window.title("Show Password Window")
    look_window.geometry("500x350")
    look_window.minsize(500,350)
    look_window.maxsize(500,350)
    frame=customtkinter.CTkFrame(master=look_window)
    frame.pack(padx=60,pady=20,fill="both",expand=True)
    label_password=customtkinter.CTkLabel(master=frame,text="Enter Master Password",font=("Arial",18))
    label_password.pack(padx=20,pady=20)
    global master_password
    master_password=customtkinter.CTkEntry(master=frame, placeholder_text="Master Passsword",show="•")
    master_password.pack(padx=20,pady=20)
    button=customtkinter.CTkButton(master=frame,text="Submit",font=("Arial",18), command=check)
    button.pack(padx=20,pady=20)
    look_window.mainloop()

def destroy():
    root.destroy()

root=customtkinter.CTk()

root.geometry("500x350")
root.minsize(500,350)
root.maxsize(500,350)
root.title("Passoword Manager")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=60,pady=20,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame, text="Password Manager", font=("Arial",24))
label.pack(padx=20,pady=20)

create_button=customtkinter.CTkButton(master=frame,text="Create",font=("Arial",18),command=create)
See_password=customtkinter.CTkButton(master=frame,text="See Password",font=("Arial",18),command=master_password)
exit=customtkinter.CTkButton(master=frame,text="Exit",font=("Arial",18),command=destroy)
create_button.pack(padx=20,pady=20)
See_password.pack(padx=20,pady=20)
exit.pack(padx=20,pady=20)

root.mainloop()
