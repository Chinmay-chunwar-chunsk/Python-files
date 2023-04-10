import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.scrolled import ScrolledFrame
import string
import os
from PIL import Image, ImageTk
import time
available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
os.chdir("C:\\")

#Main App
class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.geometry("1500x700")
        new=Files(self)
        editor=Editor(self)
        # self.columnconfigure(2,weight=4)
        self.mainloop()


# QuickAccess and other things
class Files(ScrolledFrame):
    def __init__(self,parent):
        super().__init__(parent,autohide=True,width=200,height=700)
        self.grid(row=0,column=0,sticky="w")

        #Styles
        buttonstyle=ttk.Style(theme="darkly")
        buttonstyle.configure('TButton',borderwidth=0)

        #QuickAccess
        Files.QuickAccess_command(self)
    
    def QuickAccess_command(self):
        for objects in self.winfo_children():
            objects.destroy()
        QuickAccess=ttk.Button(master=self,text="Quick Access",style="warning-outline",command=lambda m=self: Files.Destroy_Elements(m))
        QuickAccess.grid(row=0,column=0)
        counter=1
        for drive in available_drives:
            if drive.lower()=="c:":
                newdrive=ttk.Button(master=self,text="Windows_OS (C:)",style="primary-outline",command=lambda m=drive: Editor.drive_commands(m))
                newdrive.grid(row=counter,column=0)
                counter+=1
            else:
                newdrive=ttk.Button(master=self,text=f"New Volume ({drive})",style="primary-outline",command=lambda m=drive: Editor.drive_commands(m))
                newdrive.grid(row=counter,column=0)
                counter+=1

    def Destroy_Elements(self):
        for objects in self.winfo_children():
            objects.destroy()
        QuickAccess=ttk.Button(master=self, text="Quick Access",style="warning-outline",command=lambda m=self: Files.QuickAccess_command(m))
        QuickAccess.grid(row=0,column=0)
        

#Editor Window

class Editor(ScrolledFrame):
    def __init__(self,parent):
        super().__init__(parent,width=1160,height=700)
        self.grid(row=0,column=2,sticky="e")
        global Editorself
        Editorself=self
        Editor.back_button()
        Editor.title_button()


    def getfilesize(item,counter):
        unit="bytes"
        file_size = os.path.getsize(item)
        exponents_map = {'bytes': 0, 'kb': 1, 'mb': 2, 'gb': 3}
        if unit not in exponents_map:
            raise ValueError("Must select from \
            ['bytes', 'kb', 'mb', 'gb']")
        else:
            size = file_size / 1024 ** exponents_map[unit]
            label=ttk.Label(master=Editorself,text=str(size)+" MB")
            label.grid(row=counter,column=2)

    #title buttons
    def title_button():
        Name=ttk.Button(master=Editorself, text="Name",style="light-outline",width=20,command=lambda m=os.getcwd(): Editor.drive_commands(m))
        Name.grid(row=1,column=0,sticky="w")
        label=ttk.Label(master=Editorself,text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        label.grid(row=2,columnspan=5)
        Size=ttk.Button(master=Editorself,text="Size",style="light-outline",width=20)
        Size.grid(row=1,column=2)
        entry=ttk.Entry(master=Editorself,width=100)
        entry.grid(row=0,column=1,sticky="w")
        go=ttk.Button(master=Editorself,text="GO",style="info-outline",width=30,command=lambda Entry=entry: Editor.get_dir(Entry))
        go.grid(row=0,column=2,sticky="w")

    def get_dir(Entry):
        drive=Entry.get()
        Editor.drive_commands(drive)

    #back button command
    def back_button_command():
        #variables
        pwd=os.getcwd()
        newpath=[]
        name=""
        newdir=""

        #checking if user is already in root of drive
        if pwd=="C:\\":
            toast=ToastNotification(title="File Explorer Error",message="Cannot go back any more directories",duration=5000)
            toast.show_toast()
        elif pwd=="D:\\":
            toast=ToastNotification(title="File Explorer Error",message="Cannot go back any more directories",duration=5000)
            toast.show_toast()
        elif pwd=="E:\\":
            toast=ToastNotification(title="File Explorer Error",message="Cannot go back any more directories",duration=5000)
            toast.show_toast()
        elif pwd=="F:\\":
            toast=ToastNotification(title="File Explorer Error",message="Cannot go back any more directories",duration=5000)
            toast.show_toast()
        else:
            
            for letter in pwd:
                if letter=="\\":
                    newpath.append(name)
                    name=""
                    pass
                else:
                    name+=letter
            for path in newpath:
                newdir+=path
                newdir+="\\"
        Editor.drive_commands(newdir)
        print(newpath)

    #Previous Directory button
    def back_button():
        back=ttk.Button(master=Editorself, text="BACK",style="info-outline",command=Editor.back_button_command)
        back.grid(row=0,column=0,sticky="w")
        

    #commands for create drives
    def drive_commands(drive):
        print(type(drive))
        os.chdir(drive)
        pwd=os.getcwd()
        for objects in Editorself.winfo_children():
            objects.destroy()
        Editor.back_button()
        Editor.title_button()
        counter=3
        for item in os.listdir():
            
            #storing \ in string variable
            slash="\\"

            #files
            if os.path.isfile(item):
                Editor.getfilesize(item,counter)
                newfile=ttk.Button(master=Editorself,text=item,style="light-outline",command=lambda m=item: Editor.type_file(m))
                newfile.grid(row=counter,column=0,sticky="w")
                counter+=1
            #folder
            elif os.path.isdir(item):
                Editor.getfilesize(item,counter)
                newfolder=ttk.Button(master=Editorself,text=item, style="light-outline",command=lambda next=str(drive+slash+item): Editor.drive_commands(next))
                newfolder.grid(row=counter,column=0,sticky="w")
                counter+=1

    #typing selected file
    def type_file(m):
        root=ttk.Window(themename="darkly")
        root.title(m)
        data=""
        with open(m,"r") as file:
            data=file.read()
        label=ttk.Label(master=root,text=data)
        label.pack(fill="both",expand=True)
        root.mainloop()
App()