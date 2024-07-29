import tkinter as tk
import requests
from tkinter import messagebox

def send_message():
    URL = 'https://notify-api.line.me/api/notify'
    token = 'Jtd5DlFVD4kYq58F0m0ycM44EQmv00GDSfLRjs1QH5H'  # 替換為你的實際 Token
    message = entry.get()
    
    if message.strip():
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {
            'message': message
        }
        response = requests.post(URL, headers=headers, params=data)
        
        if response.status_code == 200:
            messagebox.showinfo("Success", "訊息已成功傳送!")
        else:
            messagebox.showerror("Error", f"傳送失敗! 狀態碼: {response.status_code}")
    else:
        messagebox.showwarning("Warning", "訊息不能為空!")

# 建立 GUI 視窗
root = tk.Tk()
root.title("LINE Notify 傳送訊息")

# 訊息輸入欄
label = tk.Label(root, text="輸入訊息:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# 送出按鈕
button = tk.Button(root, text="送出", command=send_message)
button.pack(pady=10)

# 啟動 GUI 主迴圈
root.mainloop()
