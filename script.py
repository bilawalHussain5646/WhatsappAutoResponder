from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import the Keys module
import time

AUTO_REPLY_TEXT = "Hello! Thanks for messaging. I'll get back to you soon."

options = webdriver.ChromeOptions()
options.add_argument("headless")  # Run in background
options.add_argument("user-data-dir=E:\\Github Projects\\Whatsapp AutoResponder\\user_data")  # Absolute path for Windows
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")

time.sleep(10)  # Wait for page to load (increase if needed)


messagesNotificationClass=".x1rg5ohu.x173ssrc.x1xaadd7.x682dto.x1e01kqd.x12j7j87.x9bpaai.x1pg5gke.x1s688f.xo5v014.x1u28eo4.x2b8uid.x16dsc37.x18ba5f9.x1sbl2l.xy9co9w.x5r174s.x7h3shv"

def auto_reply():
    print("🤖 Bot is running in background...")
    while True:
        try:
            unread_chats = driver.find_elements(By.CSS_SELECTOR, f"{messagesNotificationClass}")  # WhatsApp unread badge class

            num = 0
            for chat in unread_chats:
                if num==0:
                    num+=1
                else:
                    chat.click()
                    time.sleep(1)

                    msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                    msg_box.send_keys(AUTO_REPLY_TEXT)
                    msg_box.send_keys("\n")
                    msg_box.send_keys(Keys.ESCAPE)
                    time.sleep(1)

        except Exception as e:
            print("⚠️ Error:", e)

        time.sleep(5)

try:
    auto_reply()
except KeyboardInterrupt:
    print("🛑 Bot stopped.")
    driver.quit()
