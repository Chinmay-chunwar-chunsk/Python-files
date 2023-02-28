import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def create():
    create_window=customtkinter.CTk()
    create_window.title("Create Account")
    create_window.geometry("500x350")
    create_window.minsize(500,350)
    create_window.maxsize(500,350)


    label=customtkinter.CTkLabel(master=create_window,text="Account", font=("Arial", 24))
    label.pack(padx=20,pady=20)
    username=customtkinter.CTkEntry(master=create_window, placeholder_text="Username",font=("Arial",18))
    username.pack(padx=20,pady=20)
    password=customtkinter.CTkEntry(master=create_window, placeholder_text="Password",show="•",font=("Aria;",18))
    password.pack(padx=20,pady=20)
    submit=customtkinter.CTkButton(master=create_window,text="Submit",font=("Arial",18))
    submit.pack(padx=20,pady=20)

    create_window.mainloop()

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
See_password=customtkinter.CTkButton(master=frame,text="See Password",font=("Arial",18))
exit=customtkinter.CTkButton(master=frame,text="Exit",font=("Arial",18))
create_button.pack(padx=20,pady=20)
See_password.pack(padx=20,pady=20)
exit.pack(padx=20,pady=20)

root.mainloop()