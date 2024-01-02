import tkinter as tk
from tkinter import ttk
from tkinter import *
from bs4 import BeautifulSoup
import requests

def download_image(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

def get_weather():
    base_url = f"https://havadurumu15gunluk.xyz/havadurumu/630/istanbul-hava-durumu-15-gunluk.html"

    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        weather_info = soup.find("span", class_="status")
        temperature = soup.find("span", class_="temperature type-1")
        #image_url = "https://www.iconsdb.com/icons/preview/orange/sun-xxl.png"

        if weather_info and temperature:
            result_label.config(text= weather_info.text.strip())
            result_label2.config(text=temperature.text.strip())

            
            global image
            image = PhotoImage(file="sun-128.png")
            canvas.create_image(0, 0, anchor=NW, image=image)
        else:
            result_label.config(text="Hava durumu bilgisi alınamadı.")
    except Exception as e:
        result_label.config(text=f"Hata oluştu: {e}")

# Tkinter penceresini oluştur
window = tk.Tk()
window.title("Hava Durumu Uygulaması")
window.minsize(width=150, height=250)

# Arayüz elemanlarını oluştur
canvas = Canvas(height=130, width=130)
canvas.grid(row=0, column=0, columnspan=1, pady=5)

result_label = ttk.Label(window, text="", font=("Helvetica", 12, "bold"))
result_label2 = ttk.Label(window, text="", font=("Helvetica", 50, "bold"))

result_label.grid(row=1, column=0, columnspan=2, pady=5)
result_label2.grid(row=2, column=0, columnspan=2, pady=7)

# Hava durumu bilgilerini otomatik olarak çek
get_weather()

# Tkinter penceresini başlat
window.mainloop()
