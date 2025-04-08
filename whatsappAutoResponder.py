import tkinter as tk
from threading import Thread, Event
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import shutil
import os

driver = None
stop_event = Event()

def start_bot(status_label, notif_class, user_data_path):
    global driver
    stop_event.clear()

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument(f"user-data-dir={user_data_path}")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com")

    status_label.config(text="🔄 Waiting for WhatsApp to load...")
    time.sleep(10)
    status_label.config(text="✅ Bot Running...")

    while not stop_event.is_set():
        try:
            unread_chats = driver.find_elements(By.CSS_SELECTOR, notif_class)

            for i, chat in enumerate(unread_chats):
                if i == 0:
                    continue
                chat.click()
                time.sleep(1)
                msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                msg_box.send_keys("Hello! Thanks for messaging. I'll get back to you soon.")
                msg_box.send_keys("\n")
                msg_box.send_keys(Keys.ESCAPE)
                time.sleep(1)

        except Exception as e:
            print("⚠️ Error:", e)

        time.sleep(5)

    status_label.config(text="⛔ Bot Stopped")
    driver.quit()

def login_session(status_label, user_data_path):
    def run_login():
        if os.path.exists(user_data_path):
            try:
                shutil.rmtree(user_data_path)
                print("🧹 Old session deleted.")
            except Exception as e:
                print(f"⚠️ Failed to delete session folder: {e}")
                status_label.config(text="❌ Failed to delete session folder")
                return

        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={user_data_path}")
        driver = webdriver.Chrome(options=options)
        driver.get("https://web.whatsapp.com")
        status_label.config(text="🔑 Scan QR code in browser...")
        print("🔑 Scan the QR code in the browser window...")
        time.sleep(30)
        driver.quit()
        status_label.config(text="✅ Session saved!")

    Thread(target=run_login, daemon=True).start()

def launch_gui():
    window = tk.Tk()
    window.title("WhatsApp Auto-Responder")
    window.geometry("400x400")

    # Input fields
    tk.Label(window, text="🔔 Notification CSS Selector:", anchor="w").pack(fill="x", padx=10, pady=(10, 0))
    notif_entry = tk.Entry(window, width=50)
    notif_entry.insert(0, ".x1rg5ohu.x173ssrc.x1xaadd7.x682dto.x1e01kqd.x12j7j87.x9bpaai.x1pg5gke.x1s688f.xo5v014.x1u28eo4.x2b8uid.x16dsc37.x18ba5f9.x1sbl2l.xy9co9w.x5r174s.x7h3shv")
    notif_entry.pack(padx=10, pady=5)

    tk.Label(window, text="📁 Chrome User Data Path:", anchor="w").pack(fill="x", padx=10, pady=(10, 0))
    path_entry = tk.Entry(window, width=50)
    path_entry.insert(0, "E:\\Github Projects\\Whatsapp AutoResponder")
    path_entry.pack(padx=10, pady=5)

    status_label = tk.Label(window, text="🟡 Idle", font=("Arial", 12))
    status_label.pack(pady=10)

    def start():
        notif_class = notif_entry.get().strip()
        user_data_path = path_entry.get().strip()
        Thread(target=start_bot, args=(status_label, notif_class, user_data_path), daemon=True).start()
        status_label.config(text="🟢 Starting...")

    def stop():
        stop_event.set()
        status_label.config(text="🛑 Stopping...")

    def login():
        user_data_path = path_entry.get().strip()
        user_data_path = user_data_path + "\\user_data"
        # print(user_data_path)
        # time.sleep(50)
        login_session(status_label, user_data_path)

    tk.Button(window, text="Start Bot", command=start, width=20, bg="green", fg="white").pack(pady=5)
    tk.Button(window, text="Stop Bot", command=stop, width=20, bg="red", fg="white").pack(pady=5)
    tk.Button(window, text="Login (Scan QR)", command=login, width=20, bg="blue", fg="white").pack(pady=5)

    tk.Label(window, text="Status:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
    status_label.pack()

    window.mainloop()

if __name__ == "__main__":
    launch_gui()
