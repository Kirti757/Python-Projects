import tkinter as tk

def addbutton_click():
    task= textbox.get("1.0", tk.END).strip()
    textbox.delete("1.0", tk.END)

    if task:

        var=tk.BooleanVar()
        checkbox=tk.Checkbutton(frame,text=task,variable=var,font=('Arial',16),anchor="w", bg="white", fg="black")
        checkbox.var=var
        checkbox.pack(fill="x",anchor="w")
        tasks.append(checkbox)
  
def deletebutton_click():
    for task in tasks[:]:
        if task.var.get():
            task.destroy()
            tasks.remove(task)
    
def updatebutton_click():
    for task in tasks[:]:
        if task.var.get():
             textbox.delete("1.0",tk.END)
             textbox.insert("1.0", task.cget("text"))
             task.destroy()
             tasks.remove(task)
             break  
      
root=tk.Tk()
root.geometry("500x700")
root.configure(bg='floral white')
root.title("To-Do-List")

label = tk.Label(root, text="The To-Do-List", font=("Courier New",20,"bold"),bg="floral white",fg="brown")
label.pack(padx=20, pady=20) 

textbox=tk.Text(root,height=2,font=('Arial ',16),relief="solid", borderwidth=2)
textbox.pack(padx=20,pady=20)


frame=tk.Frame(root,bg="floral white")
frame.pack(padx=20,pady=10,fill="both",expand=True)

tasks=[]

add_button=tk.Button(root,text="Add",font=('Arial',16),width=20, height=2,bg="light green",fg="black",command=addbutton_click,relief="solid" ,borderwidth=2)
add_button.pack()


upd_button=tk.Button(root,text="Update",font=('Arial',16),width=20, height=2,bg="salmon",fg="black",command=updatebutton_click,relief="solid", borderwidth=2)
upd_button.pack(pady=20)

del_button=tk.Button(root,text="Delete",font=('Arial',16),width=20, height=2,bg="brown4",fg="black",command=deletebutton_click,relief="solid", borderwidth=2)
del_button.pack(pady=10)

root.mainloop()


