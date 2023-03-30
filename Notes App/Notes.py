import customtkinter as c
import os

#new widgets
def new_widgets():
    global files
    files=[]
    namelisthead=c.CTkLabel(master=namelist,text="Notes",font=("Arial",15))
    namelisthead.pack(side="top")
    create_new=c.CTkButton(master=namelist,text="New",font=("Arial",15),command=create_new_file)
    create_new.pack(side="top")
    delete_button=c.CTkButton(master=namelist,text="Delete",font=("Arial",15),command=select_file)
    delete_button.pack(pady=2,side="top")
    test=c.CTkLabel(master=namelist,text="")
    test.pack(padx=2,pady=2)
    os.chdir("./Notes")
    for file in os.listdir():
        files.append(file)
    for i in files:
        button=c.CTkButton(master=namelist,text=i,font=("Arial",15),fg_color="#2a2a2a")
        button.configure(command=lambda m=i: type_file(m))
        button.pack()
    os.chdir("../")

#to delete file
def delete_file():
    os.chdir("./Notes")
    os.remove(dropdown.get())
    delete_window.destroy()
    os.chdir("../")
    for widgets in namelist.winfo_children():
        widgets.destroy()
    new_widgets()
    
#To select file
def select_file():
    global dropdown
    global delete_window
    delete_window=c.CTk()
    dropdown_files=[]
    delete_window.title("Delete window")
    frame=c.CTkFrame(master=delete_window)
    frame.pack(padx=20,pady=20)
    label=c.CTkLabel(master=frame,text="Select File",font=("Arial",18))
    label.pack(padx=20,pady=20)
    dropdown=c.CTkComboBox(master=frame)
    dropdown.set("")
    os.chdir("./Notes")
    for file in os.listdir():
        dropdown_files.append(file)
    os.chdir("../")
    dropdown.configure(values=dropdown_files)
    dropdown.pack(padx=20,pady=20)
    submit=c.CTkButton(master=frame,text="Submit",font=("Arial",18),command=delete_file)
    submit.pack(padx=20,pady=20)

    delete_window.mainloop()

#saves files
def save_file(tab):
    os.chdir("./Notes")
    with open(button_name,"w") as file:
        data=text.get(1.0,"end-1c")
        file.write(data)
    os.chdir("../")
    tabview.delete(tab)

#for files that already exists
def type_file(button):
    global button_name
    button_name=button
    tabview.add(button_name)
    tab=tabview.tab(button_name)
    global text
    text=c.CTkTextbox(master=tab,font=("Arial",15))
    text.pack(padx=5,pady=5,fill="both",expand=True)
    os.chdir("./Notes")
    with open(button,"r") as file:
        data=file.read()
        text.insert("0.0",data)
    os.chdir("../")
    global save_button
    save_button=c.CTkButton(master=tab,text="Save",font=("Arial",15),command=lambda m=button_name: save_file(m))
    save_button.pack(padx=5,pady=5)

#error for submiting
def check():
    counter=0
    os.chdir("./Notes")
    files=[]
    for i in os.listdir():
        files.append(i)
    os.chdir("../")
    if len(files)==0:
        get()
    for i in files:
        if file_name.get()+".txt"==i:
            error_window=c.CTk()
            error_window.title("Error")
            frame=c.CTkFrame(master=error_window)
            frame.pack(padx=60,pady=20,fill="both",expand=True)
            test=c.CTkLabel(master=frame,text="File already exists",font=("Arial",18))
            test.pack(padx=20,pady=20)
            error_window.mainloop()
        else:
            counter+=1
            if counter==len(files):
                get()
    

# a sub function of create
def get():
    name=file_name.get()
    with open("./Notes/"+name+".txt","w") as file:
        file.write("")
    Button=c.CTkButton(master=namelist, text=name+".txt",font=("Arial",15),fg_color="#2a2a2a",command=lambda m=name+".txt": type_file(m))
    Button.pack(side="top")
    create_window.destroy()

#creates and opens a file
def create_new_file():
    global create_window
    create_window=c.CTk()
    frame=c.CTkFrame(master=create_window)
    create_window.title("File Name")
    frame.pack(fill="both",expand=True,padx=20,pady=20)
    label=c.CTkLabel(master=frame,text="Enter File name",font=("Arial",18))
    label.pack(padx=20,pady=20)
    global file_name
    file_name=c.CTkEntry(master=frame,placeholder_text="File Name", font=("Arial",18))
    file_name.pack(padx=20,pady=20)
    submit=c.CTkButton(master=frame,text="Submit",font=("Arial",18),command=check)
    submit.pack(padx=20,pady=20)
    create_window.mainloop()    


c.set_appearance_mode("System")
c.set_default_color_theme("green")
root=c.CTk()
root.geometry("1000x500")
root.title("Notes")
writehere=c.CTkFrame(master=root)
writehere.pack(side="right",fill="both",padx=10,expand=True)
tabview=c.CTkTabview(master=writehere)
tabview.pack(padx=2,pady=2,fill="both",expand=True,side="left")
namelist=c.CTkScrollableFrame(master=root,orientation="vertical")
namelist.pack(side="left",fill="both")
new_widgets()
root.mainloop()