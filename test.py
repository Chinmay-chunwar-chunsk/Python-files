import ttkbootstrap as ttk
def test(Entry):
    string=Entry.get()
    print(string)

root=ttk.Window()
Entry=ttk.Entry(master=root)
button=ttk.Button(master=root,text="ok",command=lambda Entry=Entry: test(Entry))
Entry.pack(padx=20,pady=20)
button.pack(padx=20,pady=20)
root.mainloop()