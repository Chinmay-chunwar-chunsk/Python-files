import os
import customtkinter as c
from PIL import Image, ImageTk
import string
import shutil
available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]


c.set_appearance_mode("Sytem")

class FileManager:
	def __init__(self,root):
		self.root=root
	
	def Frame(self):
		global filewindow
		filewindow=c.CTkFrame(master=root,corner_radius=20)
		filewindow.pack(padx=5,pady=5,fill="both",expand=True)
		os.chdir("./assest")
		img = c.CTkImage(Image.open("all.img"),size=(35,35))
		os.chdir("../")
		head=c.CTkLabel(master=filewindow,text="Drives                                |Total Size              |Free Space",font=("Arial",18))
		head.grid(row=1, columnspan=5)
		counter=2
		for i in available_drives:
			if i.lower()=="c:":
				drive=c.CTkButton(master=filewindow,
				    image=img,
					text="Windows "+"("+i+")",
					font=("Arial",18),
					corner_radius=8,
					fg_color="transparent",
					command=lambda m=i: FileManager.ButtonClick(m)			 
					 )
				drive.grid(row=counter, column=0,sticky="w")
				
				
				total, used, free = shutil.disk_usage(i)
				newtotal="%d GB" % (total // (2**30))
				newused="%d GB" % (free // (2**30))
				totallabel=c.CTkLabel(master=filewindow,text=newtotal,font=("Arial",18))
				usedlabel=c.CTkLabel(master=filewindow,text=newused,font=("Arial",18))
				totallabel.grid(row=counter,column=1,sticky="w")
				usedlabel.grid(row=counter,column=4,sticky="w")
				counter+=1
			else:
				drive=c.CTkButton(master=filewindow,
				    image=img,
					text="New Volume"+"("+i+")",
					font=("Arial",18),
					corner_radius=8,
					fg_color="transparent",
					command=lambda m=i: FileManager.ButtonClick(m)			 
					 )
				drive.grid(row=counter, columnspan=1,sticky="w")
				total, used, free = shutil.disk_usage(i)
				newtotal="%d GB" % (total // (2**30))
				newused="%d GB" % (free // (2**30))
				totallabel=c.CTkLabel(master=filewindow,text=newtotal,font=("Arial",18))
				usedlabel=c.CTkLabel(master=filewindow,text=newused,font=("Arial",18))
				totallabel.grid(row=counter,column=1,sticky="w")
				usedlabel.grid(row=counter,column=4,sticky="w")
				counter+=1

	def ButtonClick(m):
		img = c.CTkImage(Image.open("./assest/folder (2).img"),size=(35,35))
		for object in filewindow.winfo_children():
			object.destroy()
		os.chdir(m)
		counter=0
		for i in os.listdir():
			if os.path.isfile(i):
				button=c.CTkButton(master=filewindow,
		    		text=i,
			    	font=("Arial",18),
			    	corner_radius=8,
			    	fg_color="transparent",
			    	command=lambda m=i,dirc=os.getcwd(): FileManager.typeFile(m,dirc)
				)
				button.grid(row=counter,column=1)
				counter+=1

			elif os.path.isdir(i):
				print("folder")
		os.chdir("E:/Python/GitHub projects/Python-files")

	def typeFile(m,dirc):
		print("ok")
		os.chdir(dirc)
		data=""
		with open(m,"r") as file:
			data=file.read()
		type=c.CTk()
		type.title(m)
		new=c.CTkLabel(master=type,text=data,font=("Arial",18))
		new.grid(row=0,column=0)
		type.mainloop()



root=c.CTk()

root.title("File Manager")
fm=FileManager(root)
fm.Frame()

root.mainloop()
