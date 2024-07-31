import tkinter as tk
from tkinter import filedialog, messagebox
import requests

def send_line_notify():
    URL = 'https://notify-api.line.me/api/notify'
    H = {'Authorization': f'Bearer {token_entry.get()}'}
    P = {'message': message_entry.get()}
    
    selected_option = option_var.get()
    
    if selected_option == 'Line Sticker':
        P['stickerPackageId'] = sticker_package_id_entry.get()
        P['stickerId'] = sticker_id_entry.get()
        requests.post(URL, headers=H, params=P)
        messagebox.showinfo("Success", "Line Sticker Sent Successfully!")
    
    elif selected_option == 'Local Image File':
        file_path = file_path_entry.get()
        with open(file_path, 'rb') as f:
            F = {'imageFile': f}
            requests.post(URL, headers=H, params=P, files=F)
        messagebox.showinfo("Success", "Local Image File Sent Successfully!")
    
    elif selected_option == 'Web Image File':
        IMG = image_url_entry.get()
        response = requests.get(IMG)
        F = {'imageFile': ('image.jpg', response.content, 'image/jpeg')}
        requests.post(URL, headers=H, params=P, files=F)
        messagebox.showinfo("Success", "Web Image File Sent Successfully!")

def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def update_ui(*args):
    selected_option = option_var.get()
    if selected_option == 'Line Sticker':
        sticker_package_id_label.grid(row=5, column=0)
        sticker_package_id_entry.grid(row=5, column=1)
        sticker_id_label.grid(row=6, column=0)
        sticker_id_entry.grid(row=6, column=1)
        file_path_label.grid_forget()
        file_path_entry.grid_forget()
        browse_button.grid_forget()
        image_url_label.grid_forget()
        image_url_entry.grid_forget()
    elif selected_option == 'Local Image File':
        sticker_package_id_label.grid_forget()
        sticker_package_id_entry.grid_forget()
        sticker_id_label.grid_forget()
        sticker_id_entry.grid_forget()
        file_path_label.grid(row=5, column=0)
        file_path_entry.grid(row=5, column=1)
        browse_button.grid(row=5, column=2)
        image_url_label.grid_forget()
        image_url_entry.grid_forget()
    elif selected_option == 'Web Image File':
        sticker_package_id_label.grid_forget()
        sticker_package_id_entry.grid_forget()
        sticker_id_label.grid_forget()
        sticker_id_entry.grid_forget()
        file_path_label.grid_forget()
        file_path_entry.grid_forget()
        browse_button.grid_forget()
        image_url_label.grid(row=5, column=0)
        image_url_entry.grid(row=5, column=1)

app = tk.Tk()
app.title("LINE Notify GUI")

tk.Label(app, text="Authorization Token").grid(row=0, column=0)
token_entry = tk.Entry(app, width=50)
token_entry.grid(row=0, column=1)

tk.Label(app, text="Message").grid(row=1, column=0)
message_entry = tk.Entry(app, width=50)
message_entry.grid(row=1, column=1)

option_var = tk.StringVar(app)
option_var.set('Line Sticker')
option_var.trace('w', update_ui)

tk.Label(app, text="Send Option").grid(row=2, column=0)
option_menu = tk.OptionMenu(app, option_var, 'Line Sticker', 'Local Image File', 'Web Image File')
option_menu.grid(row=2, column=1)

sticker_package_id_label = tk.Label(app, text="Sticker Package ID")
sticker_package_id_entry = tk.Entry(app, width=50)

sticker_id_label = tk.Label(app, text="Sticker ID")
sticker_id_entry = tk.Entry(app, width=50)

file_path_label = tk.Label(app, text="File Path")
file_path_entry = tk.Entry(app, width=50)
browse_button = tk.Button(app, text="Browse", command=browse_file)

image_url_label = tk.Label(app, text="Image URL")
image_url_entry = tk.Entry(app, width=50)

send_button = tk.Button(app, text="Send", command=send_line_notify)
send_button.grid(row=7, column=1)

update_ui()  # Initialize the UI based on the default option

app.mainloop()