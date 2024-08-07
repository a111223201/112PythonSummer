import requests
import tkinter as tk
from tkinter import ttk, messagebox

# API 端點和授權標頭
URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
headers = {
    'Authorization': 'CWA-1DC7471C-30C9-4497-9682-451134DF031E'
}

# 全局變量，用來存儲從 API 獲取的數據
records = []

# 獲取氣象資料的函數
def fetch_data():
    global records
    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status()  # 觸發 HTTPError 為錯誤狀態碼
        data = response.json()
        # 確保 'records' 和 'Station' 鍵存在
        if 'records' in data and 'Station' in data['records']:
            records = data['records']['Station']
            return True
        else:
            messagebox.showerror("錯誤", "數據格式錯誤")
            return False
    except requests.RequestException as e:
        messagebox.showerror("錯誤", f"請求失敗: {e}")
        return False

# 更新下拉式選單的選項
def update_station_options():
    if fetch_data():
        station_names = [record['StationName'] for record in records]
        station_combobox['values'] = station_names
        # 確保選單在更新後顯示第一個選項
        if station_names:
            station_combobox.set(station_names[0])

# 顯示所選站點的氣象資訊
def show_station_info(event=None):
    selected_station = station_combobox.get()
    for record in records:
        if record['StationName'] == selected_station:
            obs_time = record.get('ObsTime', {}).get('DateTime', 'N/A')
            air_temp = record['WeatherElement'].get('AirTemperature', 'N/A')
            rel_humidity = record['WeatherElement'].get('RelativeHumidity', 'N/A')
            weather = record['WeatherElement'].get('Weather', 'N/A')
            info_text = (
                f"觀測地點: {record['StationName']}\n"
                f"觀測時間: {obs_time}\n"
                f"觀測溫度: {air_temp} °C\n"
                f"觀測濕度: {rel_humidity} %\n"
                f"觀測天氣: {weather}"
            )
            messagebox.showinfo("站點資訊", info_text)
            return
    messagebox.showwarning("警告", "選擇的站點不存在")

# 創建 GUI
root = tk.Tk()
root.title("台灣氣象觀測站點查詢")

# 創建下拉式選單
station_combobox = ttk.Combobox(root)
station_combobox.pack(padx=10, pady=10)

# 創建查詢按鈕
query_button = tk.Button(root, text="查詢", command=show_station_info)
query_button.pack(pady=5)

# 當下拉選單選擇變化時更新資訊
station_combobox.bind("<<ComboboxSelected>>", show_station_info)

# 更新下拉式選單的選項
update_station_options()

# 啟動主循環
root.mainloop()