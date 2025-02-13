import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

import qrcode as qr

qrimage = None 

def convertbutton_click():
    global qrimage
    link=textbox.get("1.0",tk.END).strip()
    textbox.delete("1.0",tk.END)

    qr_code=qr.make(link)
    qr_code.save("Your QR Code.png")

    qrimage = Image.open("Your QR Code.png")
    qrimageframe= ImageTk.PhotoImage(qrimage)

    for widget in frame.winfo_children():
        widget.destroy()
    qrlabel = tk.Label(frame, image=qrimageframe, bg="ghostwhite",width=350,height=350)
    qrlabel.image = qrimageframe
    qrlabel.pack(padx=100)

def Downloadbutton_Click():
    global qrimage
    if qrimage:
        filepath=filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files","*.png"),("All files","*.*")],title="Save QR Code")
        if filepath:
            qrimage.save(filepath)  
            tk.messagebox.showinfo("Download Complete", "QR Code has been downloaded!")
    else:
        tk.messagebox.showwarning("No QR Code", "Please generate a QR Code first!")

root = tk.Tk()
root.geometry("700x750")
root.title("QR Code Generator")
root.configure(bg="ghostwhite")

textboxlabel = tk.Label(root, text="Enter URL: ", font=("Arial",20),fg="black",bg="ghostwhite")
textboxlabel.pack(padx=20, pady=20,anchor="w") 

textbox = tk.Text(root, height=3, font=('Arial', 16),)
textbox = tk.Text(root, height=3, font=('Arial', 16),relief="solid",borderwidth=2)
textbox.pack(padx=20)

convert_button=tk.Button(root,text="Convert",font=('Arial',16),width=12, height=2,command=convertbutton_click,bg="lightcoral")
convert_button.pack(pady=20)

frame=tk.Frame(root,bg="white",width=350,height=350,relief="solid", borderwidth=2)
frame.pack(padx=20,pady=10,fill="both",expand=False)

download_QRbutton=tk.Button(root,text="Download QR",font=('Arial',16),width=12, height=2,command=Downloadbutton_Click,bg="lightcoral")
download_QRbutton.pack(pady=20)

root.mainloop()
