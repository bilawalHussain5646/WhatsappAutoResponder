from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=E:\\Github Projects\\Whatsapp AutoResponder\\user_data")  # Absolute path for Windows


driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")
print("🔑 Scan the QR code in the browser window...")

time.sleep(30)  # Wait for manual scan
driver.quit()
print("✅ Session saved. You can now run in headless mode.")
