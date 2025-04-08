# 🤖 WhatsApp Auto-Responder Bot (with GUI)

This is a Python-based WhatsApp Auto-Responder bot that works in the background using **Selenium** and **Tkinter**. It allows you to:
- Scan QR code and save session
- Run in **headless mode** without opening Chrome
- Auto-reply to new messages
- Customize message detection class and session path from the GUI

---

## 🧰 Features

- ✅ Headless browser automation using Selenium
- ✅ GUI using Tkinter (Start, Stop, Login)
- ✅ Customizable inputs:
  - Notification badge selector (`messagesNotificationClass`)
  - Chrome session directory (`user_data`)
- ✅ Session persistence (no need to scan QR every time)

---

## 🖥️ How it Works

1. You **scan the QR code** (once) to save your WhatsApp session.
2. You start the bot — it runs in **headless mode** and checks for new messages.
3. If a new chat is detected, it sends an automatic reply.
4. The bot keeps running in the background until stopped.

---

## 🚀 Getting Started

### 1. Install Dependencies, 

pip install -r requirements.txt


Make sure you have Python installed. Then run:

python whatsappAutoResponder.py

```bash
pip install selenium
